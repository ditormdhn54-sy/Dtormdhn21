[Peran]
Kamu adalah software architect senior untuk aplikasi Mobile/Web berfitur AI.

[Tugas]
Buat DRAF HLD (High-Level Design) dari PRD, SRS, dan User Stories berikut.

[Konteks]
Platform & stack          : Website
Konstrain                 : prototype 1 semester; satu fitur AI inti (deteksi wajah + klasifikasi masker); biaya minimal
Stack yang disarankan     : Frontend React/Next.js, Backend Python FastAPI, AI service berbasis OpenCV + TensorFlow/MobileNet (sesuai bukti riset), Database PostgreSQL atau SQLite, deployment free-tier (Vercel + Render/Railway).

PRD hasil revisi:
DRAF PRD — Sistem Pemantau Kepatuhan Masker Berbasis AI

1. Ringkasan Eksekutif
Sistem Pemantau Kepatuhan Masker Berbasis AI adalah produk berbasis website yang membantu petugas keamanan atau resepsionis gedung publik memantau kepatuhan penggunaan masker secara real-time melalui kamera.
Produk berfokus pada tiga kemampuan AI utama: deteksi wajah, klasifikasi status masker, serta prediksi jenis kelamin dan estimasi rentang usia. Hasil deteksi ditampilkan secara langsung pada dashboard dan dicatat sebagai data klasifikasi untuk kebutuhan pemantauan dan pelaporan agregat.
Target utama adalah Pak Andi, petugas keamanan yang menangani ratusan pengunjung per hari dan mengalami kesulitan melakukan pemeriksaan serta pencatatan secara manual.
Berdasarkan bukti riset yang diberikan, model CNN berbasis MobileNet mencapai akurasi deteksi masker 99%, sementara prediksi jenis kelamin dan usia mencapai akurasi 98,75%, dengan sensitivity 98,5% dan specificity 99%. Implementasi real-time menggunakan OpenCV juga dilaporkan memiliki latensi rendah dan responsivitas yang baik (Sopian, Setiadi, & Agustino, 2024, DOI: 10.37012/jtik.v10i2.2395).

2. Problem Statement & Bukti
Problem Statement
Kepatuhan penggunaan masker di tempat umum masih perlu dipantau. Verifikasi secara manual oleh petugas keamanan memiliki beberapa masalah:
* Lambat ketika jumlah pengunjung tinggi.
* Tidak konsisten karena bergantung pada petugas.
* Menguras tenaga petugas.
* Pencatatan kepatuhan dan demografis secara manual tidak efisien.

Fakta vs Asumsi
| Jenis     | Pernyataan                                                                                                             |
| --------- | ---------------------------------------------------------------------------------------------------------------------- |
| FAKTA     | Petugas keamanan perlu memantau kepatuhan penggunaan masker di tempat umum.                                            |
| FAKTA     | Verifikasi manual dinyatakan lambat, tidak konsisten, dan menguras tenaga.                                             |
| FAKTA     | Target user menghadapi ratusan pengunjung setiap hari.                                                                 |
| FAKTA     | Riset yang diberikan melaporkan akurasi deteksi masker 99%.                                                            |
| FAKTA     | Riset melaporkan akurasi prediksi jenis kelamin dan usia 98,75%.                                                       |
| FAKTA     | Riset melaporkan sensitivity 98,5% dan specificity 99%.                                                                |
| FAKTA     | Implementasi real-time menggunakan OpenCV dilaporkan memiliki latensi rendah dan responsivitas baik.                   |
| ASUMSI-01 | Dashboard dapat digunakan oleh petugas dengan perangkat yang memiliki kamera.                                          |
| ASUMSI-02 | Data hasil klasifikasi cukup untuk kebutuhan pelaporan manajemen tanpa menyimpan gambar wajah mentah.                  |
| ASUMSI-03 | Rentang usia yang digunakan dapat ditentukan sesuai kebutuhan prototype karena konteks tidak menetapkan kategori usia. |
| ASUMSI-04 | Target penggunaan prototype adalah lokasi dengan akses kamera yang memadai.                                            |

3. Target User & Stakeholder
| Peran                                   | Kebutuhan                                                                                                  | Pengaruh                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| Petugas keamanan/resepsionis (Pak Andi) | Deteksi cepat, dashboard sederhana, informasi status masker secara real-time, tanpa kontak fisik           | Tinggi — pengguna utama                   |
| Manajemen gedung                        | Data agregat kepatuhan dan demografis untuk pelaporan dan analisis                                         | Tinggi — menentukan nilai bisnis produk   |
| Pengunjung                              | [ASUMSI-05] Pemantauan yang tidak memerlukan kontak fisik dan tidak menyimpan gambar wajah secara permanen | Sedang — pihak yang terdampak oleh sistem |

4. Value Proposition
Pain yang Dikurangi
1. Mengurangi kebutuhan petugas untuk memeriksa pengunjung satu per satu.
2. Mengurangi pencatatan manual.
3. Mengurangi beban petugas ketika lalu lintas pengunjung tinggi.
4. Mengurangi ketidakkonsistenan proses pemantauan manual.
Gain yang Diciptakan
1. Pemantauan real-time terhadap status masker.
2. Respons lebih cepat terhadap pengunjung yang tidak menggunakan masker.
3. Pencatatan otomatis timestamp, status masker, dan data demografis hasil klasifikasi.
4. Data agregat yang dapat digunakan manajemen untuk pelaporan.
5. Penggunaan tanpa kontak fisik.
Mengapa AI Bukan Gimmick?
AI memiliki fungsi inti dalam produk karena sistem harus menginterpretasikan informasi visual dari wajah secara otomatis dan mengklasifikasikannya menjadi status masker, jenis kelamin, serta estimasi usia.
Tanpa kemampuan computer vision, sistem tidak dapat menjalankan fungsi utama pemantauan otomatis. Selain itu, bukti riset yang diberikan menunjukkan performa model yang tinggi serta kemampuan implementasi real-time.

5. Tujuan Produk & KPI Terukur
| Tujuan                                    | KPI                                             | Target                                               | Cara Mengukur                                                        |
| ----------------------------------------- | ----------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------- |
| Mendeteksi kepatuhan masker secara akurat | Akurasi deteksi masker                          | ≥95%                                                 | Pengujian hasil prediksi model terhadap data berlabel                |
| Memberikan respons real-time              | Latensi deteksi & prediksi                      | <1 detik/wajah                                       | Mengukur waktu dari wajah terdeteksi hingga hasil klasifikasi muncul |
| Membantu petugas melakukan pemantauan     | Waktu penggunaan dashboard                      | [ASUMSI-06] ≤5 menit untuk memahami penggunaan dasar | Uji usability terhadap pengguna target                               |
| Mengurangi pencatatan manual              | Persentase hasil deteksi yang tercatat otomatis | [ASUMSI-07] ≥95%                                     | Membandingkan deteksi yang terjadi dengan log yang tersimpan         |
| Menjaga privasi                           | Gambar wajah mentah tersimpan permanen          | 0                                                    | Audit penyimpanan data setelah proses deteksi                        |
| Menjaga stabilitas penggunaan             | Sistem tidak crash ketika kamera gagal diakses  | 100% kasus menampilkan pesan error                   | Pengujian skenario kegagalan akses kamera                            |

