# DRAFT Acceptance Criteria & Metode Pengujian

## Sistem Pemantau Kepatuhan Masker Berbasis AI

> **Catatan pengujian:** Untuk skenario AI, `75%` digunakan sebagai ambang confidence yang diberikan pada spesifikasi. Target latensi yang digunakan adalah **≤1 detik per wajah**, sedangkan target akurasi klasifikasi masker adalah **≥95%**. Untuk pengujian akurasi, dataset uji harus memiliki label ground truth sehingga hasil prediksi dapat dibandingkan secara objektif.

---

# US-01 — Deteksi Wajah Real-Time ★

**Traceability:** FR-01, NFR-02
**Prioritas:** Must Have

### Scenario 1: Deteksi wajah pada kondisi normal

```gherkin
Scenario: Wajah jelas terdeteksi pada kondisi normal
  Given kamera aktif dan live feed tersedia
  And terdapat wajah yang terlihat jelas dengan pencahayaan cukup di dalam frame
  When sistem menerima frame yang mengandung wajah
  Then sistem mendeteksi wajah tersebut
  And hasil deteksi tersedia pada UI dalam waktu <= 1 detik per wajah
```

### Scenario 2: Wajah terpotong di tepi frame

```gherkin
Scenario: Wajah terpotong di tepi frame
  Given kamera aktif dan live feed tersedia
  And sebagian wajah berada di tepi frame sehingga wajah tidak terlihat sepenuhnya
  When sistem menerima frame tersebut
  Then sistem tidak mengalami crash
  And sistem hanya menghasilkan deteksi apabila wajah memenuhi kondisi deteksi
  And waktu pemrosesan tidak melebihi 1 detik per wajah yang berhasil diproses
```

### Scenario 3: Confidence deteksi rendah

```gherkin
Scenario: Wajah sulit dideteksi dengan confidence score < 75%
  Given kamera aktif dan wajah terlihat sebagian atau dalam pencahayaan remang
  When sistem memproses frame dan confidence score deteksi berada di bawah 75%
  Then sistem tidak membuat keputusan klasifikasi masker yang pasti berdasarkan deteksi tersebut
  And sistem tidak mengalami crash
```

### Scenario 4: Respons melebihi batas waktu

```gherkin
Scenario: Pemrosesan deteksi melebihi batas 1 detik
  Given kamera aktif dan sistem sedang menerima live feed
  When waktu pemrosesan deteksi satu wajah melebihi 1 detik
  Then sistem tidak menampilkan hasil tersebut sebagai hasil real-time yang memenuhi NFR-02
  And sistem tetap tidak mengalami crash
```

### Metode Uji

* **Integration Test:** kamera → proses deteksi wajah.
* **System Test:** live feed dengan kondisi pencahayaan dan posisi wajah berbeda.
* **Performance Test:** pengukuran timestamp frame masuk sampai hasil deteksi muncul.
* **Tools:** OpenCV, Python `time/perf_counter`, log timestamp, dataset/frame uji.

---

# US-02 — Klasifikasi Status Masker ★

**Traceability:** FR-02, NFR-01, NFR-02
**Prioritas:** Must Have

### Scenario 1: Klasifikasi masker berhasil

```gherkin
Scenario: Wajah dengan masker diklasifikasikan sebagai Pakai Masker
  Given kamera aktif dan wajah terlihat jelas dengan pencahayaan cukup
  And wajah menggunakan masker
  When sistem memproses wajah tersebut
  And confidence score klasifikasi >= 75%
  Then sistem menampilkan status "Pakai Masker"
  And hasil klasifikasi muncul dalam waktu <= 1 detik per wajah
```

### Scenario 2: Wajah tanpa masker diklasifikasikan

```gherkin
Scenario: Wajah tanpa masker diklasifikasikan sebagai Tidak Pakai Masker
  Given kamera aktif dan wajah terlihat jelas dengan pencahayaan cukup
  And wajah tidak menggunakan masker
  When sistem memproses wajah tersebut
  And confidence score klasifikasi >= 75%
  Then sistem menampilkan status "Tidak Pakai Masker"
  And hasil klasifikasi muncul dalam waktu <= 1 detik per wajah
```

### Scenario 3: Confidence klasifikasi di bawah 75%

```gherkin
Scenario: Klasifikasi masker menghasilkan confidence score < 75%
  Given kamera aktif dan wajah sebagian terpotong atau pencahayaan remang
  When sistem menghasilkan confidence score klasifikasi < 75%
  Then sistem menampilkan status "Tidak Pasti / Terhalang"
  And sistem tidak menampilkan "Pakai Masker" atau "Tidak Pakai Masker" sebagai keputusan pasti
  And sistem tidak mengalami crash
```

