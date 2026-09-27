# DRAF LLD (LOW-LEVEL DESIGN)

## Sistem Pemantau Kepatuhan Masker Berbasis AI

### 1. Tujuan dan Scope

LLD ini menerjemahkan rancangan HLD menjadi rancangan teknis yang lebih detail untuk fitur **Must Have** pada SRS.

Fitur yang dibahas:

| ID    | Fitur                                    | Prioritas |
| ----- | ---------------------------------------- | --------- |
| FR-01 | Deteksi wajah dari live feed kamera      | Must      |
| FR-02 | Klasifikasi status penggunaan masker     | Must      |
| FR-05 | Penyajian hasil deteksi secara real-time | Must      |
| FR-06 | Pencatatan hasil deteksi                 | Must      |
| FR-08 | Penanganan kegagalan akses kamera        | Must      |

Fitur prediksi jenis kelamin, estimasi usia, ringkasan agregat, filter laporan, dan visualisasi statistik tidak menjadi bagian implementasi inti LLD ini karena bukan fitur Must Have pada SRS.

---

# 2. Desain Modul / Class

Pola arsitektur mengikuti **Clean Architecture**:

**Presentation → Application → Domain → Infrastructure**

## 2.1 Struktur Modul

```text
src/
├── presentation/
│   ├── CameraController
│   └── DetectionController
│
├── application/
│   ├── DetectionPipeline
│   ├── CameraSessionService
│   └── DetectionLogService
│
├── domain/
│   ├── DetectionResult
│   ├── FaceDetection
│   ├── MaskClassification
│   └── DetectionLog
│
└── infrastructure/
    ├── CameraAdapter
    ├── FaceDetectionModel
    ├── MaskClassificationModel
    └── DetectionRepository
```

---

## 2.2 Class `DetectionPipeline`

**Layer:** Application

**Tanggung jawab:**

* Mengatur alur utama pemrosesan frame.
* Memanggil face detection.
* Memanggil mask classification.
* Melakukan post-processing hasil.
* Menghasilkan hasil deteksi untuk ditampilkan secara real-time.
* Meneruskan hasil valid ke proses logging.

**Atribut kunci:**

```text
faceDetector
maskClassifier
detectionLogService
```

**Method utama:**

```text
processFrame(frame)
detectFaces(frame)
classifyMask(face)
buildDetectionResult()
```

**Alur:**

```text
Camera Frame
    ↓
DetectionPipeline
    ↓
FaceDetector
    ↓
MaskClassifier
    ↓
DetectionResult
    ↓
UI + DetectionLogService
```

Fungsi ini merealisasikan FR-01 dan FR-02 serta menjadi bagian utama pemenuhan FR-05 dan FR-06.

---

## 2.3 Class `CameraSessionService`

**Layer:** Application

**Tanggung jawab:**

* Mengelola sesi penggunaan kamera.
* Memulai akses kamera.
* Memeriksa status kamera.
* Menangani kamera tidak tersedia atau permission ditolak.
* Menghentikan sesi kamera dengan aman.
* Memberikan status kamera kepada Presentation Layer.

**Atribut kunci:**

```text
cameraAdapter
sessionStatus
errorHandler
```

**Method utama:**

```text
startCamera()
getCameraStatus()
stopCamera()
handleCameraError()
```

Status sesi dapat menggunakan:

```text
IDLE
STARTING
ACTIVE
FAILED
STOPPED
```

Class ini terutama digunakan untuk memenuhi FR-08 dan mendukung FR-01.

---

## 2.4 Class `DetectionLogService`

**Layer:** Application

**Tanggung jawab:**

* Menerima hasil klasifikasi yang valid.
* Membentuk data log.
* Menyimpan timestamp dan status masker.
* Tidak menyimpan gambar wajah mentah.
* Menangani kegagalan penyimpanan.

**Atribut kunci:**

```text
detectionRepository
```

**Method utama:**

```text
createLog(detectionResult)
saveLog(detectionLog)
validateLog(detectionLog)
```

Data minimum mengikuti SRS, yaitu timestamp, status masker, jenis kelamin, dan estimasi rentang usia. Namun karena fitur demografis merupakan Should Have, pada implementasi Must Have nilai tersebut dapat bernilai `null` sampai fitur terkait diaktifkan.

---

# 3. Domain Model

## 3.1 `FaceDetection`

```text
FaceDetection
-------------------------
faceId
boundingBox
confidence
```

Keterangan:

