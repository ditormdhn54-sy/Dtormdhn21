# DRAF PRD — Sistem Pemantau Kepatuhan Masker Berbasis AI

## 1. Ringkasan Eksekutif

**Sistem Pemantau Kepatuhan Masker Berbasis AI** adalah produk berbasis website yang membantu petugas keamanan atau resepsionis gedung publik memantau kepatuhan penggunaan masker secara real-time melalui kamera.

Produk berfokus pada tiga kemampuan AI utama: **deteksi wajah, klasifikasi status masker, serta prediksi jenis kelamin dan estimasi rentang usia**. Hasil deteksi ditampilkan secara langsung pada dashboard dan dicatat sebagai data klasifikasi untuk kebutuhan pemantauan dan pelaporan agregat.

Target utama adalah **Pak Andi**, petugas keamanan yang menangani ratusan pengunjung per hari dan mengalami kesulitan melakukan pemeriksaan serta pencatatan secara manual.

Berdasarkan bukti riset yang diberikan, model CNN berbasis MobileNet mencapai akurasi deteksi masker **99%**, sementara prediksi jenis kelamin dan usia mencapai akurasi **98,75%**, dengan sensitivity **98,5%** dan specificity **99%**. Implementasi real-time menggunakan OpenCV juga dilaporkan memiliki latensi rendah dan responsivitas yang baik (Sopian, Setiadi, & Agustino, 2024, DOI: 10.37012/jtik.v10i2.2395).

---

## 2. Problem Statement & Bukti

### Problem Statement

Kepatuhan penggunaan masker di tempat umum masih perlu dipantau. Verifikasi secara manual oleh petugas keamanan memiliki beberapa masalah:

* Lambat ketika jumlah pengunjung tinggi.
* Tidak konsisten karena bergantung pada petugas.
* Menguras tenaga petugas.
* Pencatatan kepatuhan dan demografis secara manual tidak efisien.

### Fakta vs Asumsi

| Jenis         | Pernyataan                                                                                                             |
| ------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **FAKTA**     | Petugas keamanan perlu memantau kepatuhan penggunaan masker di tempat umum.                                            |
| **FAKTA**     | Verifikasi manual dinyatakan lambat, tidak konsisten, dan menguras tenaga.                                             |
| **FAKTA**     | Target user menghadapi ratusan pengunjung setiap hari.                                                                 |
| **FAKTA**     | Riset yang diberikan melaporkan akurasi deteksi masker 99%.                                                            |
| **FAKTA**     | Riset melaporkan akurasi prediksi jenis kelamin dan usia 98,75%.                                                       |
| **FAKTA**     | Riset melaporkan sensitivity 98,5% dan specificity 99%.                                                                |
| **FAKTA**     | Implementasi real-time menggunakan OpenCV dilaporkan memiliki latensi rendah dan responsivitas baik.                   |
| **ASUMSI-01** | Dashboard dapat digunakan oleh petugas dengan perangkat yang memiliki kamera.                                          |
| **ASUMSI-02** | Data hasil klasifikasi cukup untuk kebutuhan pelaporan manajemen tanpa menyimpan gambar wajah mentah.                  |
| **ASUMSI-03** | Rentang usia yang digunakan dapat ditentukan sesuai kebutuhan prototype karena konteks tidak menetapkan kategori usia. |
| **ASUMSI-04** | Target penggunaan prototype adalah lokasi dengan akses kamera yang memadai.                                            |

---

## 3. Target User & Stakeholder

| Peran                                       | Kebutuhan                                                                                                  | Pengaruh                                      |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Petugas keamanan/resepsionis (Pak Andi)** | Deteksi cepat, dashboard sederhana, informasi status masker secara real-time, tanpa kontak fisik           | **Tinggi** — pengguna utama                   |
| **Manajemen gedung**                        | Data agregat kepatuhan dan demografis untuk pelaporan dan analisis                                         | **Tinggi** — menentukan nilai bisnis produk   |
| **Pengunjung**                              | [ASUMSI-05] Pemantauan yang tidak memerlukan kontak fisik dan tidak menyimpan gambar wajah secara permanen | **Sedang** — pihak yang terdampak oleh sistem |