### Scenario 4: Akurasi klasifikasi mencapai target

```gherkin
Scenario: Akurasi klasifikasi masker memenuhi target
  Given tersedia dataset pengujian berlabel untuk kategori "Pakai Masker" dan "Tidak Pakai Masker"
  When seluruh data uji diproses oleh sistem
  Then persentase prediksi yang benar mencapai >= 95%
```

### Metode Uji

* **Unit Test:** fungsi klasifikasi dan penerapan threshold `0,75`.
* **Integration Test:** deteksi wajah → klasifikasi masker.
* **System Test:** pengujian pada dataset berlabel.
* **Performance Test:** pengukuran latensi per wajah.
* **Tools:** Python/pytest, OpenCV, confusion matrix, accuracy score, `perf_counter`.

---

# US-03 — Hasil Deteksi Real-Time ★

**Traceability:** FR-05, NFR-02, NFR-03
**Prioritas:** Must Have

### Scenario 1: Hasil ditampilkan secara real-time

```gherkin
Scenario: Hasil klasifikasi tampil pada live feed
  Given kamera aktif dan live feed berjalan
  And wajah terlihat jelas dengan pencahayaan cukup
  When sistem selesai mengklasifikasikan status masker
  Then hasil "Pakai Masker" atau "Tidak Pakai Masker" ditampilkan pada UI
  And hasil tampil dalam waktu <= 1 detik per wajah
```

### Scenario 2: Hasil meragukan

```gherkin
Scenario: UI menampilkan hasil tidak pasti
  Given kamera aktif dan wajah terdeteksi dalam kondisi pencahayaan remang
  When confidence score klasifikasi < 75%
  Then UI menampilkan indikator "Tidak Pasti / Terhalang"
  And UI tidak menampilkan status masker pasti
  And sistem tidak mengalami crash
```

### Scenario 3: Stream terputus saat proses berlangsung

```gherkin
Scenario: Live stream terputus ketika AI sedang memproses
  Given kamera aktif dan sistem sedang memproses live feed
  When stream kamera terputus sebelum hasil klasifikasi tersedia
  Then sistem tidak menampilkan hasil klasifikasi baru sebagai hasil valid
  And sistem menampilkan kondisi kegagalan kamera/stream
  And sistem tidak mengalami crash
```

### Scenario 4: Petugas memahami penggunaan dasar

```gherkin
Scenario: Petugas dapat memahami penggunaan dasar sistem
  Given petugas belum menerima pelatihan khusus
  When petugas diberikan akses ke fitur pemantauan
  Then petugas dapat memahami cara menjalankan pemantauan dasar dalam waktu <= 5 menit
```

### Metode Uji

* **E2E Test:** kamera → AI → UI.
* **Performance Test:** pengukuran waktu pemrosesan sampai hasil tampil.
* **Usability Test:** observasi petugas target tanpa pelatihan khusus.
* **Tools:** browser DevTools, Playwright/Selenium, stopwatch/log timestamp.

---

# US-04 — Prediksi Jenis Kelamin ★

**Traceability:** FR-03, NFR-02
**Prioritas:** Should Have

### Scenario 1: Prediksi jenis kelamin pada wajah jelas

```gherkin
Scenario: Jenis kelamin diprediksi dari wajah yang terlihat jelas
  Given kamera aktif dan wajah terlihat jelas dengan pencahayaan cukup
  When sistem memproses wajah yang terdeteksi
  Then sistem menghasilkan hasil klasifikasi jenis kelamin
  And hasil tersedia dalam waktu <= 1 detik per wajah
```

### Scenario 2: Wajah sebagian terpotong

```gherkin
Scenario: Prediksi jenis kelamin pada wajah yang terpotong
  Given kamera aktif dan sebagian wajah berada di tepi frame
  When sistem memproses wajah tersebut
  Then sistem tidak mengalami crash
  And sistem tidak menghasilkan klasifikasi apabila kualitas input tidak memenuhi kondisi deteksi
  And waktu pemrosesan tidak melebihi 1 detik untuk wajah yang berhasil diproses
```

### Scenario 3: Confidence hasil klasifikasi rendah

```gherkin
Scenario: Hasil prediksi jenis kelamin memiliki confidence score < 75%
  Given kamera aktif dan wajah berada pada kondisi pencahayaan remang
  When sistem menghasilkan confidence score < 75% pada proses klasifikasi
  Then sistem tidak memperlakukan hasil tersebut sebagai klasifikasi yang pasti
  And sistem tidak mengalami crash
```

