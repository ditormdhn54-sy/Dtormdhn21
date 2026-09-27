[Peran] Kamu adalah requirements analyst senior.
[Tugas] Ubah PRD berikut menjadi DRAF SRS ringkas.
[Konteks]
  PRD hasil revisi :
  DRAF PRD — Sistem Pemantau Kepatuhan Masker Berbasis AI
    1. Ringkasan Eksekutif
  Sistem Pemantau Kepatuhan Masker Berbasis AI adalah produk berbasis website yang membantu petugas keamanan atau resepsionis gedung publik memantau kepatuhan penggunaan masker secara real-time melalui kamera.
  Produk berfokus pada tiga kemampuan AI utama: deteksi wajah, klasifikasi status masker, serta prediksi jenis kelamin dan estimasi rentang usia. Hasil deteksi ditampilkan secara langsung pada dashboard dan dicatat sebagai data klasifikasi untuk kebutuhan pemantauan dan pelaporan agregat.
  Target utama adalah Pak Andi, petugas keamanan yang menangani ratusan pengunjung per hari dan mengalami kesulitan melakukan pemeriksaan serta pencatatan secara manual.
  Berdasarkan bukti riset yang diberikan, model CNN berbasis MobileNet mencapai akurasi deteksi masker 99%, sementara prediksi jenis kelamin dan usia mencapai akurasi 98,75%, dengan sensitivity 98,5% dan specificity 99%. Implementasi real-time menggunakan OpenCV juga dilaporkan memiliki latensi rendah dan responsivitas yang baik (Sopian, Setiadi, & Agustino, 2024, DOI: 10.37012/jtik.v10i2.2395).

    2. Problem Statement & Bukti
  Problem Statement: Kepatuhan penggunaan masker di tempat umum masih perlu dipantau. Verifikasi secara manual oleh petugas keamanan lambat, tidak konsisten, dan menguras tenaga terutama saat lalu lintas pengunjung tinggi.
  FAKTA: Petugas keamanan perlu memantau kepatuhan penggunaan masker di tempat umum. Verifikasi manual dinyatakan lambat, tidak konsisten, dan menguras tenaga. Target user menghadapi ratusan pengunjung setiap hari. Riset melaporkan akurasi deteksi masker 99%, akurasi prediksi jenis kelamin dan usia 98,75%, sensitivity 98,5%, specificity 99%. Implementasi real-time menggunakan OpenCV memiliki latensi rendah.
  ASUMSI-01: Dashboard dapat digunakan oleh petugas dengan perangkat yang memiliki kamera.
  ASUMSI-02: Data hasil klasifikasi cukup untuk kebutuhan pelaporan manajemen tanpa menyimpan gambar wajah mentah.
  ASUMSI-03: Rentang usia dapat ditentukan sesuai kebutuhan prototype.
  ASUMSI-04: Target penggunaan prototype adalah lokasi dengan akses kamera yang memadai.
  ASUMSI-05: Pemantauan tidak memerlukan kontak fisik dan tidak menyimpan gambar wajah secara permanen.

    3. Target User & Stakeholder: Petugas keamanan/resepsionis (Pak Andi) - pengguna utama. Manajemen gedung - penentu nilai bisnis. Pengunjung - pihak terdampak.

  4. Value Proposition: Pain: pemeriksaan manual lambat, pencatatan manual, ketidakkonsistenan. Gain: pemantauan real-time, pencatatan otomatis, data agregat, tanpa kontak fisik. AI inti karena harus interpretasi visual wajah otomatis.

    5. Tujuan Produk & KPI: Akurasi deteksi masker ≥95%. Latensi deteksi & prediksi <1 detik/wajah. Usability ≤5 menit. Log tercatat ≥95%. 0 gambar wajah mentah tersimpan. Error handling 100%.

  6. Scope Fitur 3 Bulan — MoSCoW:
  Must: ★ FR-01 Deteksi wajah, ★ FR-02 Deteksi status masker, ★ FR-05 Dashboard real-time, FR-06 Log deteksi, Error kamera
  Should: ★ FR-03 Prediksi jenis kelamin, ★ FR-04 Estimasi usia, Ringkasan data [ASUMSI-08]
  Could: Filter laporan [ASUMSI-09], Visualisasi statistik [ASUMSI-10]
  Won't: Penyimpanan gambar wajah permanen, Identifikasi identitas individu, Sistem penegakan/sanksi otomatis

    7. Non-Goals: Identifikasi identitas, simpan gambar wajah mentah, sanksi otomatis, sistem keamanan penuh, pengenalan wajah individu.

  8. Asumsi & Risiko: Kamera tidak memadai, kategori usia belum ditentukan, kegagalan pencatatan, akurasi turun karena kondisi, privasi, kamera gagal diakses, data & biaya terbatas.

  Platform & stack : Website — backend Python (OpenCV + model CNN/MobileNet), frontend web untuk live feed & laporan.

  Acuan kualitas : ISO/IEC 25010
  Prioritas : MoSCoW

[Format output]
 1) Tujuan, scope, definisi istilah;
 2) User & stakeholder, lingkungan operasi, asumsi & dependensi;
 3) FR: tabel FR-01..FR-n — pola "Sistem harus dapat <aksi> <objek> saat <kondisi> → <output>" + ID, prioritas MoSCoW, metode verifikasi;
 4) NFR: tabel NFR-01..NFR-m — kategori ISO/IEC 25010 + metrik + target + kondisi ukur (wajib: akurasi & latensi AI, keamanan, privasi, usability);
 5) Kebutuhan data minimum fitur AI (input → output model);
 6) Aturan bisnis hasil riset;
 7) Matriks traceability: FR/NFR → fitur PRD terkait.

[Aturan]
    - Setiap FR/NFR harus dapat ditelusuri ke bukti pada PRD/riset; dilarang menambah kebutuhan tanpa bukti.
    - Bila pembahasan mulai masuk arsitektur/UI, hentikan (itu urusan HLD/LLD).
    - Bahasa Indonesia baku, format Markdown.