6. Scope Fitur 3 Bulan — MoSCoW
| Prioritas   | Fitur                             | Deskripsi                                                                          |
| ----------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| Must Have   | ★ FR-01 Deteksi wajah             | Mendeteksi wajah dari live feed kamera secara real-time                            |
| Must Have   | ★ FR-02 Deteksi status masker     | Mengklasifikasikan wajah menjadi menggunakan atau tidak menggunakan masker         |
| Must Have   | ★ FR-05 Dashboard real-time       | Menampilkan hasil deteksi secara langsung kepada petugas                           |
| Must Have   | FR-06 Log deteksi                 | Menyimpan timestamp, status masker, dan hasil demografis                           |
| Must Have   | Error kamera                      | Menampilkan pesan yang jelas ketika kamera gagal diakses                           |
| Should Have | ★ FR-03 Prediksi jenis kelamin    | Memberikan hasil klasifikasi jenis kelamin dari wajah terdeteksi                   |
| Should Have | ★ FR-04 Estimasi usia             | Memberikan estimasi dalam bentuk rentang usia                                      |
| Should Have | Ringkasan data                    | [ASUMSI-08] Menampilkan ringkasan agregat kepatuhan dan demografis untuk manajemen |
| Could Have  | Filter laporan                    | [ASUMSI-09] Filter data berdasarkan periode waktu                                  |
| Could Have  | Visualisasi statistik             | [ASUMSI-10] Grafik sederhana mengenai tingkat kepatuhan                            |
| Won't Have  | Penyimpanan gambar wajah permanen | Tidak termasuk karena bertentangan dengan kebutuhan privasi                        |
| Won't Have  | Identifikasi identitas individu   | Tidak termasuk dalam kebutuhan produk                                              |
| Won't Have  | Sistem penegakan/sanksi otomatis  | Sistem hanya melakukan pemantauan dan pencatatan                                   |

Catatan: ★ menandai fitur yang menggunakan AI.

7. Non-Goals
Untuk menjaga prototype tetap realistis dalam batas waktu 1 semester, produk tidak mencakup:
1. Identifikasi nama atau identitas spesifik pengunjung.
2. Penyimpanan permanen gambar wajah mentah.
3. Pemberian sanksi atau tindakan otomatis kepada pengunjung.
4. Sistem keamanan gedung secara keseluruhan.
5. Fungsi pengenalan wajah untuk mencari individu tertentu.
6. Fitur di luar pemantauan masker dan data demografis yang disebutkan dalam konteks.
7. Pengembangan produk berskala penuh untuk seluruh gedung/instansi di luar kebutuhan prototype.

8. Asumsi & Risiko Utama + Mitigasi
| Asumsi/Risiko                                                    | Dampak                                    | Mitigasi                                                                       |
| ---------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------ |
| ASUMSI-01: Perangkat memiliki kamera yang memadai                | Deteksi tidak dapat berjalan              | Uji penggunaan dengan perangkat yang tersedia sebelum implementasi             |
| ASUMSI-03: Kategori rentang usia belum ditentukan                | Hasil usia tidak seragam                  | Menentukan kategori rentang usia sebelum tahap pengujian                       |
| ASUMSI-07: Sebagian hasil deteksi mungkin gagal tercatat         | Data laporan tidak lengkap                | Melakukan pengujian pencatatan dan menangani kegagalan dengan pesan yang jelas |
| Risiko: Kondisi wajah/kamera dapat memengaruhi hasil deteksi     | Akurasi menurun                           | Melakukan pengujian pada kondisi penggunaan yang relevan                       |
| Risiko: Akurasi aktual prototype berbeda dengan hasil penelitian | KPI tidak tercapai                        | Melakukan evaluasi menggunakan data pengujian sendiri                          |
| Risiko: Prediksi demografis dapat menghasilkan kesalahan         | Data analisis kurang akurat               | Menampilkan hasil sebagai estimasi/klasifikasi, bukan fakta identitas individu |
| Risiko: Privasi pengunjung                                       | Potensi masalah privasi                   | Tidak menyimpan gambar wajah mentah secara permanen                            |
| Risiko: Kamera gagal diakses                                     | Pemantauan terhenti                       | Menampilkan pesan error yang jelas dan mencegah sistem crash                   |
| Keterbatasan: Data dan biaya AI terbatas                         | Pengembangan model/fitur menjadi terbatas | Memprioritaskan fitur Must Have untuk prototype 3 bulan                        |

Prioritas MVP
Jika waktu pengembangan semakin terbatas, urutan prioritas MVP adalah:
Deteksi wajah → Deteksi masker ★ → Dashboard real-time → Log deteksi → Estimasi demografis ★ → Laporan agregat.
Dengan demikian, deteksi kepatuhan masker tetap menjadi fungsi AI utama, sedangkan prediksi jenis kelamin dan usia menjadi fitur pendukung untuk kebutuhan analisis manajemen.

SRS hasil revisi:
DRAF SRS Ringkas
Sistem Pemantau Kepatuhan Masker Berbasis AI

1. Tujuan, Scope, dan Definisi Istilah
1.1 Tujuan
Sistem bertujuan menyediakan pemantauan kepatuhan penggunaan masker secara real-time melalui kamera sehingga petugas keamanan/resepsionis dapat melakukan verifikasi secara lebih cepat dibandingkan pemeriksaan manual.
Sistem juga menghasilkan klasifikasi jenis kelamin dan estimasi rentang usia untuk mendukung kebutuhan data agregat manajemen gedung.

1.2 Scope Sistem
Dalam scope:
* Deteksi wajah dari live feed kamera.
* Klasifikasi status penggunaan masker.
* Prediksi jenis kelamin.
* Estimasi rentang usia.
* Penyajian hasil deteksi secara real-time.
* Pencatatan hasil deteksi.
* Ringkasan data agregat.
* Penanganan kegagalan akses kamera.

Di luar scope:
* Identifikasi nama/identitas individu.
* Pengenalan wajah individu.
* Penyimpanan permanen gambar wajah mentah.
* Pemberian sanksi otomatis.
* Sistem keamanan gedung secara keseluruhan.