### Scenario 4: Respons model melebihi batas

```gherkin
Scenario: Prediksi jenis kelamin membutuhkan waktu lebih dari 1 detik
  Given wajah telah terdeteksi dan proses prediksi dimulai
  When waktu dari awal pemrosesan sampai hasil tersedia > 1 detik
  Then hasil tersebut dinyatakan tidak memenuhi target NFR-02
  And sistem tetap dapat menangani proses tanpa crash
```

### Metode Uji

* **Unit Test:** fungsi prediksi dan penanganan confidence.
* **Integration Test:** deteksi wajah → prediksi jenis kelamin.
* **Performance Test:** pengukuran latensi per wajah.
* **System Test:** pengujian menggunakan dataset berlabel jenis kelamin.
* **Tools:** pytest, OpenCV, Python timer, confusion matrix.

---

# US-05 — Estimasi Rentang Usia ★

**Traceability:** FR-04, NFR-02
**Prioritas:** Should Have

### Scenario 1: Estimasi rentang usia berhasil

```gherkin
Scenario: Rentang usia dihasilkan dari wajah yang jelas
  Given kamera aktif dan wajah terlihat jelas dengan pencahayaan cukup
  When sistem memproses wajah tersebut
  Then sistem menghasilkan estimasi dalam bentuk rentang usia
  And hasil tersedia dalam waktu <= 1 detik per wajah
```

### Scenario 2: Wajah terpotong atau pencahayaan remang

```gherkin
Scenario: Estimasi usia pada input wajah berkualitas rendah
  Given kamera aktif dan wajah sebagian terpotong atau berada dalam pencahayaan remang
  When sistem memproses wajah tersebut
  Then sistem tidak mengalami crash
  And sistem tidak menghasilkan estimasi yang diperlakukan sebagai hasil pasti apabila kualitas input tidak memadai
```

### Scenario 3: Confidence hasil klasifikasi rendah

```gherkin
Scenario: Hasil estimasi memiliki confidence score < 75%
  Given wajah berhasil dideteksi tetapi kualitas visual rendah
  When confidence score hasil klasifikasi < 75%
  Then sistem menandai hasil sebagai tidak pasti
  And sistem tidak memperlakukan estimasi tersebut sebagai hasil pasti
  And sistem tidak mengalami crash
```

### Scenario 4: Model tidak merespons dalam batas waktu

```gherkin
Scenario: Proses estimasi usia melebihi 1 detik
  Given wajah telah terdeteksi dan proses estimasi usia dimulai
  When hasil estimasi baru tersedia setelah > 1 detik
  Then proses tersebut dinyatakan tidak memenuhi NFR-02
  And sistem tidak mengalami crash
```

### Metode Uji

* **Unit Test:** fungsi estimasi dan validasi output rentang usia.
* **Integration Test:** deteksi wajah → estimasi usia.
* **Performance Test:** pengukuran latensi.
* **System Test:** pengujian dataset dengan label rentang usia.
* **Tools:** pytest, OpenCV, Python timer, confusion matrix/accuracy sesuai bentuk label pengujian.

---

# US-06 — Pencatatan Otomatis Hasil Deteksi

**Traceability:** FR-06, NFR-06
**Prioritas:** Must Have

### Scenario 1: Log berhasil dibuat otomatis

```gherkin
Scenario: Hasil deteksi dicatat otomatis
  Given sistem berhasil menghasilkan klasifikasi status masker
  When hasil klasifikasi tersedia
  Then sistem membuat log secara otomatis tanpa input manual dari petugas
  And log mencatat timestamp
  And log mencatat status_masker
```

### Scenario 2: Status masker tercatat dengan nilai valid

```gherkin
Scenario: Log menyimpan status masker yang valid
  Given sistem menghasilkan status masker dengan confidence score >= 75%
  When sistem menyimpan hasil deteksi
  Then nilai status_masker adalah "Pakai Masker" atau "Tidak Pakai Masker"
```

### Scenario 3: Hasil tidak pasti tidak menjadi keputusan pasti

```gherkin
Scenario: Hasil dengan confidence score < 75% ditangani sebagai tidak pasti
  Given sistem menghasilkan confidence score < 75%
  When sistem memproses hasil tersebut
  Then status yang ditampilkan adalah "Tidak Pasti / Terhalang"
  And sistem tidak mencatatnya sebagai "Pakai Masker" atau "Tidak Pakai Masker" yang pasti
```