* `faceId`: identifier sementara untuk membedakan wajah dalam satu frame.
* `boundingBox`: lokasi wajah pada frame.
* `confidence`: tingkat keyakinan model mendeteksi wajah.

`faceId` bukan identitas individu dan tidak digunakan untuk face recognition.

---

## 3.2 `MaskClassification`

```text
MaskClassification
-------------------------
status
confidence
```

Nilai `status`:

```text
MASK
NO_MASK
UNCERTAIN
```

`UNCERTAIN` digunakan apabila hasil klasifikasi tidak cukup meyakinkan untuk menghasilkan status definitif.

---

## 3.3 `DetectionResult`

```text
DetectionResult
-------------------------
timestamp
faceDetection
maskClassification
```

Contoh:

```json
{
  "timestamp": "2026-09-20T10:15:30Z",
  "face": {
    "faceId": "temporary-001",
    "boundingBox": {
      "x": 120,
      "y": 80,
      "width": 150,
      "height": 180
    },
    "confidence": 0.94
  },
  "mask": {
    "status": "MASK",
    "confidence": 0.97
  }
}
```

---

# 4. Skema Data

## 4.1 Entitas `detection_logs`

Entitas utama digunakan untuk menyimpan hasil klasifikasi tanpa menyimpan gambar wajah mentah.

| Field         | Tipe           | Constraint | Keterangan                   |
| ------------- | -------------- | ---------- | ---------------------------- |
| `id`          | UUID / Integer | PK         | ID log                       |
| `timestamp`   | DateTime       | NOT NULL   | Waktu deteksi                |
| `mask_status` | VARCHAR        | NOT NULL   | Status masker                |
| `gender`      | VARCHAR        | NULL       | Disiapkan untuk fitur Should |
| `age_range`   | VARCHAR        | NULL       | Disiapkan untuk fitur Should |

Sesuai NFR-05 dan NFR-06, gambar wajah mentah tidak menjadi field pada database.

### Constraint

```text
PRIMARY KEY(id)

timestamp NOT NULL

mask_status NOT NULL

gender NULL

age_range NULL
```

Nilai `mask_status` dibatasi pada:

```text
MASK
NO_MASK
UNCERTAIN
```

### Relasi

Untuk scope Must Have:

```text
DetectionResult
      │
      ▼
DetectionLog
      │
      ▼
detection_logs
```

Tidak diperlukan relasi antar-user atau identitas individu karena sistem memang berada di luar scope identifikasi individu.

---

# 5. Pilihan Database

HLD menyediakan dua alternatif database:

### Opsi 1 — PostgreSQL

Kelebihan:

* Cocok untuk deployment server.
* Mendukung concurrent access.
* Lebih sesuai jika jumlah log berkembang.

Kekurangan:

* Membutuhkan konfigurasi database server.

### Opsi 2 — SQLite

Kelebihan:

* Sangat sederhana untuk prototype lokal.
* Tidak membutuhkan database server terpisah.

Kekurangan:

* Kurang sesuai untuk kebutuhan concurrent access yang lebih tinggi.

### [KEPUTUSAN TIM: PostgreSQL / SQLite]

**Kriteria pemilihan:**

* Target deployment.
* Jumlah akses bersamaan.
* Kemudahan pengembangan prototype.
* Ketersediaan resource deployment.

---

# 6. Spesifikasi API Detail

API mengikuti backend **Python FastAPI** sebagaimana ditetapkan pada stack HLD.

## 6.1 Start Camera

### Endpoint

```http
POST /api/camera/start
```

### Request

Tidak membutuhkan body.

### Response sukses

```json
{
  "status": "ACTIVE",
  "message": "Camera started successfully"
}
```

### Error

```json
{
  "status": "FAILED",
  "code": "CAMERA_PERMISSION_DENIED",
  "message": "Akses kamera ditolak. Silakan berikan izin kamera."
}
```

### Kode error

| HTTP | Code                       | Kondisi                   |
| ---- | -------------------------- | ------------------------- |
| 403  | `CAMERA_PERMISSION_DENIED` | Permission kamera ditolak |
| 404  | `CAMERA_NOT_FOUND`         | Kamera tidak ditemukan    |
| 500  | `CAMERA_START_FAILED`      | Kamera gagal dijalankan   |

> [ASUMSI-01] Endpoint kamera digunakan untuk mengoordinasikan status sesi; mekanisme akses kamera aktual tetap dilakukan melalui Camera Interface pada browser.

---

# 7. API Detection

## 7.1 `POST /api/detection`

Endpoint digunakan untuk mengirim input frame yang akan diproses oleh pipeline deteksi.

