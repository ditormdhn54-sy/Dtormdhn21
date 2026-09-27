# DRAF SRS Ringkas

## Sistem Pemantau Kepatuhan Masker Berbasis AI

---

## 1. Tujuan, Scope, dan Definisi Istilah

### 1.1 Tujuan

Sistem bertujuan menyediakan pemantauan kepatuhan penggunaan masker secara real-time melalui kamera sehingga petugas keamanan/resepsionis dapat melakukan verifikasi secara lebih cepat dibandingkan pemeriksaan manual.

Sistem juga menghasilkan klasifikasi jenis kelamin dan estimasi rentang usia untuk mendukung kebutuhan data agregat manajemen gedung.

### 1.2 Scope Sistem

**Dalam scope:**

* Deteksi wajah dari live feed kamera.
* Klasifikasi status penggunaan masker.
* Prediksi jenis kelamin.
* Estimasi rentang usia.
* Penyajian hasil deteksi secara real-time.
* Pencatatan hasil deteksi.
* Ringkasan data agregat.
* Penanganan kegagalan akses kamera.

**Di luar scope:**

* Identifikasi nama/identitas individu.
* Pengenalan wajah individu.
* Penyimpanan permanen gambar wajah mentah.
* Pemberian sanksi otomatis.
* Sistem keamanan gedung secara keseluruhan.

### 1.3 Definisi Istilah

| Istilah             | Definisi                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------- |
| **AI**              | Kemampuan sistem melakukan klasifikasi/prediksi berdasarkan data visual.                 |
| **Computer Vision** | Pemrosesan informasi visual dari kamera untuk memperoleh hasil deteksi atau klasifikasi. |
| **Deteksi wajah**   | Proses menemukan wajah pada input kamera.                                                |
| **Status masker**   | Klasifikasi apakah wajah menggunakan atau tidak menggunakan masker.                      |
| **Jenis kelamin**   | Hasil klasifikasi jenis kelamin dari wajah terdeteksi.                                   |
| **Estimasi usia**   | Perkiraan usia dalam bentuk rentang usia.                                                |
| **Live feed**       | Input gambar/video yang diperoleh secara langsung dari kamera.                           |
| **Log deteksi**     | Catatan hasil deteksi yang mencakup timestamp, status masker, dan data demografis.       |

---

# 2. User, Stakeholder, Lingkungan Operasi, Asumsi & Dependensi

### 2.1 User dan Stakeholder

| Aktor                        | Peran           | Kebutuhan                                                                 |
| ---------------------------- | --------------- | ------------------------------------------------------------------------- |
| Petugas keamanan/resepsionis | Pengguna utama  | Memantau status masker secara cepat dan real-time                         |
| Manajemen gedung             | Pengguna data   | Memperoleh data agregat kepatuhan dan demografis                          |
| Pengunjung                   | Pihak terdampak | Pemantauan tanpa kontak fisik dan tanpa penyimpanan permanen gambar wajah |

### 2.2 Lingkungan Operasi

Sistem digunakan pada:

* Platform **website**.
* Lokasi publik seperti gedung perkantoran, mall, atau fasilitas kesehatan.
* Lingkungan dengan akses kamera.
* Kondisi lalu lintas pengunjung yang dapat mencapai ratusan orang per hari.

Detail perangkat keras, jaringan, sistem operasi, dan spesifikasi infrastruktur **belum ditentukan dalam PRD** sehingga tidak menjadi kebutuhan SRS.

### 2.3 Asumsi

| ID    | Asumsi                                                                             |
| ----- | ---------------------------------------------------------------------------------- |
| AS-01 | Perangkat yang digunakan memiliki akses kamera.                                    |
| AS-02 | Kondisi kamera memungkinkan wajah terdeteksi.                                      |
| AS-03 | Data klasifikasi dapat memenuhi kebutuhan pelaporan tanpa menyimpan gambar mentah. |
| AS-04 | Rentang usia dapat ditentukan untuk kebutuhan prototype.                           |
| AS-05 | Pemantauan dilakukan tanpa kontak fisik.                                           |

### 2.4 Dependensi

| ID     | Dependensi                                                                                                                             |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| DEP-01 | Sistem bergantung pada ketersediaan akses kamera untuk melakukan deteksi real-time.                                                    |
| DEP-02 | Kemampuan AI bergantung pada model CNN berbasis MobileNet sebagaimana digunakan dalam bukti riset.                                     |
| DEP-03 | Pengukuran kualitas AI bergantung pada data pengujian yang dapat digunakan untuk membandingkan hasil prediksi dengan label yang benar. |

---

# 3. Functional Requirements

**Prioritas:** Must = wajib, Should = penting tetapi dapat menyusul, Could = tambahan.