1.3 Definisi Istilah
| Istilah         | Definisi                                                                                 |
| --------------- | ---------------------------------------------------------------------------------------- |
| AI              | Kemampuan sistem melakukan klasifikasi/prediksi berdasarkan data visual.                 |
| Computer Vision | Pemrosesan informasi visual dari kamera untuk memperoleh hasil deteksi atau klasifikasi. |
| Deteksi wajah   | Proses menemukan wajah pada input kamera.                                                |
| Status masker   | Klasifikasi apakah wajah menggunakan atau tidak menggunakan masker.                      |
| Jenis kelamin   | Hasil klasifikasi jenis kelamin dari wajah terdeteksi.                                   |
| Estimasi usia   | Perkiraan usia dalam bentuk rentang usia.                                                |
| Live feed       | Input gambar/video yang diperoleh secara langsung dari kamera.                           |
| Log deteksi     | Catatan hasil deteksi yang mencakup timestamp, status masker, dan data demografis.       |

2. User, Stakeholder, Lingkungan Operasi, Asumsi & Dependensi
2.1 User dan Stakeholder
| Aktor                        | Peran           | Kebutuhan                                                                 |
| ---------------------------- | --------------- | ------------------------------------------------------------------------- |
| Petugas keamanan/resepsionis | Pengguna utama  | Memantau status masker secara cepat dan real-time                         |
| Manajemen gedung             | Pengguna data   | Memperoleh data agregat kepatuhan dan demografis                          |
| Pengunjung                   | Pihak terdampak | Pemantauan tanpa kontak fisik dan tanpa penyimpanan permanen gambar wajah |

2.2 Lingkungan Operasi
Sistem digunakan pada:
* Platform website.
* Lokasi publik seperti gedung perkantoran, mall, atau fasilitas kesehatan.
* Lingkungan dengan akses kamera.
* Kondisi lalu lintas pengunjung yang dapat mencapai ratusan orang per hari.
Detail perangkat keras, jaringan, sistem operasi, dan spesifikasi infrastruktur belum ditentukan dalam PRD sehingga tidak menjadi kebutuhan SRS.

2.3 Asumsi
| ID    | Asumsi                                                                             |
| ----- | ---------------------------------------------------------------------------------- |
| AS-01 | Perangkat yang digunakan memiliki akses kamera.                                    |
| AS-02 | Kondisi kamera memungkinkan wajah terdeteksi.                                      |
| AS-03 | Data klasifikasi dapat memenuhi kebutuhan pelaporan tanpa menyimpan gambar mentah. |
| AS-04 | Rentang usia dapat ditentukan untuk kebutuhan prototype.                           |
| AS-05 | Pemantauan dilakukan tanpa kontak fisik.                                           |

2.4 Dependensi
| ID     | Dependensi                                                                                                                             |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| DEP-01 | Sistem bergantung pada ketersediaan akses kamera untuk melakukan deteksi real-time.                                                    |
| DEP-02 | Kemampuan AI bergantung pada model CNN berbasis MobileNet sebagaimana digunakan dalam bukti riset.                                     |
| DEP-03 | Pengukuran kualitas AI bergantung pada data pengujian yang dapat digunakan untuk membandingkan hasil prediksi dengan label yang benar. |

3. Functional Requirements
Prioritas: Must = wajib, Should = penting tetapi dapat menyusul, Could = tambahan.
| ID    | Requirement                                                                                                                                                        | Prioritas | Metode Verifikasi            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------------------- |
| FR-01 | Sistem harus dapat mendeteksi wajah dari live feed kamera saat kamera tersedia → menghasilkan lokasi/hasil wajah terdeteksi untuk proses klasifikasi berikutnya.   | Must      | Pengujian                    |
| FR-02 | Sistem harus dapat mengklasifikasikan status penggunaan masker pada wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan status pakai/tidak pakai masker. | Must      | Pengujian akurasi            |
| FR-03 | Sistem harus dapat memprediksi jenis kelamin dari wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan hasil klasifikasi jenis kelamin.                   | Should    | Pengujian akurasi            |
| FR-04 | Sistem harus dapat mengestimasi rentang usia dari wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan estimasi rentang usia.                             | Should    | Pengujian akurasi            |
| FR-05 | Sistem harus dapat menampilkan hasil deteksi secara real-time saat proses deteksi berlangsung → petugas memperoleh informasi hasil klasifikasi.                    | Must      | Pengujian fungsional         |
| FR-06 | Sistem harus dapat menyimpan log hasil deteksi saat hasil klasifikasi diperoleh → tersimpan timestamp, status masker, dan data demografis.                         | Must      | Pengujian database/log       |
| FR-07 | Sistem harus dapat menampilkan ringkasan data deteksi saat data hasil klasifikasi tersedia → menghasilkan data agregat kepatuhan dan demografis.                   | Should    | Pengujian fungsional         |
| FR-08 | Sistem harus dapat menampilkan pesan kesalahan saat akses kamera gagal → petugas mengetahui bahwa kamera tidak dapat digunakan.                                    | Must      | Pengujian skenario kegagalan |
| FR-09 | Sistem dapat memfilter data hasil deteksi berdasarkan periode saat fitur laporan digunakan → menghasilkan data sesuai periode yang dipilih.                        | Could     | Pengujian fungsional         |
| FR-10 | Sistem dapat menampilkan visualisasi statistik saat data agregat tersedia → menghasilkan representasi statistik kepatuhan.                                         | Could     | Pengujian fungsional         |

FR-09 dan FR-10 berasal dari fitur Could Have pada PRD sehingga bukan persyaratan inti prototype.

4. Non-Functional Requirements
Acuan kualitas: ISO/IEC 25010.
| ID     | Kategori ISO/IEC 25010 | Requirement                                                                                                          | Metrik                                             | Target                | Kondisi Ukur                                                    |
| ------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------- | --------------------------------------------------------------- |
| NFR-01 | Performance efficiency | Sistem harus menghasilkan klasifikasi status masker dengan tingkat akurasi yang memenuhi target.                     | Accuracy                                           | ≥95%                  | Pengujian menggunakan data berlabel                             |
| NFR-02 | Performance efficiency | Sistem harus menghasilkan deteksi dan prediksi dalam waktu yang ditetapkan.                                          | Latensi per wajah                                  | <1 detik/wajah        | Diukur sejak wajah terdeteksi hingga hasil klasifikasi tersedia |
| NFR-03 | Usability              | Sistem harus dapat dipahami oleh petugas tanpa pelatihan khusus.                                                     | Waktu pemahaman penggunaan                         | ≤5 menit              | Uji penggunaan oleh target user                                 |
| NFR-04 | Reliability            | Sistem harus memberikan informasi ketika kamera tidak dapat diakses dan tidak mengalami crash pada kondisi tersebut. | Keberhasilan penanganan error                      | 100% kasus pengujian  | Pengujian dengan skenario kamera gagal                          |
| NFR-05 | Security/Privacy       | Sistem tidak boleh menyimpan gambar wajah mentah secara permanen.                                                    | Jumlah gambar wajah mentah yang tersimpan permanen | 0                     | Pemeriksaan data setelah proses deteksi                         |
| NFR-06 | Privacy                | Data yang dicatat harus berupa hasil klasifikasi sesuai kebutuhan sistem, bukan gambar wajah mentah.                 | Kepatuhan jenis data tersimpan                     | 100% sesuai ketentuan | Audit terhadap log hasil deteksi                                |