---

## 4. Value Proposition

### Pain yang Dikurangi

1. Mengurangi kebutuhan petugas untuk memeriksa pengunjung satu per satu.
2. Mengurangi pencatatan manual.
3. Mengurangi beban petugas ketika lalu lintas pengunjung tinggi.
4. Mengurangi ketidakkonsistenan proses pemantauan manual.

### Gain yang Diciptakan

1. **Pemantauan real-time** terhadap status masker.
2. **Respons lebih cepat** terhadap pengunjung yang tidak menggunakan masker.
3. **Pencatatan otomatis** timestamp, status masker, dan data demografis hasil klasifikasi.
4. **Data agregat** yang dapat digunakan manajemen untuk pelaporan.
5. Penggunaan tanpa kontak fisik.

### Mengapa AI Bukan Gimmick?

AI memiliki fungsi inti dalam produk karena sistem harus **menginterpretasikan informasi visual dari wajah secara otomatis** dan mengklasifikasikannya menjadi status masker, jenis kelamin, serta estimasi usia.

Tanpa kemampuan computer vision, sistem tidak dapat menjalankan fungsi utama pemantauan otomatis. Selain itu, bukti riset yang diberikan menunjukkan performa model yang tinggi serta kemampuan implementasi real-time.

---

# 5. Tujuan Produk & KPI Terukur

| Tujuan                                    | KPI                                             |                                               Target | Cara Mengukur                                                        |
| ----------------------------------------- | ----------------------------------------------- | ---------------------------------------------------: | -------------------------------------------------------------------- |
| Mendeteksi kepatuhan masker secara akurat | Akurasi deteksi masker                          |                                             **≥95%** | Pengujian hasil prediksi model terhadap data berlabel                |
| Memberikan respons real-time              | Latensi deteksi & prediksi                      |                                   **<1 detik/wajah** | Mengukur waktu dari wajah terdeteksi hingga hasil klasifikasi muncul |
| Membantu petugas melakukan pemantauan     | Waktu penggunaan dashboard                      | [ASUMSI-06] ≤5 menit untuk memahami penggunaan dasar | Uji usability terhadap pengguna target                               |
| Mengurangi pencatatan manual              | Persentase hasil deteksi yang tercatat otomatis |                                     [ASUMSI-07] ≥95% | Membandingkan deteksi yang terjadi dengan log yang tersimpan         |
| Menjaga privasi                           | Gambar wajah mentah tersimpan permanen          |                                                **0** | Audit penyimpanan data setelah proses deteksi                        |
| Menjaga stabilitas penggunaan             | Sistem tidak crash ketika kamera gagal diakses  |               **100% kasus menampilkan pesan error** | Pengujian skenario kegagalan akses kamera                            |

---

# 6. Scope Fitur 3 Bulan — MoSCoW

| Prioritas       | Fitur                             | Deskripsi                                                                          |
| --------------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| **Must Have**   | ★ FR-01 Deteksi wajah             | Mendeteksi wajah dari live feed kamera secara real-time                            |
| **Must Have**   | ★ FR-02 Deteksi status masker     | Mengklasifikasikan wajah menjadi menggunakan atau tidak menggunakan masker         |
| **Must Have**   | ★ FR-05 Dashboard real-time       | Menampilkan hasil deteksi secara langsung kepada petugas                           |
| **Must Have**   | FR-06 Log deteksi                 | Menyimpan timestamp, status masker, dan hasil demografis                           |
| **Must Have**   | Error kamera                      | Menampilkan pesan yang jelas ketika kamera gagal diakses                           |
| **Should Have** | ★ FR-03 Prediksi jenis kelamin    | Memberikan hasil klasifikasi jenis kelamin dari wajah terdeteksi                   |
| **Should Have** | ★ FR-04 Estimasi usia             | Memberikan estimasi dalam bentuk rentang usia                                      |
| **Should Have** | Ringkasan data                    | [ASUMSI-08] Menampilkan ringkasan agregat kepatuhan dan demografis untuk manajemen |
| **Could Have**  | Filter laporan                    | [ASUMSI-09] Filter data berdasarkan periode waktu                                  |
| **Could Have**  | Visualisasi statistik             | [ASUMSI-10] Grafik sederhana mengenai tingkat kepatuhan                            |
| **Won't Have**  | Penyimpanan gambar wajah permanen | Tidak termasuk karena bertentangan dengan kebutuhan privasi                        |
| **Won't Have**  | Identifikasi identitas individu   | Tidak termasuk dalam kebutuhan produk                                              |
| **Won't Have**  | Sistem penegakan/sanksi otomatis  | Sistem hanya melakukan pemantauan dan pencatatan                                   |