### Metode Uji

* **Unit Test:** fungsi pembentukan log.
* **Integration Test:** AI → pencatatan log.
* **System Test:** verifikasi log setelah beberapa deteksi.
* **Tools:** pytest, database inspection/query, log assertion.

---

# US-07 — Kelengkapan Data Log Deteksi

**Traceability:** FR-06, NFR-05, NFR-06
**Prioritas:** Must Have

### Scenario 1: Log menyimpan seluruh data yang tersedia

```gherkin
Scenario: Log menyimpan data deteksi dan demografis
  Given sistem menghasilkan status masker, jenis kelamin, dan rentang usia
  When hasil deteksi dicatat
  Then log memiliki timestamp
  And log memiliki status_masker
  And log memiliki jenis_kelamin
  And log memiliki rentang_usia
```

### Scenario 2: Data demografis tidak tersedia

```gherkin
Scenario: Log tetap dibuat ketika data demografis tidak tersedia
  Given sistem berhasil menghasilkan status masker
  And data jenis kelamin atau rentang usia tidak tersedia
  When hasil deteksi dicatat
  Then log tetap dibuat
  And timestamp tetap tersedia
  And status_masker tetap tersedia
  And data demografis yang tidak tersedia tidak diisi dengan nilai hasil tebakan manual
```

### Scenario 3: Gambar wajah mentah tidak disimpan

```gherkin
Scenario: Data wajah mentah tidak tersimpan permanen
  Given sistem telah melakukan deteksi dan mencatat hasil klasifikasi
  When penyimpanan data diperiksa setelah proses deteksi selesai
  Then jumlah gambar wajah mentah yang tersimpan permanen di server/database adalah 0
```

### Metode Uji

* **Integration Test:** AI → database.
* **Database Test:** validasi struktur dan isi log.
* **Security/Privacy Test:** pemeriksaan storage/database.
* **Tools:** SQL query, database inspection, filesystem inspection, automated assertions.

---

# US-08 — Ringkasan Data Deteksi & Demografis Agregat

**Traceability:** FR-07, NFR-03
**Prioritas:** Should Have

### Scenario 1: Ringkasan data tersedia

```gherkin
Scenario: Sistem menampilkan ringkasan hasil deteksi
  Given terdapat log hasil deteksi yang telah tersimpan
  When manajemen membuka ringkasan data
  Then sistem menampilkan data agregat kepatuhan masker
  And sistem menampilkan data demografis yang tersedia
```

### Scenario 2: Ringkasan tidak menggunakan gambar wajah

```gherkin
Scenario: Ringkasan menggunakan data klasifikasi
  Given terdapat log hasil deteksi
  When sistem menghasilkan ringkasan data
  Then ringkasan menggunakan data klasifikasi yang tercatat
  And sistem tidak mengambil gambar wajah mentah sebagai data laporan
```

### Scenario 3: Petugas memahami fungsi dasar ringkasan

```gherkin
Scenario: Pengguna memahami penggunaan dasar fitur
  Given pengguna belum menerima pelatihan khusus
  When pengguna diberikan akses ke fitur ringkasan
  Then pengguna dapat memahami fungsi dasar fitur dalam waktu <= 5 menit
```

### Metode Uji

* **Integration Test:** log → agregasi data.
* **System Test:** verifikasi hasil agregasi dengan data log.
* **Usability Test:** pengujian terhadap pengguna target.
* **Tools:** SQL/data validation, browser testing, Playwright/Selenium.

---

# US-09 — Informasi Pesan Kesalahan Kamera Gagal

**Traceability:** FR-08, NFR-04
**Prioritas:** Must Have

### Scenario 1: Kamera tidak ditemukan

```gherkin
Scenario: Sistem menangani kamera yang tidak tersedia
  Given perangkat tidak memiliki kamera yang dapat diakses
  When petugas membuka fitur pemantauan
  Then sistem menampilkan pesan bahwa kamera tidak ditemukan
  And sistem tidak memulai proses deteksi wajah
```

### Scenario 2: Izin kamera ditolak

```gherkin
Scenario: Petugas menolak izin kamera
  Given browser meminta izin akses kamera
  When petugas menolak izin kamera
  Then sistem menampilkan pesan bahwa akses kamera ditolak
  And sistem memberikan informasi untuk mencoba kembali setelah izin tersedia
  And sistem tidak mengalami crash
```

### Scenario 3: Kamera gagal saat pemantauan