Catatan: PRD tidak memberikan target kuantitatif tambahan untuk keamanan selain kebutuhan privasi, sehingga SRS tidak menetapkan target keamanan teknis lain.

5. Kebutuhan Data Minimum Fitur AI
| Fitur AI                 | Input            | Output Model                              |
| ------------------------ | ---------------- | ----------------------------------------- |
| ★ Deteksi wajah          | Live feed kamera | Wajah terdeteksi                          |
| ★ Klasifikasi masker     | Wajah terdeteksi | Status: pakai masker / tidak pakai masker |
| ★ Prediksi jenis kelamin | Wajah terdeteksi | Hasil klasifikasi jenis kelamin           |
| ★ Estimasi usia          | Wajah terdeteksi | Estimasi rentang usia                     |

Data yang Dicatat
Berdasarkan FR-06, sistem mencatat minimum:
* Timestamp
* Status masker
* Jenis kelamin
* Estimasi rentang usia
Gambar wajah mentah tidak disimpan permanen.

6. Aturan Bisnis Hasil Riset
BR-01 — Kriteria Kepatuhan Masker
Hasil klasifikasi status masker menjadi dasar sistem untuk menentukan apakah wajah yang terdeteksi menggunakan atau tidak menggunakan masker.
BR-02 — Target Akurasi
Hasil deteksi masker pada prototype harus mencapai akurasi minimal 95%, sesuai KPI dan NFR.
BR-03 — Target Latensi
Proses deteksi dan prediksi harus menghasilkan respons kurang dari 1 detik per wajah.
BR-04 — Hasil Demografis
Jenis kelamin dan usia digunakan sebagai hasil klasifikasi/estimasi untuk kebutuhan analisis, bukan sebagai identitas individu.
BR-05 — Privasi Data
Gambar wajah mentah tidak disimpan secara permanen. Data yang dipertahankan berupa hasil klasifikasi yang dibutuhkan untuk pemantauan dan pelaporan.
BR-06 — Bukti Performa Penelitian
Riset Sopian, Setiadi, & Agustino (2024) yang dicantumkan dalam PRD melaporkan:
* Akurasi deteksi masker: 99%
* Akurasi prediksi jenis kelamin dan usia: 98,75%
* Sensitivity: 98,5%
* Specificity: 99%
* Implementasi real-time dilaporkan memiliki latensi rendah dan responsivitas baik.
Nilai tersebut merupakan bukti riset/acuan, bukan jaminan bahwa prototype akan memperoleh performa identik. Performa prototype tetap harus diverifikasi melalui pengujian.

7. Matriks Traceability
| Requirement SRS | Fitur/Elemen PRD Terkait                 | Sumber          |
| --------------- | ---------------------------------------- | --------------- |
| FR-01           | ★ FR-01 Deteksi wajah                    | PRD Scope       |
| FR-02           | ★ FR-02 Deteksi status masker            | PRD Scope       |
| FR-03           | ★ FR-03 Prediksi jenis kelamin           | PRD Scope       |
| FR-04           | ★ FR-04 Estimasi usia                    | PRD Scope       |
| FR-05           | ★ FR-05 Dashboard real-time              | PRD Scope       |
| FR-06           | FR-06 Log deteksi                        | PRD Scope       |
| FR-07           | Ringkasan data                           | PRD Should Have |
| FR-08           | Error kamera                             | PRD Must Have   |
| FR-09           | Filter laporan                           | PRD Could Have  |
| FR-10           | Visualisasi statistik                    | PRD Could Have  |
| NFR-01          | KPI akurasi deteksi masker ≥95%          | PRD KPI         |
| NFR-02          | KPI latensi <1 detik/wajah               | PRD KPI         |
| NFR-03          | Usability ≤5 menit                       | PRD KPI/NFR     |
| NFR-04          | Error handling 100%                      | PRD KPI/NFR     |
| NFR-05          | 0 gambar wajah mentah tersimpan permanen | PRD KPI/NFR     |
| NFR-06          | Privasi data hasil klasifikasi           | PRD NFR-03      |
| BR-01           | Status masker pakai/tidak                | FR-02           |
| BR-02           | Akurasi ≥95%                             | NFR-01          |
| BR-03           | Latensi <1 detik                         | NFR-02          |
| BR-04           | Data jenis kelamin & usia                | FR-03, FR-04    |
| BR-05           | Tidak menyimpan gambar wajah mentah      | NFR-05/NFR-06   |
| BR-06           | Hasil riset MobileNet/CNN                | Bukti riset PRD |

Kesimpulan SRS
SRS ini mempertahankan batasan PRD: fokus pada kebutuhan dan perilaku sistem, bukan bagaimana sistem dibangun. Karena itu, detail seperti struktur backend, arsitektur, API, database schema, pemilihan library, desain UI, dan konfigurasi model belum dimasukkan dan seharusnya dibahas pada dokumen HLD/LLD.

User stories/AC P3:
DRAF USER STORIES
Sistem Pemantau Kepatuhan Masker Berbasis AI

User story berikut hanya diturunkan dari fitur Must Have dan Should Have pada SRS. Setiap story memiliki keterlacakan langsung ke minimal satu Functional Requirement.

Epik 1 — Deteksi Wajah dan Kepatuhan Masker
US-01 — Deteksi Wajah
Sebagai petugas keamanan/resepsionis,
Saya ingin sistem mendeteksi wajah dari kamera secara real-time,
Sehingga saya dapat memantau pengunjung secara otomatis tanpa melakukan pemeriksaan satu per satu.
* Prioritas: Must Have
* Keterlacakan: FR-01, NFR-02

US-02 — Klasifikasi Status Masker
Sebagai petugas keamanan/resepsionis,
Saya ingin sistem mengklasifikasikan apakah wajah terdeteksi menggunakan atau tidak menggunakan masker,
Sehingga saya dapat mengetahui kepatuhan penggunaan masker secara cepat.
* Prioritas: Must Have
* Keterlacakan: FR-02, NFR-01, NFR-02

US-03 — Hasil Deteksi Real-Time
Sebagai petugas keamanan/resepsionis,
Saya ingin melihat hasil deteksi secara real-time,
Sehingga saya dapat segera mengetahui status masker pengunjung.
* Prioritas: Must Have
* Keterlacakan: FR-05, NFR-02, NFR-03

