# Log Prompt — PTM-05: REST API & Database

Sistem Pemantau Kepatuhan Masker Berbasis AI · Intelligent Mobile and Web Application Development

Deklarasi: AI (ChatGPT) digunakan sebagai co-pilot penyusunan draf teknis. Seluruh fakta, angka target (akurasi ≥95%, latensi <1 detik), dan keputusan arsitektur bersumber dari SRS/LLD (PTM-02–04) hasil analisis tim, bukan dikarang oleh AI.

---

## Sesi 1 — Prompt D.1: Draft OpenAPI 3.0

**Target Prompt:** D.1 OpenAPI
**Alat AI & Versi:** ChatGPT
**Ringkasan Prompt:** Meminta AI membuat spesifikasi OpenAPI 3.0 (YAML) untuk 3 endpoint (camera session, detection, detection log) berdasarkan LLD PTM-04 dan User Story Must Have (FR-01, FR-02, FR-05, FR-06, FR-08), dengan stack FastAPI + PostgreSQL.

**Kualitas Output (1-5):** 4

**Masalah pada Output AI Pertama:**
- Penamaan path masih singular/nested (`/api/camera/start`, `/api/detection`, `/api/detection/log`), belum mengikuti aturan resource naming noun jamak yang diwajibkan checklist D.1.

**Revisi Manual yang Dilakukan:**
- Path direvisi menjadi `/api/camera-sessions`, `/api/detections`, `/api/detection-logs`.
- Referensi path di bagian `description` (mis. penyebutan `/api/camera/start` di endpoint deteksi) turut disesuaikan agar konsisten.

---

## Sesi 2 — Prompt D.2: Draft ERD + Skema Pydantic

**Target Prompt:** D.2 ERD/Skema
**Alat AI & Versi:** ChatGPT
**Ringkasan Prompt:** Meminta AI membuat ERD (Mermaid) dan skema Pydantic (Python) berdasarkan `components/schemas` OpenAPI hasil revisi D.1 dan entitas `detection_logs` pada LLD, dengan penekanan constraint bisnis (enum `mask_status`, confidence 0.0–1.0, field nullable untuk fitur Should Have).

**Kualitas Output (1-5):** 4

**Masalah pada Output AI Pertama:**
- Perlu penyesuaian tipe data (`UUID` vs `int` untuk primary key) agar konsisten dengan `format: uuid` di OpenAPI.
- Belum ada penanda eksplisit bahwa sesi kamera tidak memiliki tabel database tersendiri (bersifat sementara/in-memory).

**Revisi Manual yang Dilakukan:**
- Primary key `detection_logs.id` dipastikan bertipe UUID di skema Pydantic (`models.py`), sinkron dengan `format: uuid` pada `DetectionLog` di OpenAPI.
- Ditambahkan `[ASUMSI-07]` di `erd.md` yang menandai bahwa sesi kamera dikelola sebagai state sementara, bukan entitas database — masih menunggu `[KEPUTUSAN TIM]`.

---

## Tabel Asumsi yang Ditandai AI

| Kode Asumsi | Isi Asumsi | Verifikasi Tim |
|---|---|---|
| ASUMSI-01 | Autentikasi bearer token (JWT) untuk endpoint yang membutuhkan proteksi | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-02 | `session_id` dari `/api/camera-sessions` dipakai untuk request deteksi berikutnya | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-03 | Frame dikirim sebagai `multipart/form-data`, bukan base64 | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-04 | `camera_id` opsional; sistem pakai kamera default jika kosong | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-05 | `session_id` wajib disertakan di setiap request deteksi | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-06 | Field `timestamp` di request deteksi bersifat opsional | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-07 | Sesi kamera tidak memiliki tabel database tersendiri (in-memory) | [KEPUTUSAN TIM: perlu diisi] |

> Kolom "Verifikasi Tim" wajib diisi Benar/Diubah/Dihapus sebelum submit tugas — pindahkan juga ke Bagian E.3 Lembar Kerja Praktikum (LKP-PTM-05).