> **Catatan:** ★ menandai fitur yang menggunakan AI.

---

# 7. Non-Goals

Untuk menjaga prototype tetap realistis dalam batas waktu **1 semester**, produk **tidak mencakup**:

1. Identifikasi nama atau identitas spesifik pengunjung.
2. Penyimpanan permanen gambar wajah mentah.
3. Pemberian sanksi atau tindakan otomatis kepada pengunjung.
4. Sistem keamanan gedung secara keseluruhan.
5. Fungsi pengenalan wajah untuk mencari individu tertentu.
6. Fitur di luar pemantauan masker dan data demografis yang disebutkan dalam konteks.
7. Pengembangan produk berskala penuh untuk seluruh gedung/instansi di luar kebutuhan prototype.

---

# 8. Asumsi & Risiko Utama + Mitigasi

| Asumsi/Risiko                                                        | Dampak                                    | Mitigasi                                                                           |
| -------------------------------------------------------------------- | ----------------------------------------- | ---------------------------------------------------------------------------------- |
| **ASUMSI-01:** Perangkat memiliki kamera yang memadai                | Deteksi tidak dapat berjalan              | Uji penggunaan dengan perangkat yang tersedia sebelum implementasi                 |
| **ASUMSI-03:** Kategori rentang usia belum ditentukan                | Hasil usia tidak seragam                  | Menentukan kategori rentang usia sebelum tahap pengujian                           |
| **ASUMSI-07:** Sebagian hasil deteksi mungkin gagal tercatat         | Data laporan tidak lengkap                | Melakukan pengujian pencatatan dan menangani kegagalan dengan pesan yang jelas     |
| **Risiko:** Kondisi wajah/kamera dapat memengaruhi hasil deteksi     | Akurasi menurun                           | Melakukan pengujian pada kondisi penggunaan yang relevan                           |
| **Risiko:** Akurasi aktual prototype berbeda dengan hasil penelitian | KPI tidak tercapai                        | Melakukan evaluasi menggunakan data pengujian sendiri                              |
| **Risiko:** Prediksi demografis dapat menghasilkan kesalahan         | Data analisis kurang akurat               | Menampilkan hasil sebagai **estimasi/klasifikasi**, bukan fakta identitas individu |
| **Risiko:** Privasi pengunjung                                       | Potensi masalah privasi                   | Tidak menyimpan gambar wajah mentah secara permanen                                |
| **Risiko:** Kamera gagal diakses                                     | Pemantauan terhenti                       | Menampilkan pesan error yang jelas dan mencegah sistem crash                       |
| **Keterbatasan:** Data dan biaya AI terbatas                         | Pengembangan model/fitur menjadi terbatas | Memprioritaskan fitur **Must Have** untuk prototype 3 bulan                        |

### Prioritas MVP

Jika waktu pengembangan semakin terbatas, urutan prioritas MVP adalah:

**Deteksi wajah → Deteksi masker ★ → Dashboard real-time → Log deteksi → Estimasi demografis ★ → Laporan agregat.**

Dengan demikian, **deteksi kepatuhan masker tetap menjadi fungsi AI utama**, sedangkan prediksi jenis kelamin dan usia menjadi fitur pendukung untuk kebutuhan analisis manajemen.