Epik 2 — Prediksi Demografis Pengunjung
US-04 — Prediksi Jenis Kelamin
Sebagai manajemen gedung,
Saya ingin sistem menghasilkan klasifikasi jenis kelamin dari wajah yang terdeteksi,
Sehingga saya dapat memperoleh data demografis agregat untuk kebutuhan analisis.
* Prioritas: Should Have
* Keterlacakan: FR-03, NFR-02

US-05 — Estimasi Rentang Usia
Sebagai manajemen gedung,
Saya ingin sistem menghasilkan estimasi rentang usia dari wajah yang terdeteksi,
Sehingga saya dapat memperoleh informasi demografis agregat untuk kebutuhan analisis.
* Prioritas: Should Have
* Keterlacakan: FR-04, NFR-02

Catatan: hasil jenis kelamin dan usia merupakan klasifikasi/estimasi, bukan identitas individu, sesuai BR-04.

Epik 3 — Pencatatan Hasil Deteksi
US-06 — Pencatatan Otomatis
Sebagai petugas keamanan/resepsionis,
Saya ingin hasil deteksi dicatat secara otomatis,
Sehingga saya tidak perlu melakukan pencatatan pengunjung secara manual.
* Prioritas: Must Have
* Keterlacakan: FR-06, NFR-06

US-07 — Data Log Deteksi
Sebagai manajemen gedung,
Saya ingin log deteksi menyimpan timestamp, status masker, jenis kelamin, dan estimasi rentang usia,
Sehingga saya dapat menggunakan data tersebut untuk pemantauan dan pelaporan agregat.
* Prioritas: Must Have
* Keterlacakan: FR-06, NFR-05, NFR-06

Epik 4 — Informasi Agregat
US-08 — Ringkasan Data Deteksi
Sebagai manajemen gedung,
Saya ingin melihat ringkasan data hasil deteksi dan data demografis,
Sehingga saya dapat mengetahui kondisi kepatuhan masker dan karakteristik demografis pengunjung secara agregat.
* Prioritas: Should Have
* Keterlacakan: FR-07, NFR-03

Epik 5 — Penanganan Kegagalan Kamera
US-09 — Informasi Kamera Gagal
Sebagai petugas keamanan/resepsionis,
Saya ingin sistem memberikan pesan ketika kamera gagal diakses,
Sehingga saya mengetahui bahwa proses pemantauan tidak dapat dilakukan melalui kamera.
* Prioritas: Must Have
* Keterlacakan: FR-08, NFR-04

US-10 — Sistem Tetap Stabil Saat Kamera Gagal
Sebagai petugas keamanan/resepsionis,
Saya ingin sistem tidak mengalami crash ketika kamera gagal diakses,
Sehingga saya dapat mengetahui masalah kamera melalui informasi kesalahan yang diberikan sistem.
* Prioritas: Must Have
* Keterlacakan: FR-08, NFR-04

Ringkasan Backlog User Stories
| ID    | Epik                   | User Story                | Prioritas | Traceability          |
| ----- | ---------------------- | ------------------------- | --------- | --------------------- |
| US-01 | Deteksi Wajah & Masker | Deteksi wajah real-time   | Must      | FR-01, NFR-02         |
| US-02 | Deteksi Wajah & Masker | Klasifikasi status masker | Must      | FR-02, NFR-01, NFR-02 |
| US-03 | Deteksi Wajah & Masker | Melihat hasil real-time   | Must      | FR-05, NFR-02, NFR-03 |
| US-04 | Demografis             | Prediksi jenis kelamin    | Should    | FR-03, NFR-02         |
| US-05 | Demografis             | Estimasi rentang usia     | Should    | FR-04, NFR-02         |
| US-06 | Pencatatan             | Pencatatan otomatis       | Must      | FR-06, NFR-06         |
| US-07 | Pencatatan             | Penyimpanan data log      | Must      | FR-06, NFR-05, NFR-06 |
| US-08 | Agregasi               | Ringkasan data deteksi    | Should    | FR-07, NFR-03         |
| US-09 | Kamera                 | Pesan kamera gagal        | Must      | FR-08, NFR-04         |
| US-10 | Kamera                 | Stabil saat kamera gagal  | Must      | FR-08, NFR-04         |

Catatan Scope
FR-09 (filter laporan) dan FR-10 (visualisasi statistik) tidak dibuat menjadi user story karena keduanya berstatus Could Have, sesuai aturan tugas.
Dengan demikian, backlog inti terdiri dari 10 user stories yang mencakup seluruh FR Must Have dan Should Have dari SRS tanpa menambahkan kebutuhan baru.

[Format output]
1) Diagram arsitektur (Mermaid/ASCII): client → backend API → AI service → data store → layanan eksternal (bila ada);
2) Deskripsi komponen: peran, tanggung jawab, teknologi usulan. Untuk keputusan penting (mis. AI on-device vs cloud API) sajikan tabel trade-off: akurasi, latensi, biaya, privasi, effort, lalu beri rekomendasi;
3) Aliran data end-to-end fitur AI: input → preprocessing → inference → postprocessing → output → penyimpanan, termasuk titik fallback saat model gagal;
4) Kontrak antarkomponen tingkat tinggi: API utama, format data, pemicu/event;
5) Penempatan security & privacy by design: auth, enkripsi, data sensitif, logging;
6) Lingkungan deployment ringkas (development/staging/production).

[Aturan]
- Desain hanya dari FR/NFR yang ada; jangan menambah fitur. Gap apa pun → [ASUMSI-XX].
- Jangan masuk detail class/method/query (itu LLD).
- Setiap keputusan besar diberi alasan 1-2 kalimat + alternatif.

[Peran]
Kamu adalah software engineer senior (sesuai stack tim).

[Tugas]
Buat DRAF LLD untuk fitur prioritas Must pada SRS berdasarkan HLD hasil revisi.

[Konteks]
Stack & pola :
- Frontend : React / Next.js
- Backend  : Python FastAPI
- AI       : OpenCV + CNN berbasis MobileNet (TensorFlow / ONNX)
- Database : PostgreSQL atau SQLite
- Pola     : Clean Architecture (layer: Presentation → Application → Domain → Infrastructure)

SRS hasil revisi :
DRAF SRS Ringkas
Sistem Pemantau Kepatuhan Masker Berbasis AI

1. Tujuan, Scope, dan Definisi Istilah
1.1 Tujuan
Sistem bertujuan menyediakan pemantauan kepatuhan penggunaan masker secara real-time melalui kamera sehingga petugas keamanan/resepsionis dapat melakukan verifikasi secara lebih cepat dibandingkan pemeriksaan manual.
Sistem juga menghasilkan klasifikasi jenis kelamin dan estimasi rentang usia untuk mendukung kebutuhan data agregat manajemen gedung.