### Request

```json
{
  "frame": "<encoded-frame-data>",
  "timestamp": "2026-09-20T10:15:30Z"
}
```

> [ASUMSI-02] Format `encoded-frame-data` digunakan sebagai representasi frame pada komunikasi client–backend. Format final perlu ditentukan berdasarkan implementasi frontend dan kebutuhan latency.

### Response sukses

```json
{
  "timestamp": "2026-09-20T10:15:30Z",
  "detections": [
    {
      "face": {
        "faceId": "temporary-001",
        "boundingBox": {
          "x": 120,
          "y": 80,
          "width": 150,
          "height": 180
        },
        "confidence": 0.94
      },
      "mask": {
        "status": "MASK",
        "confidence": 0.97
      }
    }
  ]
}
```

### Response tidak ada wajah

```json
{
  "timestamp": "2026-09-20T10:15:30Z",
  "detections": []
}
```

### Kode error

| HTTP | Code                         | Kondisi                        |
| ---- | ---------------------------- | ------------------------------ |
| 400  | `INVALID_FRAME`              | Input frame tidak valid        |
| 408  | `INFERENCE_TIMEOUT`          | Proses AI melebihi batas waktu |
| 422  | `INVALID_INPUT`              | Data input tidak sesuai format |
| 500  | `FACE_DETECTION_FAILED`      | Face detection gagal           |
| 500  | `MASK_CLASSIFICATION_FAILED` | Mask classification gagal      |
| 503  | `AI_SERVICE_UNAVAILABLE`     | Layanan AI tidak tersedia      |

---

# 8. API Detection Log

## 8.1 `POST /api/detection/log`

Digunakan untuk menyimpan hasil klasifikasi yang telah berhasil diproses.

### Request

```json
{
  "timestamp": "2026-09-20T10:15:30Z",
  "mask_status": "MASK",
  "gender": null,
  "age_range": null
}
```

### Response

```json
{
  "status": "SUCCESS",
  "log_id": "log-001"
}
```

### Error

```json
{
  "status": "FAILED",
  "code": "LOG_SAVE_FAILED",
  "message": "Hasil deteksi belum dapat disimpan."
}
```

### Kode error

| HTTP | Code                   | Kondisi                  |
| ---- | ---------------------- | ------------------------ |
| 400  | `INVALID_LOG_DATA`     | Data log tidak valid     |
| 500  | `LOG_SAVE_FAILED`      | Database gagal menyimpan |
| 503  | `DATABASE_UNAVAILABLE` | Database tidak tersedia  |

---

# 9. Sequence / Alur Detail Fitur AI

## 9.1 Alur Normal

```text
Petugas
   │
   ▼
Web Client
   │
   │ Camera Frame
   ▼
Backend API
   │
   ▼
Input Validation
   │
   ▼
Preprocessing
   │
   ▼
Face Detection
   │
   ├── Tidak ada wajah ──► Response []
   │
   ▼
Face Crop / Region
   │
   ▼
Mask Classification
   │
   ▼
Postprocessing
   │
   ├──────────────► Real-time UI
   │
   └──────────────► Detection Log
                          │
                          ▼
                       Database
```

---

## 9.2 Detail Tahapan

### Step 1 — Validasi Input

Backend memeriksa:

* frame tersedia;
* format input sesuai;
* timestamp tersedia.

Jika input tidak valid, proses dihentikan dan sistem mengembalikan `INVALID_FRAME` atau `INVALID_INPUT`.

### Step 2 — Preprocessing

Frame diproses sebelum masuk model AI.

Proses dapat mencakup:

* decoding frame;
* resize;
* normalisasi;
* penyesuaian format input model.

> [KEPUTUSAN TIM: library dan parameter preprocessing final]

Pilihan:

1. OpenCV preprocessing.
2. TensorFlow/ONNX preprocessing pipeline.

Kriteria:

* kompatibilitas model;
* latency;
* konsistensi preprocessing training dan inference.

### Step 3 — Face Detection

`FaceDetectionModel` menerima frame hasil preprocessing.

Output:

```text
boundingBox
confidence
```

Jika tidak terdapat wajah:

```text
detections = []
```

dan hasil dikembalikan ke frontend tanpa menjalankan mask classification.

### Step 4 — Mask Classification

Setiap wajah yang terdeteksi diproses oleh `MaskClassificationModel`.

Input:

```text
Face Region
```

Output:

```text
mask_status
confidence
```