| ID        | Requirement                                                                                                                                                                | Prioritas  | Metode Verifikasi            |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------------------------- |
| **FR-01** | Sistem harus dapat **mendeteksi wajah dari live feed kamera saat kamera tersedia** → menghasilkan lokasi/hasil wajah terdeteksi untuk proses klasifikasi berikutnya.       | **Must**   | Pengujian                    |
| **FR-02** | Sistem harus dapat **mengklasifikasikan status penggunaan masker pada wajah terdeteksi saat wajah berhasil dideteksi** → menghasilkan status **pakai/tidak pakai masker**. | **Must**   | Pengujian akurasi            |
| **FR-03** | Sistem harus dapat **memprediksi jenis kelamin dari wajah terdeteksi saat wajah berhasil dideteksi** → menghasilkan hasil klasifikasi jenis kelamin.                       | **Should** | Pengujian akurasi            |
| **FR-04** | Sistem harus dapat **mengestimasi rentang usia dari wajah terdeteksi saat wajah berhasil dideteksi** → menghasilkan estimasi rentang usia.                                 | **Should** | Pengujian akurasi            |
| **FR-05** | Sistem harus dapat **menampilkan hasil deteksi secara real-time saat proses deteksi berlangsung** → petugas memperoleh informasi hasil klasifikasi.                        | **Must**   | Pengujian fungsional         |
| **FR-06** | Sistem harus dapat **menyimpan log hasil deteksi saat hasil klasifikasi diperoleh** → tersimpan timestamp, status masker, dan data demografis.                             | **Must**   | Pengujian database/log       |
| **FR-07** | Sistem harus dapat **menampilkan ringkasan data deteksi saat data hasil klasifikasi tersedia** → menghasilkan data agregat kepatuhan dan demografis.                       | **Should** | Pengujian fungsional         |
| **FR-08** | Sistem harus dapat **menampilkan pesan kesalahan saat akses kamera gagal** → petugas mengetahui bahwa kamera tidak dapat digunakan.                                        | **Must**   | Pengujian skenario kegagalan |
| **FR-09** | Sistem dapat **memfilter data hasil deteksi berdasarkan periode saat fitur laporan digunakan** → menghasilkan data sesuai periode yang dipilih.                            | **Could**  | Pengujian fungsional         |
| **FR-10** | Sistem dapat **menampilkan visualisasi statistik saat data agregat tersedia** → menghasilkan representasi statistik kepatuhan.                                             | **Could**  | Pengujian fungsional         |

> FR-09 dan FR-10 berasal dari fitur **Could Have** pada PRD sehingga bukan persyaratan inti prototype.

---

# 4. Non-Functional Requirements

Acuan kualitas: **ISO/IEC 25010**.

| ID         | Kategori ISO/IEC 25010 | Requirement                                                                                                          | Metrik                                             | Target                    | Kondisi Ukur                                                    |
| ---------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------- | --------------------------------------------------------------- |
| **NFR-01** | Performance efficiency | Sistem harus menghasilkan klasifikasi status masker dengan tingkat akurasi yang memenuhi target.                     | Accuracy                                           | **≥95%**                  | Pengujian menggunakan data berlabel                             |
| **NFR-02** | Performance efficiency | Sistem harus menghasilkan deteksi dan prediksi dalam waktu yang ditetapkan.                                          | Latensi per wajah                                  | **<1 detik/wajah**        | Diukur sejak wajah terdeteksi hingga hasil klasifikasi tersedia |
| **NFR-03** | Usability              | Sistem harus dapat dipahami oleh petugas tanpa pelatihan khusus.                                                     | Waktu pemahaman penggunaan                         | **≤5 menit**              | Uji penggunaan oleh target user                                 |
| **NFR-04** | Reliability            | Sistem harus memberikan informasi ketika kamera tidak dapat diakses dan tidak mengalami crash pada kondisi tersebut. | Keberhasilan penanganan error                      | **100% kasus pengujian**  | Pengujian dengan skenario kamera gagal                          |
| **NFR-05** | Security/Privacy       | Sistem tidak boleh menyimpan gambar wajah mentah secara permanen.                                                    | Jumlah gambar wajah mentah yang tersimpan permanen | **0**                     | Pemeriksaan data setelah proses deteksi                         |
| **NFR-06** | Privacy                | Data yang dicatat harus berupa hasil klasifikasi sesuai kebutuhan sistem, bukan gambar wajah mentah.                 | Kepatuhan jenis data tersimpan                     | **100% sesuai ketentuan** | Audit terhadap log hasil deteksi                                |

**Catatan:** PRD tidak memberikan target kuantitatif tambahan untuk keamanan selain kebutuhan privasi, sehingga SRS tidak menetapkan target keamanan teknis lain.

---

# 5. Kebutuhan Data Minimum Fitur AI