1.2 Scope Sistem
Dalam scope:
* Deteksi wajah dari live feed kamera.
* Klasifikasi status penggunaan masker.
* Prediksi jenis kelamin.
* Estimasi rentang usia.
* Penyajian hasil deteksi secara real-time.
* Pencatatan hasil deteksi.
* Ringkasan data agregat.
* Penanganan kegagalan akses kamera.

Di luar scope:
* Identifikasi nama/identitas individu.
* Pengenalan wajah individu.
* Penyimpanan permanen gambar wajah mentah.
* Pemberian sanksi otomatis.
* Sistem keamanan gedung secara keseluruhan.

1.3 Definisi Istilah
| Istilah         | Definisi                                                                                 |
| --------------- | ---------------------------------------------------------------------------------------- |
| AI              | Kemampuan sistem melakukan klasifikasi/prediksi berdasarkan data visual.                 |
| Computer Vision | Pemrosesan informasi visual dari kamera untuk memperoleh hasil deteksi atau klasifikasi. |
| Deteksi wajah   | Proses menemukan wajah pada input kamera.                                                |
| Status masker   | Klasifikasi apakah wajah menggunakan atau tidak menggunakan masker.                      |
| Jenis kelamin   | Hasil klasifikasi jenis kelamin dari wajah terdeteksi.                                   |
| Estimasi usia   | Perkiraan usia dalam bentuk rentang usia.                                                |
| Live feed       | Input gambar/video yang diperoleh secara langsung dari kamera.                           |
| Log deteksi     | Catatan hasil deteksi yang mencakup timestamp, status masker, dan data demografis.       |

2. User, Stakeholder, Lingkungan Operasi, Asumsi & Dependensi
2.1 User dan Stakeholder
| Aktor                        | Peran           | Kebutuhan                                                                 |
| ---------------------------- | --------------- | ------------------------------------------------------------------------- |
| Petugas keamanan/resepsionis | Pengguna utama  | Memantau status masker secara cepat dan real-time                         |
| Manajemen gedung             | Pengguna data   | Memperoleh data agregat kepatuhan dan demografis                          |
| Pengunjung                   | Pihak terdampak | Pemantauan tanpa kontak fisik dan tanpa penyimpanan permanen gambar wajah |

2.2 Lingkungan Operasi
Sistem digunakan pada:
* Platform website.
* Lokasi publik seperti gedung perkantoran, mall, atau fasilitas kesehatan.
* Lingkungan dengan akses kamera.
* Kondisi lalu lintas pengunjung yang dapat mencapai ratusan orang per hari.
Detail perangkat keras, jaringan, sistem operasi, dan spesifikasi infrastruktur belum ditentukan dalam PRD sehingga tidak menjadi kebutuhan SRS.

2.3 Asumsi
| ID    | Asumsi                                                                             |
| ----- | ---------------------------------------------------------------------------------- |
| AS-01 | Perangkat yang digunakan memiliki akses kamera.                                    |
| AS-02 | Kondisi kamera memungkinkan wajah terdeteksi.                                      |
| AS-03 | Data klasifikasi dapat memenuhi kebutuhan pelaporan tanpa menyimpan gambar mentah. |
| AS-04 | Rentang usia dapat ditentukan untuk kebutuhan prototype.                           |
| AS-05 | Pemantauan dilakukan tanpa kontak fisik.                                           |

2.4 Dependensi
| ID     | Dependensi                                                                                                                             |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| DEP-01 | Sistem bergantung pada ketersediaan akses kamera untuk melakukan deteksi real-time.                                                    |
| DEP-02 | Kemampuan AI bergantung pada model CNN berbasis MobileNet sebagaimana digunakan dalam bukti riset.                                     |
| DEP-03 | Pengukuran kualitas AI bergantung pada data pengujian yang dapat digunakan untuk membandingkan hasil prediksi dengan label yang benar. |

3. Functional Requirements
Prioritas: Must = wajib, Should = penting tetapi dapat menyusul, Could = tambahan.
| ID    | Requirement                                                                                                                                                        | Prioritas | Metode Verifikasi            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- | ---------------------------- |
| FR-01 | Sistem harus dapat mendeteksi wajah dari live feed kamera saat kamera tersedia → menghasilkan lokasi/hasil wajah terdeteksi untuk proses klasifikasi berikutnya.   | Must      | Pengujian                    |
| FR-02 | Sistem harus dapat mengklasifikasikan status penggunaan masker pada wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan status pakai/tidak pakai masker. | Must      | Pengujian akurasi            |
| FR-03 | Sistem harus dapat memprediksi jenis kelamin dari wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan hasil klasifikasi jenis kelamin.                   | Should    | Pengujian akurasi            |
| FR-04 | Sistem harus dapat mengestimasi rentang usia dari wajah terdeteksi saat wajah berhasil dideteksi → menghasilkan estimasi rentang usia.                             | Should    | Pengujian akurasi            |
| FR-05 | Sistem harus dapat menampilkan hasil deteksi secara real-time saat proses deteksi berlangsung → petugas memperoleh informasi hasil klasifikasi.                    | Must      | Pengujian fungsional         |
| FR-06 | Sistem harus dapat menyimpan log hasil deteksi saat hasil klasifikasi diperoleh → tersimpan timestamp, status masker, dan data demografis.                         | Must      | Pengujian database/log       |
| FR-07 | Sistem harus dapat menampilkan ringkasan data deteksi saat data hasil klasifikasi tersedia → menghasilkan data agregat kepatuhan dan demografis.                   | Should    | Pengujian fungsional         |
| FR-08 | Sistem harus dapat menampilkan pesan kesalahan saat akses kamera gagal → petugas mengetahui bahwa kamera tidak dapat digunakan.                                    | Must      | Pengujian skenario kegagalan |
| FR-09 | Sistem dapat memfilter data hasil deteksi berdasarkan periode saat fitur laporan digunakan → menghasilkan data sesuai periode yang dipilih.                        | Could     | Pengujian fungsional         |
| FR-10 | Sistem dapat menampilkan visualisasi statistik saat data agregat tersedia → menghasilkan representasi statistik kepatuhan.                                         | Could     | Pengujian fungsional         |

FR-09 dan FR-10 berasal dari fitur Could Have pada PRD sehingga bukan persyaratan inti prototype.