Target akurasi sistem untuk klasifikasi masker adalah **≥95%**, sedangkan target latency adalah **<1 detik per wajah**.

### Step 5 — Postprocessing

Hasil model diubah menjadi format `DetectionResult`.

Contoh:

```text
Face:
  Bounding Box
  Confidence

Mask:
  MASK / NO_MASK / UNCERTAIN
  Confidence
```

### Step 6 — Response Real-Time

Backend mengirim hasil ke frontend.

Frontend kemudian menampilkan:

* lokasi wajah;
* status masker;
* informasi status deteksi.

### Step 7 — Logging

Hasil klasifikasi yang memenuhi validasi dikirim ke `DetectionLogService`.

Data yang disimpan:

```text
timestamp
mask_status
gender
age_range
```

Tidak terdapat field gambar wajah mentah pada database.

---

# 10. Skenario Timeout dan Kegagalan Model

## 10.1 Face Detection Timeout

```text
Frame
  ↓
Face Detection
  ↓
Timeout
  ↓
Stop current inference
  ↓
Return INFERENCE_TIMEOUT
  ↓
UI menampilkan pesan
  ↓
Sistem tetap aktif
```

Sistem tidak boleh crash ketika satu proses inference mengalami timeout.

---

## 10.2 Mask Classification Failure

Jika face detection berhasil tetapi klasifikasi masker gagal:

```text
Face Detected
     ↓
Mask Classification
     ↓
Failure
     ↓
Return MASK_CLASSIFICATION_FAILED
     ↓
UI menampilkan status sementara
     ↓
Frame berikutnya dapat diproses
```

Sistem tidak menyimpan hasil masker sebagai hasil valid apabila klasifikasi gagal.

---

# 11. Rancangan Error Handling & Fallback

## 11.1 Camera Error

| Kondisi                        | Respons Sistem                | Fallback                             |
| ------------------------------ | ----------------------------- | ------------------------------------ |
| Kamera tidak ditemukan         | Tampilkan pesan               | User memilih kamera lain             |
| Permission ditolak             | Tampilkan instruksi           | User memberikan permission           |
| Kamera terputus                | Tampilkan status disconnected | Coba reconnect                       |
| Kamera gagal start             | Tampilkan error               | Retry start                          |
| Browser tidak mendukung kamera | Tampilkan pesan               | Gunakan browser/perangkat kompatibel |

SRS mensyaratkan bahwa kegagalan kamera harus diinformasikan kepada petugas dan tidak menyebabkan crash. Target pengujiannya adalah **100% kasus kegagalan kamera tertangani**.

---

## 11.2 Retry

Untuk kegagalan sementara:

```text
Failure
   ↓
Check retryable?
   ├── YES → Retry
   │           ↓
   │       Success → Continue
   │           ↓
   │       Failure → Error UI
   │
   └── NO → Error UI
```

> [KEPUTUSAN TIM: jumlah maksimum retry]

Pilihan:

1. Retry otomatis 1–3 kali.
2. Retry hanya berdasarkan tindakan pengguna.

Kriteria:

* latency;
* beban server;
* stabilitas koneksi;
* pengalaman pengguna.

---

# 12. Mode Offline

HLD tidak menetapkan kebutuhan offline penuh. Oleh karena itu:

**[ASUMSI-03]** Mode offline bukan mode operasional utama.

Jika backend/AI tidak tersedia:

```text
Camera
   ↓
Backend unavailable
   ↓
UI menunjukkan:
" layanan deteksi tidak tersedia "
   ↓
Tidak melakukan klasifikasi
```

Sistem tetap menampilkan kondisi error tanpa crash.

Apabila tim menginginkan inference lokal/offline, keputusan tersebut harus ditetapkan sebagai perubahan desain:

**[KEPUTUSAN TIM: Offline inference diperlukan / tidak diperlukan]**

---

# 13. Kontrak Internal Modul AI

## 13.1 Face Detection

### Input

```text
Frame
```

### Output

```json
{
  "faces": [
    {
      "boundingBox": {
        "x": 100,
        "y": 80,
        "width": 120,
        "height": 160
      },
      "confidence": 0.94
    }
  ]
}
```

---

## 13.2 Mask Classification

### Input

```text
Face Region
```

### Output

```json
{
  "status": "MASK",
  "confidence": 0.97
}
```

### [KEPUTUSAN TIM: Model Format]

Pilihan:

1. TensorFlow.
2. ONNX Runtime.

Kriteria:

* latency inference;
* kompatibilitas model;
* kemudahan deployment;
* dukungan hardware.

---

