"""
Skema Pydantic v2 — sinkron dengan components/schemas pada docs/api/openapi.yaml
Sistem Pemantau Kepatuhan Masker Berbasis AI (FastAPI + PostgreSQL)
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class MaskStatus(str, Enum):
    """Status klasifikasi masker. Sinkron dengan MaskStatus di openapi.yaml."""
    MASK = "MASK"
    NO_MASK = "NO_MASK"
    UNCERTAIN = "UNCERTAIN"


class CameraSessionStatus(str, Enum):
    STARTED = "STARTED"


# ---------------------------------------------------------------------------
# Camera Session — POST /api/camera-sessions
# ---------------------------------------------------------------------------

class CameraStartRequest(BaseModel):
    camera_id: Optional[str] = Field(
        default=None, description="Identifier kamera (opsional). Jika kosong, gunakan default.", examples=["cam-lobby-01"]
    )
    resolution: Optional[str] = Field(
        default=None, description="Preferensi resolusi (opsional)", examples=["1280x720"]
    )

    model_config = {"extra": "forbid"}


class CameraStartResponse(BaseModel):
    session_id: UUID = Field(description="ID sesi kamera aktif")
    status: CameraSessionStatus
    camera_id: Optional[str] = None
    started_at: datetime


# ---------------------------------------------------------------------------
# Bounding Box (shared)
# ---------------------------------------------------------------------------

class BoundingBox(BaseModel):
    x: float = Field(description="Koordinat kiri atas (normalized 0-1 atau pixel)")
    y: float
    width: float
    height: float


# ---------------------------------------------------------------------------
# Detection — POST /api/detections
# ---------------------------------------------------------------------------

class DetectionRequest(BaseModel):
    session_id: UUID = Field(description="Session ID dari /api/camera-sessions")
    # frame dikirim sebagai multipart/form-data (UploadFile di endpoint FastAPI),
    # bukan field Pydantic biasa — lihat [ASUMSI-03].
    timestamp: Optional[datetime] = Field(
        default=None, description="Timestamp frame dari client (opsional) — [ASUMSI-06]"
    )


class DetectionResult(BaseModel):
    face_id: str = Field(description="Identifier sementara untuk wajah dalam frame", examples=["face-001"])
    mask_status: MaskStatus
    confidence: float = Field(ge=0.0, le=1.0, description="Confidence score klasifikasi masker")
    bounding_box: BoundingBox
    gender: Optional[str] = Field(default=None, description="Prediksi gender (opsional, nullable)")
    age_range: Optional[str] = Field(default=None, description="Prediksi rentang usia (opsional, nullable)")

    @field_validator("confidence")
    @classmethod
    def validate_confidence(cls, v: float) -> float:
        if not 0.0 <= v <= 1.0:
            raise ValueError("confidence harus berada di rentang 0.0 - 1.0")
        return v


class DetectionResponse(BaseModel):
    session_id: Optional[UUID] = None
    processed_at: datetime
    detections: list[DetectionResult] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Detection Log — POST /api/detection-logs
# ---------------------------------------------------------------------------

class DetectionLogCreate(BaseModel):
    timestamp: datetime = Field(description="Waktu deteksi")
    mask_status: MaskStatus
    gender: Optional[str] = None
    age_range: Optional[str] = None
    session_id: Optional[UUID] = Field(default=None, description="Opsional, korelasi ke sesi kamera")
    confidence: Optional[float] = Field(default=None, ge=0.0, le=1.0, description="Confidence score (opsional, untuk audit)")


class DetectionLog(BaseModel):
    """Representasi baris pada tabel detection_logs (lihat docs/db/erd.md)."""
    id: UUID = Field(default_factory=uuid4, description="Primary key")
    timestamp: datetime
    mask_status: MaskStatus
    gender: Optional[str] = None
    age_range: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Waktu record disimpan di database")

    model_config = {"from_attributes": True}  # agar bisa dibentuk dari ORM row (SQLAlchemy/Tortoise)


# ---------------------------------------------------------------------------
# Error Response (shared)
# ---------------------------------------------------------------------------

class ErrorResponse(BaseModel):
    error_code: str = Field(description="Kode error spesifik (sesuai LLD), mis. CAMERA_PERMISSION_DENIED")
    message: str = Field(description="Pesan human-readable")
    details: Optional[dict] = Field(default=None, description="Detail tambahan (opsional)")
