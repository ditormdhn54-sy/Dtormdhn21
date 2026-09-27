# API Contract — Sistem Pemantau Kepatuhan Masker Berbasis AI

## 1. Ringkasan

Dokumen ini menjelaskan keputusan desain di balik `openapi.yaml`, hasil turunan dari LLD (PTM-04) dan User Story Must Have (PTM-03). API ini melayani dua kelompok pengguna: **petugas keamanan** (real-time monitoring) dan **manajemen gedung** (logging & pelaporan).

## 2. Mengapa 3 Endpoint Ini

| Endpoint | FR Terkait | Alasan |
|---|---|---|
| `POST /api/camera-sessions` | FR-01, FR-08 | Memisahkan siklus hidup sesi kamera (mulai/berhenti/status) dari proses deteksi, agar frontend bisa menangani status kamera (aktif/gagal) secara independen dari hasil AI |
| `POST /api/detections` | FR-01, FR-02, FR-05 | Endpoint inti pipeline AI — menerima frame, mengembalikan hasil deteksi wajah + status masker secara real-time |
| `POST /api/detection-logs` | FR-06 | Dipisahkan dari `/api/detections` agar frontend punya kendali eksplisit kapan hasil disimpan sebagai log permanen (bukan setiap frame otomatis tersimpan) |

Tidak ditambahkan endpoint di luar tiga ini karena FR Must Have pada SRS hanya mencakup deteksi, klasifikasi, penyajian real-time, pencatatan, dan penanganan kegagalan kamera — bukan fitur agregasi/laporan (itu scope Should Have).

## 3. Penamaan Resource

Path menggunakan noun jamak sesuai konvensi REST (`/api/camera-sessions`, `/api/detections`, `/api/detection-logs`), direvisi dari draf awal AI yang masih singular (`/api/camera/start`, `/api/detection`, `/api/detection/log`).

## 4. Kenapa `gender` dan `age_range` Nullable

Berdasarkan SRS, prediksi jenis kelamin dan estimasi usia adalah fitur **Should Have**, bukan Must Have. Field ini tetap disediakan di skema data (`DetectionResult`, `DetectionLog`) agar struktur data sudah siap saat fitur tersebut diaktifkan di iterasi berikutnya, tapi bernilai `null` selama implementasi Must Have berjalan.

## 5. Kenapa Tidak Menyimpan Raw Image

NFR-05 dan NFR-06 pada SRS mensyaratkan privasi by design: jumlah gambar wajah mentah yang tersimpan permanen harus 0. Oleh karena itu:
- `DetectionRequest` menerima frame hanya untuk diproses sesaat (in-memory), tidak pernah disimpan ke database
- `DetectionLog` dan `DetectionLogCreate` hanya menyimpan hasil klasifikasi (`mask_status`, `gender`, `age_range`, `timestamp`) — tidak ada field gambar

## 6. Autentikasi (Asumsi)

LLD (PTM-04) belum menetapkan mekanisme autentikasi secara eksplisit. Skema `bearerAuth` (JWT) ditambahkan sebagai asumsi placeholder pada seluruh endpoint, karena aplikasi ini ditujukan untuk petugas keamanan internal gedung (bukan publik), sehingga proteksi akses dianggap kebutuhan dasar meski belum dirinci detailnya oleh tim.

## 7. Error Handling & Kode Status

Setiap endpoint menyediakan minimal 3 kode respons (sukses + 4xx + 5xx), mengikuti skenario kegagalan yang sudah dipetakan di LLD:
- Kegagalan input (400, 422) — frame/data tidak valid
- Kegagalan proses AI (408 timeout, 500 face/mask pipeline gagal, 503 layanan AI tidak tersedia)
- Kegagalan penyimpanan (500 gagal simpan, 503 database tidak tersedia)

Prinsip: sistem tidak boleh crash pada kegagalan apa pun — selalu mengembalikan kode error terstruktur (`ErrorResponse`) agar frontend bisa menampilkan pesan yang ramah pengguna.

## 8. Daftar Asumsi (dari Prompt D.1 & D.2)

| Kode | Asumsi | Status Verifikasi Tim |
|---|---|---|
| ASUMSI-01 | Autentikasi bearer token (JWT) untuk endpoint yang membutuhkan proteksi | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-02 | `session_id` dari `/api/camera-sessions` dipakai untuk mengaitkan request deteksi berikutnya | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-03 | Frame dikirim sebagai `multipart/form-data`, bukan base64 | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-04 | `camera_id` opsional; sistem pakai kamera default jika kosong | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-05 | `session_id` wajib disertakan di setiap request deteksi | [KEPUTUSAN TIM: perlu diisi] |
| ASUMSI-06 | Field `timestamp` di request deteksi bersifat opsional (metadata tambahan) | [KEPUTUSAN TIM: perlu diisi] |

> Isi kolom "Status Verifikasi Tim" dengan Benar/Diubah/Dihapus sebelum submit — ini juga wajib direfleksikan di Bagian E.3 Lembar Kerja.
