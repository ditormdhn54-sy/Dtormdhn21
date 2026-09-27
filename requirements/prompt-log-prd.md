[Peran] Kamu adalah product manager senior untuk produk Mobile/Web berfitur AI.
[Tugas] Susun DRAF PRD ringkas untuk "Sistem Pemantau Kepatuhan Masker Berbasis AI" berdasarkan kasus berikut.
[Konteks]
  Problem statement : Sejak pandemi COVID-19, kepatuhan penggunaan masker di tempat umum (gedung perkantoran, mall, fasilitas kesehatan) masih perlu dipantau, namun verifikasi manual oleh petugas keamanan lambat, tidak konsisten, dan menguras tenaga terutama di lokasi dengan lalu lintas pengunjung tinggi. Dibutuhkan sistem otomatis yang dapat mendeteksi kepatuhan masker secara real-time sekaligus memberi data demografis pengunjung untuk kebutuhan keamanan dan analisis.
  Target user : Petugas keamanan/resepsionis gedung publik — persona: "Pak Andi", satpam gedung perkantoran, butuh alat verifikasi cepat tanpa kontak fisik.
  Stakeholder lain : Manajemen gedung (butuh data agregat kepatuhan & demografis pengunjung untuk pelaporan).
  Persona ringkas : Pak Andi, 35 tahun, satpam gedung perkantoran. Shift pagi-malam, menghadapi ratusan pengunjung tiap hari. Kesulitan menegur satu per satu dan mencatat manual. Butuh sistem yang cepat, akurat, dan mudah digunakan.
  Bukti riset : Model CNN berbasis MobileNet mencapai akurasi deteksi masker 99%, sedangkan prediksi jenis kelamin dan usia memiliki akurasi 98,75%, dengan sensitivity 98,5% dan specificity 99%, dan implementasi real-time menggunakan OpenCV menunjukkan latensi deteksi rendah dan responsivitas yang baik (Sopian, Setiadi, & Agustino, 2024, DOI: 10.37012/jtik.v10i2.2395).
  Platform & stack : Website — backend Python (OpenCV + model CNN/MobileNet), frontend web untuk live feed & laporan.
  Fitur AI inti : Computer Vision — deteksi status masker + prediksi jenis kelamin & estimasi usia dari wajah, real-time.
  Konstrain : prototype 1 semester; data & biaya AI terbatas.
  Functional Requirements:
    FR-01 Mendeteksi wajah dari live feed kamera secara real-time
    FR-02 Mengklasifikasikan status masker (pakai/tidak) dari wajah terdeteksi
    FR-03 Memprediksi jenis kelamin dari wajah terdeteksi
    FR-04 Memprediksi estimasi rentang usia dari wajah terdeteksi
    FR-05 Menampilkan hasil deteksi di dashboard secara real-time
    FR-06 Menyimpan log deteksi (timestamp, status, demografis) ke database
  Non-Functional Requirements:
    NFR-01 Akurasi deteksi masker ≥95%
    NFR-02 Latensi deteksi & prediksi <1 detik per wajah
    NFR-03 Privasi: gambar wajah mentah tidak disimpan permanen, hanya hasil klasifikasi
    NFR-04 Usability: petugas paham dashboard tanpa training khusus <5 menit
    NFR-05 Reliability: pesan error jelas saat kamera gagal akses, sistem tidak crash

[Format output]
 1) Ringkasan eksekutif;
 2) Problem statement & bukti (pisahkan fakta vs asumsi);
  3) Target user & stakeholder (tabel peran–kebutuhan–pengaruh);
  4) Value proposition: pain yang dikurangi, gain yang diciptakan, mengapa fitur AI bukan gimmick;
  5) Tujuan produk & KPI terukur (+ cara mengukurnya);
  6) Scope fitur 3 bulan: tabel MoSCoW (fitur AI bertanda ★);
  7) Non-goals eksplisit;
  8) Asumsi & risiko utama + mitigasi.

[Aturan]
    - Hanya gunakan data pada [Konteks]; bila kurang, tulis [ASUMSI-XX] lalu lanjutkan.
    - Jangan menulis solusi teknis/arsitektur (itu urusan SRS/HLD/LLD).
    - Bahasa Indonesia baku, format Markdown.