| Fitur AI                 | Input            | Output Model                                  |
| ------------------------ | ---------------- | --------------------------------------------- |
| ★ Deteksi wajah          | Live feed kamera | Wajah terdeteksi                              |
| ★ Klasifikasi masker     | Wajah terdeteksi | Status: **pakai masker / tidak pakai masker** |
| ★ Prediksi jenis kelamin | Wajah terdeteksi | Hasil klasifikasi jenis kelamin               |
| ★ Estimasi usia          | Wajah terdeteksi | Estimasi **rentang usia**                     |

### Data yang Dicatat

Berdasarkan FR-06, sistem mencatat minimum:

* **Timestamp**
* **Status masker**
* **Jenis kelamin**
* **Estimasi rentang usia**

**Gambar wajah mentah tidak disimpan permanen.**

---

# 6. Aturan Bisnis Hasil Riset

### BR-01 — Kriteria Kepatuhan Masker

Hasil klasifikasi status masker menjadi dasar sistem untuk menentukan apakah wajah yang terdeteksi **menggunakan atau tidak menggunakan masker**.

### BR-02 — Target Akurasi

Hasil deteksi masker pada prototype harus mencapai akurasi minimal **95%**, sesuai KPI dan NFR.

### BR-03 — Target Latensi

Proses deteksi dan prediksi harus menghasilkan respons kurang dari **1 detik per wajah**.

### BR-04 — Hasil Demografis

Jenis kelamin dan usia digunakan sebagai **hasil klasifikasi/estimasi untuk kebutuhan analisis**, bukan sebagai identitas individu.

### BR-05 — Privasi Data

Gambar wajah mentah **tidak disimpan secara permanen**. Data yang dipertahankan berupa hasil klasifikasi yang dibutuhkan untuk pemantauan dan pelaporan.

### BR-06 — Bukti Performa Penelitian

Riset Sopian, Setiadi, & Agustino (2024) yang dicantumkan dalam PRD melaporkan:

* Akurasi deteksi masker: **99%**
* Akurasi prediksi jenis kelamin dan usia: **98,75%**
* Sensitivity: **98,5%**
* Specificity: **99%**
* Implementasi real-time dilaporkan memiliki latensi rendah dan responsivitas baik.

Nilai tersebut merupakan **bukti riset/acuan**, bukan jaminan bahwa prototype akan memperoleh performa identik. Performa prototype tetap harus diverifikasi melalui pengujian.

---

# 7. Matriks Traceability

| Requirement SRS | Fitur/Elemen PRD Terkait                 | Sumber          |
| --------------- | ---------------------------------------- | --------------- |
| **FR-01**       | ★ FR-01 Deteksi wajah                    | PRD Scope       |
| **FR-02**       | ★ FR-02 Deteksi status masker            | PRD Scope       |
| **FR-03**       | ★ FR-03 Prediksi jenis kelamin           | PRD Scope       |
| **FR-04**       | ★ FR-04 Estimasi usia                    | PRD Scope       |
| **FR-05**       | ★ FR-05 Dashboard real-time              | PRD Scope       |
| **FR-06**       | FR-06 Log deteksi                        | PRD Scope       |
| **FR-07**       | Ringkasan data                           | PRD Should Have |
| **FR-08**       | Error kamera                             | PRD Must Have   |
| **FR-09**       | Filter laporan                           | PRD Could Have  |
| **FR-10**       | Visualisasi statistik                    | PRD Could Have  |
| **NFR-01**      | KPI akurasi deteksi masker ≥95%          | PRD KPI         |
| **NFR-02**      | KPI latensi <1 detik/wajah               | PRD KPI         |
| **NFR-03**      | Usability ≤5 menit                       | PRD KPI/NFR     |
| **NFR-04**      | Error handling 100%                      | PRD KPI/NFR     |
| **NFR-05**      | 0 gambar wajah mentah tersimpan permanen | PRD KPI/NFR     |
| **NFR-06**      | Privasi data hasil klasifikasi           | PRD NFR-03      |
| **BR-01**       | Status masker pakai/tidak                | FR-02           |
| **BR-02**       | Akurasi ≥95%                             | NFR-01          |
| **BR-03**       | Latensi <1 detik                         | NFR-02          |
| **BR-04**       | Data jenis kelamin & usia                | FR-03, FR-04    |
| **BR-05**       | Tidak menyimpan gambar wajah mentah      | NFR-05/NFR-06   |
| **BR-06**       | Hasil riset MobileNet/CNN                | Bukti riset PRD |

### Kesimpulan SRS

SRS ini mempertahankan batasan PRD: **fokus pada kebutuhan dan perilaku sistem, bukan bagaimana sistem dibangun**. Karena itu, detail seperti struktur backend, arsitektur, API, database schema, pemilihan library, desain UI, dan konfigurasi model **belum dimasukkan** dan seharusnya dibahas pada dokumen HLD/LLD.