4. Non-Functional Requirements
Acuan kualitas: ISO/IEC 25010.
| ID     | Kategori ISO/IEC 25010 | Requirement                                                                                                          | Metrik                                             | Target                | Kondisi Ukur                                                    |
| ------ | ---------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------- | --------------------------------------------------------------- |
| NFR-01 | Performance efficiency | Sistem harus menghasilkan klasifikasi status masker dengan tingkat akurasi yang memenuhi target.                     | Accuracy                                           | ≥95%                  | Pengujian menggunakan data berlabel                             |
| NFR-02 | Performance efficiency | Sistem harus menghasilkan deteksi dan prediksi dalam waktu yang ditetapkan.                                          | Latensi per wajah                                  | <1 detik/wajah        | Diukur sejak wajah terdeteksi hingga hasil klasifikasi tersedia |
| NFR-03 | Usability              | Sistem harus dapat dipahami oleh petugas tanpa pelatihan khusus.                                                     | Waktu pemahaman penggunaan                         | ≤5 menit              | Uji penggunaan oleh target user                                 |
| NFR-04 | Reliability            | Sistem harus memberikan informasi ketika kamera tidak dapat diakses dan tidak mengalami crash pada kondisi tersebut. | Keberhasilan penanganan error                      | 100% kasus pengujian  | Pengujian dengan skenario kamera gagal                          |
| NFR-05 | Security/Privacy       | Sistem tidak boleh menyimpan gambar wajah mentah secara permanen.                                                    | Jumlah gambar wajah mentah yang tersimpan permanen | 0                     | Pemeriksaan data setelah proses deteksi                         |
| NFR-06 | Privacy                | Data yang dicatat harus berupa hasil klasifikasi sesuai kebutuhan sistem, bukan gambar wajah mentah.                 | Kepatuhan jenis data tersimpan                     | 100% sesuai ketentuan | Audit terhadap log hasil deteksi                                |

Catatan: PRD tidak memberikan target kuantitatif tambahan untuk keamanan selain kebutuhan privasi, sehingga SRS tidak menetapkan target keamanan teknis lain.

5. Kebutuhan Data Minimum Fitur AI
| Fitur AI                 | Input            | Output Model                              |
| ------------------------ | ---------------- | ----------------------------------------- |
| ★ Deteksi wajah          | Live feed kamera | Wajah terdeteksi                          |
| ★ Klasifikasi masker     | Wajah terdeteksi | Status: pakai masker / tidak pakai masker |
| ★ Prediksi jenis kelamin | Wajah terdeteksi | Hasil klasifikasi jenis kelamin           |
| ★ Estimasi usia          | Wajah terdeteksi | Estimasi rentang usia                     |

Data yang Dicatat
Berdasarkan FR-06, sistem mencatat minimum:
* Timestamp
* Status masker
* Jenis kelamin
* Estimasi rentang usia
Gambar wajah mentah tidak disimpan permanen.

6. Aturan Bisnis Hasil Riset
BR-01 — Kriteria Kepatuhan Masker
Hasil klasifikasi status masker menjadi dasar sistem untuk menentukan apakah wajah yang terdeteksi menggunakan atau tidak menggunakan masker.
BR-02 — Target Akurasi
Hasil deteksi masker pada prototype harus mencapai akurasi minimal 95%, sesuai KPI dan NFR.
BR-03 — Target Latensi
Proses deteksi dan prediksi harus menghasilkan respons kurang dari 1 detik per wajah.
BR-04 — Hasil Demografis
Jenis kelamin dan usia digunakan sebagai hasil klasifikasi/estimasi untuk kebutuhan analisis, bukan sebagai identitas individu.
BR-05 — Privasi Data
Gambar wajah mentah tidak disimpan secara permanen. Data yang dipertahankan berupa hasil klasifikasi yang dibutuhkan untuk pemantauan dan pelaporan.
BR-06 — Bukti Performa Penelitian
Riset Sopian, Setiadi, & Agustino (2024) yang dicantumkan dalam PRD melaporkan:
* Akurasi deteksi masker: 99%
* Akurasi prediksi jenis kelamin dan usia: 98,75%
* Sensitivity: 98,5%
* Specificity: 99%
* Implementasi real-time dilaporkan memiliki latensi rendah dan responsivitas baik.
Nilai tersebut merupakan bukti riset/acuan, bukan jaminan bahwa prototype akan memperoleh performa identik. Performa prototype tetap harus diverifikasi melalui pengujian.

7. Matriks Traceability
| Requirement SRS | Fitur/Elemen PRD Terkait                 | Sumber          |
| --------------- | ---------------------------------------- | --------------- |
| FR-01           | ★ FR-01 Deteksi wajah                    | PRD Scope       |
| FR-02           | ★ FR-02 Deteksi status masker            | PRD Scope       |
| FR-03           | ★ FR-03 Prediksi jenis kelamin           | PRD Scope       |
| FR-04           | ★ FR-04 Estimasi usia                    | PRD Scope       |
| FR-05           | ★ FR-05 Dashboard real-time              | PRD Scope       |
| FR-06           | FR-06 Log deteksi                        | PRD Scope       |
| FR-07           | Ringkasan data                           | PRD Should Have |
| FR-08           | Error kamera                             | PRD Must Have   |
| FR-09           | Filter laporan                           | PRD Could Have  |
| FR-10           | Visualisasi statistik                    | PRD Could Have  |
| NFR-01          | KPI akurasi deteksi masker ≥95%          | PRD KPI         |
| NFR-02          | KPI latensi <1 detik/wajah               | PRD KPI         |
| NFR-03          | Usability ≤5 menit                       | PRD KPI/NFR     |
| NFR-04          | Error handling 100%                      | PRD KPI/NFR     |
| NFR-05          | 0 gambar wajah mentah tersimpan permanen | PRD KPI/NFR     |
| NFR-06          | Privasi data hasil klasifikasi           | PRD NFR-03      |
| BR-01           | Status masker pakai/tidak                | FR-02           |
| BR-02           | Akurasi ≥95%                             | NFR-01          |
| BR-03           | Latensi <1 detik                         | NFR-02          |
| BR-04           | Data jenis kelamin & usia                | FR-03, FR-04    |
| BR-05           | Tidak menyimpan gambar wajah mentah      | NFR-05/NFR-06   |
| BR-06           | Hasil riset MobileNet/CNN                | Bukti riset PRD |

Kesimpulan SRS
SRS ini mempertahankan batasan PRD: fokus pada kebutuhan dan perilaku sistem, bukan bagaimana sistem dibangun. Karena itu, detail seperti struktur backend, arsitektur, API, database schema, pemilihan library, desain UI, dan konfigurasi model belum dimasukkan dan seharusnya dibahas pada dokumen HLD/LLD.

HLD hasil revisi :
DRAF HLD (HIGH-LEVEL DESIGN)
Sistem Pemantau Kepatuhan Masker Berbasis AI

