# DRAF USER STORIES

## Sistem Pemantau Kepatuhan Masker Berbasis AI

User story berikut hanya diturunkan dari fitur **Must Have** dan **Should Have** pada SRS. Setiap story memiliki keterlacakan langsung ke minimal satu Functional Requirement.

---

## Epik 1 — Deteksi Wajah dan Kepatuhan Masker

### US-01 — Deteksi Wajah

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** sistem mendeteksi wajah dari kamera secara real-time,
**Sehingga** saya dapat memantau pengunjung secara otomatis tanpa melakukan pemeriksaan satu per satu.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-01, NFR-02

### US-02 — Klasifikasi Status Masker

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** sistem mengklasifikasikan apakah wajah terdeteksi menggunakan atau tidak menggunakan masker,
**Sehingga** saya dapat mengetahui kepatuhan penggunaan masker secara cepat.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-02, NFR-01, NFR-02

### US-03 — Hasil Deteksi Real-Time

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** melihat hasil deteksi secara real-time,
**Sehingga** saya dapat segera mengetahui status masker pengunjung.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-05, NFR-02, NFR-03

---

# Epik 2 — Prediksi Demografis Pengunjung

### US-04 — Prediksi Jenis Kelamin

**Sebagai** manajemen gedung,
**Saya ingin** sistem menghasilkan klasifikasi jenis kelamin dari wajah yang terdeteksi,
**Sehingga** saya dapat memperoleh data demografis agregat untuk kebutuhan analisis.

* **Prioritas:** Should Have
* **Keterlacakan:** FR-03, NFR-02

### US-05 — Estimasi Rentang Usia

**Sebagai** manajemen gedung,
**Saya ingin** sistem menghasilkan estimasi rentang usia dari wajah yang terdeteksi,
**Sehingga** saya dapat memperoleh informasi demografis agregat untuk kebutuhan analisis.

* **Prioritas:** Should Have
* **Keterlacakan:** FR-04, NFR-02

> Catatan: hasil jenis kelamin dan usia merupakan **klasifikasi/estimasi**, bukan identitas individu, sesuai BR-04.

---

# Epik 3 — Pencatatan Hasil Deteksi

### US-06 — Pencatatan Otomatis

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** hasil deteksi dicatat secara otomatis,
**Sehingga** saya tidak perlu melakukan pencatatan pengunjung secara manual.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-06, NFR-06

### US-07 — Data Log Deteksi

**Sebagai** manajemen gedung,
**Saya ingin** log deteksi menyimpan timestamp, status masker, jenis kelamin, dan estimasi rentang usia,
**Sehingga** saya dapat menggunakan data tersebut untuk pemantauan dan pelaporan agregat.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-06, NFR-05, NFR-06

---

# Epik 4 — Informasi Agregat

### US-08 — Ringkasan Data Deteksi

**Sebagai** manajemen gedung,
**Saya ingin** melihat ringkasan data hasil deteksi dan data demografis,
**Sehingga** saya dapat mengetahui kondisi kepatuhan masker dan karakteristik demografis pengunjung secara agregat.

* **Prioritas:** Should Have
* **Keterlacakan:** FR-07, NFR-03

---

# Epik 5 — Penanganan Kegagalan Kamera

### US-09 — Informasi Kamera Gagal

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** sistem memberikan pesan ketika kamera gagal diakses,
**Sehingga** saya mengetahui bahwa proses pemantauan tidak dapat dilakukan melalui kamera.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-08, NFR-04

### US-10 — Sistem Tetap Stabil Saat Kamera Gagal

**Sebagai** petugas keamanan/resepsionis,
**Saya ingin** sistem tidak mengalami crash ketika kamera gagal diakses,
**Sehingga** saya dapat mengetahui masalah kamera melalui informasi kesalahan yang diberikan sistem.

* **Prioritas:** Must Have
* **Keterlacakan:** FR-08, NFR-04

---

# Ringkasan Backlog User Stories

| ID        | Epik                   | User Story                | Prioritas | Traceability          |
| --------- | ---------------------- | ------------------------- | --------- | --------------------- |
| **US-01** | Deteksi Wajah & Masker | Deteksi wajah real-time   | Must      | FR-01, NFR-02         |
| **US-02** | Deteksi Wajah & Masker | Klasifikasi status masker | Must      | FR-02, NFR-01, NFR-02 |
| **US-03** | Deteksi Wajah & Masker | Melihat hasil real-time   | Must      | FR-05, NFR-02, NFR-03 |
| **US-04** | Demografis             | Prediksi jenis kelamin    | Should    | FR-03, NFR-02         |
| **US-05** | Demografis             | Estimasi rentang usia     | Should    | FR-04, NFR-02         |
| **US-06** | Pencatatan             | Pencatatan otomatis       | Must      | FR-06, NFR-06         |
| **US-07** | Pencatatan             | Penyimpanan data log      | Must      | FR-06, NFR-05, NFR-06 |
| **US-08** | Agregasi               | Ringkasan data deteksi    | Should    | FR-07, NFR-03         |
| **US-09** | Kamera                 | Pesan kamera gagal        | Must      | FR-08, NFR-04         |
| **US-10** | Kamera                 | Stabil saat kamera gagal  | Must      | FR-08, NFR-04         |

### Catatan Scope

**FR-09 (filter laporan)** dan **FR-10 (visualisasi statistik)** tidak dibuat menjadi user story karena keduanya berstatus **Could Have**, sesuai aturan tugas.

Dengan demikian, backlog inti terdiri dari **10 user stories** yang mencakup seluruh FR **Must Have dan Should Have** dari SRS tanpa menambahkan kebutuhan baru.