# 14. Rancangan Repository

## `DetectionRepository`

**Layer:** Infrastructure

**Tanggung jawab:**

* Menyimpan `DetectionLog`.
* Mengambil data log jika diperlukan.
* Menyediakan abstraksi database bagi Application Layer.

**Method utama:**

```text
save(detectionLog)
findById(logId)
```

Implementasi database:

```text
PostgreSQLDetectionRepository
```

atau

```text
SQLiteDetectionRepository
```

Pemilihan implementasi:

**[KEPUTUSAN TIM: PostgreSQLDetectionRepository / SQLiteDetectionRepository]**

---

# 15. Security & Privacy

Implementasi wajib mempertahankan batasan privacy dari SRS.

### Data yang boleh disimpan

```text
timestamp
mask_status
gender
age_range
```

### Data yang tidak boleh disimpan permanen

```text
raw face image
```

### Prinsip

```text
Camera Frame
     ↓
AI Processing
     ↓
Detection Result
     ↓
Logging
     ↓
Database

Raw Frame ──X──> Permanent Database
```

NFR-05 menetapkan jumlah gambar wajah mentah yang tersimpan permanen harus **0**, sedangkan NFR-06 mengharuskan data yang dicatat berupa hasil klasifikasi sesuai kebutuhan sistem.

---

# 16. Traceability Desain terhadap Requirement

| Elemen LLD                | FR/NFR              | Implementasi                               |
| ------------------------- | ------------------- | ------------------------------------------ |
| `CameraSessionService`    | FR-01, FR-08        | Mengelola kamera dan kondisi kegagalan     |
| `FaceDetectionModel`      | FR-01               | Mendeteksi wajah                           |
| `MaskClassificationModel` | FR-02               | Mengklasifikasikan status masker           |
| `DetectionPipeline`       | FR-01, FR-02, FR-05 | Mengatur pipeline AI                       |
| `DetectionResult`         | FR-05               | Struktur hasil deteksi                     |
| `DetectionLogService`     | FR-06               | Mengelola penyimpanan hasil                |
| `DetectionRepository`     | FR-06               | Menyimpan log ke database                  |
| `DetectionController`     | FR-05, FR-06        | Menghubungkan API dengan application layer |
| `CameraController`        | FR-08               | Mengirim status kamera ke UI               |
| Error Handler             | FR-08, NFR-04       | Menangani kamera gagal tanpa crash         |
| AI Pipeline               | NFR-01              | Mendukung target akurasi masker ≥95%       |
| AI Pipeline               | NFR-02              | Mendukung target latency <1 detik/wajah    |
| `detection_logs`          | NFR-05              | Tidak menyimpan raw image                  |
| `DetectionLogService`     | NFR-06              | Hanya menyimpan hasil klasifikasi          |

---

# 17. Ringkasan Arsitektur LLD

```text
┌───────────────────────────────────────────┐
│              PRESENTATION                 │
│                                           │
│ React / Next.js                           │
│ CameraController                          │
│ DetectionController                       │
└───────────────────┬───────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│               APPLICATION                 │
│                                           │
│ CameraSessionService                      │
│ DetectionPipeline                         │
│ DetectionLogService                       │
└───────────────────┬───────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│                 DOMAIN                    │
│                                           │
│ FaceDetection                             │
│ MaskClassification                        │
│ DetectionResult                           │
│ DetectionLog                              │
└───────────────────┬───────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│             INFRASTRUCTURE                │
│                                           │
│ CameraAdapter                             │
│ FaceDetectionModel                        │
│ MaskClassificationModel                   │
│ DetectionRepository                       │
│ OpenCV + TensorFlow / ONNX                │
│ PostgreSQL / SQLite                       │
└───────────────────────────────────────────┘
```

### Alur utama

```text
Camera
  ↓
CameraSessionService
  ↓
DetectionPipeline
  ↓
Face Detection
  ↓
Mask Classification
  ↓
DetectionResult
  ├──────────→ Real-time UI
  │
  └──────────→ DetectionLogService
                    ↓
              DetectionRepository
                    ↓
                 Database
```

Dengan desain ini, LLD tetap berada pada level implementasi teknis tanpa masuk ke kode konkret, query SQL, atau detail konfigurasi deployment. Requirement inti yang direalisasikan adalah **FR-01, FR-02, FR-05, FR-06, dan FR-08**, dengan target kualitas utama **akurasi masker ≥95%, latency <1 detik/wajah, penanganan kegagalan kamera 100%, dan 0 penyimpanan permanen raw face image**.