1. Tujuan dan Ruang Lingkup HLD
HLD ini mendefinisikan rancangan arsitektur tingkat tinggi untuk sistem Sistem Pemantau Kepatuhan Masker Berbasis AI berbasis website.
Sistem dirancang untuk mendukung:
* deteksi wajah dari live feed kamera;
* klasifikasi status penggunaan masker;
* prediksi jenis kelamin;
* estimasi rentang usia;
* penayangan hasil secara real-time;
* pencatatan hasil deteksi;
* penyajian ringkasan data agregat;
* penanganan kegagalan akses kamera.
HLD tidak membahas detail class, method, query database, atau implementasi kode karena aspek tersebut termasuk LLD. Scope ini mengikuti FR/NFR pada SRS.

2. Gambaran Arsitektur Sistem
Arsitektur menggunakan pendekatan client–backend–AI service–data store.

flowchart LR
    U[Petugas Keamanan / Resepsionis]
    subgraph CLIENT[Web Client]
        UI[React / Next.js]
        CAM[WebRTC / MediaDevices API]
    end
    subgraph BACKEND[Backend]
        API[FastAPI API]
        FH[Error Handling & Fallback]
    end
    subgraph AI[AI Service]
        FD[Face Detection<br/>CNN / MobileNet]
        MC[Mask Classification<br/>CNN Classifier]
        DI[Demographic Inference<br/>Gender & Age]
    end
    subgraph DATA[Data Store]
        DB[(PostgreSQL / SQLite)]
    end
    U --> UI
    UI --> CAM
    CAM --> API
    API --> FD
    FD --> MC
    FD --> DI
    MC --> API
    DI --> API
    API --> UI
    API --> DB
    API --> FH
    FH --> UI

Arsitektur tersebut mempertahankan pemisahan antara antarmuka website, backend API, layanan AI, dan penyimpanan data. Komponen AI utama menggunakan OpenCV serta model CNN berbasis MobileNet sebagaimana menjadi dependensi pada SRS.

3. Deskripsi Komponen
| Komponen                      | Peran                | Tanggung Jawab                                                                          | Teknologi Usulan            |
| ----------------------------- | -------------------- | --------------------------------------------------------------------------------------- | --------------------------- |
| Web Client                    | Antarmuka pengguna   | Menampilkan live feed, hasil deteksi, status sistem, dan informasi agregat              | React / Next.js             |
| Camera Interface              | Sumber input visual  | Mengakses kamera perangkat dan menyediakan live stream                                  | WebRTC / MediaDevices API   |
| Backend API                   | Penghubung sistem    | Menerima input/proses dari client, mengoordinasikan AI, logging, dan response ke client | Python FastAPI              |
| Face Detection Service        | Deteksi wajah        | Menemukan lokasi wajah dari frame kamera                                                | OpenCV + CNN/MobileNet      |
| Mask Classification Service   | Klasifikasi masker   | Mengklasifikasikan status masker pada wajah terdeteksi                                  | CNN Classifier              |
| Demographic Inference Service | Data demografis      | Menghasilkan klasifikasi jenis kelamin dan estimasi rentang usia                        | Model AI Computer Vision    |
| Logging Service               | Pencatatan           | Menyimpan timestamp, status masker, dan data demografis                                 | FastAPI + PostgreSQL/SQLite |
| Error Handling & Fallback     | Penanganan kegagalan | Menangani kamera gagal, stream terputus, dan kegagalan proses AI                        | FastAPI + React/Next.js     |
| Database                      | Penyimpanan data     | Menyimpan hasil klasifikasi/log yang diperlukan sistem                                  | PostgreSQL / SQLite         |

4. Keputusan Arsitektur AI
Rekomendasi: AI Service berbasis Python/OpenCV pada backend.
Alasannya, stack yang diberikan menetapkan Python FastAPI sebagai backend dan OpenCV + TensorFlow/MobileNet sebagai AI service. Penggunaan model terpusat memudahkan pengujian terhadap target akurasi dan latency.
[ASUMSI-01] Infrastruktur deployment yang dipilih mampu menjalankan inference model dalam batas latency yang dipersyaratkan.

5. Aliran Data End-to-End
Input (Camera Live Feed) → Preprocessing → Face Detection → Mask Classification → Demographic Inference → Postprocessing → Output Real-time → Logging → Database.
Fallback: jika AI gagal atau kamera gagal → tampilkan pesan error tanpa crash.

6. Fallback dan Error Handling
Sistem harus menangani:
- Kamera tidak ditemukan
- Permission kamera ditolak
- Kamera terputus
- Face detection gagal
- Mask classification gagal
- Backend/AI timeout
Target NFR-04: 100% kasus pengujian kegagalan kamera ditangani tanpa crash.

7. Kontrak Antarkomponen Tingkat Tinggi
Client → Backend : POST /api/detection
Backend → AI Service : Face Detection → Mask Classification → Demographic Inference
Backend → Database : menyimpan timestamp, status_masker, jenis_kelamin, rentang_usia (tanpa raw image)

8. Target Performance
| Parameter                         | Target         |
| --------------------------------- | -------------- |
| Akurasi klasifikasi masker        | ≥95%           |
| Latensi deteksi/prediksi          | <1 detik/wajah |
| Penanganan kegagalan kamera       | 100% kasus     |
| Raw face image tersimpan permanen | 0              |

9. Security & Privacy by Design
- Tidak menyimpan gambar wajah mentah secara permanen (NFR-05, NFR-06, BR-05).
- Data yang disimpan hanya hasil klasifikasi.
- Komunikasi menggunakan HTTPS (diasumsikan pada deployment).

10. Logging dan Data Store
Hanya menyimpan:
timestamp, status_masker, jenis_kelamin, rentang_usia.

11. Deployment Environment
Development : lokal (React + FastAPI + OpenCV + PostgreSQL/SQLite)
Staging & Production/Demo : Vercel (frontend) + Render/Railway (backend + AI) + PostgreSQL

[Format output]
1) Desain modul/class 2-3 fitur Must terpenting (termasuk fitur AI): tanggung jawab, atribut kunci, method utama;
2) Skema data: entitas, relasi, constraint (SQL/Prisma/ERD teks);
3) Spesifikasi API detail endpoint inti: method, path, request/response (contoh JSON), daftar kode error;
4) Sequence/alur detail fitur AI: validasi input → preprocessing → pemanggilan model/API → fallback → respons; sertakan skenario timeout & kegagalan model;
5) Rancangan error handling & fallback (retry, pesan ramah, mode offline);
6) Tabel traceability: elemen desain ↔ ID FR/NFR.

[Aturan]
- Turunkan dari SRS/HLD; DILARANG mengubah requirement.
- Hanya kerjakan fitur Must Have (FR-01, FR-02, FR-05, FR-06, FR-08).
- Pilihan yang belum diputuskan (library, dsb.): sarankan 2 opsi + kriteria pilih, lalu tulis [KEPUTUSAN TIM: ...] yang wajib diisi tim.
- Nama class/field bahasa Inggris; penjelasan Bahasa Indonesia.