```gherkin
Scenario: Kamera terputus saat live monitoring
  Given live feed sedang berjalan
  When koneksi kamera terputus
  Then sistem menampilkan pesan kesalahan kamera
  And sistem tidak menampilkan hasil deteksi baru dari stream yang sudah terputus
  And sistem tidak mengalami crash
```

### Metode Uji

* **System Test:** simulasi kamera tidak tersedia/terputus.
* **E2E Test:** browser permission denied.
* **Negative Test:** berbagai kondisi kegagalan perangkat.
* **Tools:** Playwright/Selenium, browser permission control, device camera simulation.

---

# US-10 — Stabilitas Sistem Saat Kamera Gagal

**Traceability:** FR-08, NFR-04
**Prioritas:** Must Have

### Scenario 1: Kamera gagal tanpa menyebabkan crash

```gherkin
Scenario: Sistem tetap berjalan ketika kamera gagal
  Given sistem berada pada halaman pemantauan
  When kamera tidak tersedia atau gagal diakses
  Then sistem tidak mengalami crash
  And sistem menampilkan pesan kesalahan kamera
  And sistem tetap memberikan respons kepada pengguna
```

### Scenario 2: Kamera terputus di tengah pemantauan

```gherkin
Scenario: Sistem menangani kamera yang terputus saat live feed
  Given live feed kamera sedang aktif
  When kamera terputus secara tiba-tiba
  Then sistem mendeteksi kegagalan akses kamera
  And sistem menampilkan pesan kesalahan
  And sistem tidak mengalami crash
```

### Scenario 3: Pengujian seluruh skenario kegagalan kamera

```gherkin
Scenario: Seluruh kasus kamera gagal ditangani tanpa crash
  Given tersedia skenario kamera tidak ditemukan, izin ditolak, dan kamera terputus
  When seluruh skenario tersebut diuji
  Then 100% skenario menghasilkan penanganan error
  And 0% skenario menyebabkan crash pada browser atau sistem
```

### Metode Uji

* **System Test:** pengujian skenario kegagalan kamera.
* **Negative Test:** kamera tidak ditemukan, izin ditolak, kamera dicabut/terputus.
* **Reliability Test:** pengulangan skenario kegagalan.
* **Tools:** Playwright/Selenium, browser DevTools, simulasi device/camera, application log.

---

# Rekapitulasi Acceptance Criteria

| User Story                   | Prioritas | Jumlah Skenario | Metrik Utama                      | Metode Utama              |
| ---------------------------- | --------- | --------------: | --------------------------------- | ------------------------- |
| **US-01** Deteksi Wajah      | Must      |               4 | ≤1 detik/wajah                    | Integration + Performance |
| **US-02** Klasifikasi Masker | Must      |               4 | ≥95%; threshold 75%; ≤1 detik     | System + Accuracy         |
| **US-03** Hasil Real-Time    | Must      |               4 | ≤1 detik; ≤5 menit usability      | E2E + Usability           |
| **US-04** Jenis Kelamin      | Should    |               4 | ≤1 detik; threshold 75%           | Integration + Performance |
| **US-05** Rentang Usia       | Should    |               4 | ≤1 detik; threshold 75%           | Integration + Performance |
| **US-06** Log Otomatis       | Must      |               3 | Otomatis; data tercatat           | Integration               |
| **US-07** Kelengkapan Log    | Must      |               3 | 0 gambar mentah; field lengkap    | Database + Privacy        |
| **US-08** Data Agregat       | Should    |               3 | ≤5 menit usability                | System + Usability        |
| **US-09** Error Kamera       | Must      |               3 | Error ditampilkan; no crash       | E2E + Negative            |
| **US-10** Stabilitas Kamera  | Must      |               3 | **100%** tertangani; **0% crash** | Reliability + Negative    |

### Parameter QA yang menjadi acuan

* **Confidence ≥75%** → hasil klasifikasi masker dapat ditampilkan sebagai **Pakai Masker / Tidak Pakai Masker**.
* **Confidence <75%** → **Tidak Pasti / Terhalang**, tanpa keputusan masker pasti.
* **Latensi ≤1 detik/wajah** → memenuhi NFR-02.
* **Akurasi klasifikasi masker ≥95%** → memenuhi NFR-01.
* **0 gambar wajah mentah permanen** → memenuhi NFR-05.
* **100% kasus kamera gagal tertangani tanpa crash** → memenuhi NFR-04.
* **Log minimal:** `timestamp`, `status_masker`, serta `jenis_kelamin` dan `rentang_usia` **jika tersedia** → memenuhi NFR-06.
