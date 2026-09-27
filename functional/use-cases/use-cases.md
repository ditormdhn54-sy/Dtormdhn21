Berikut 1 use case utama yang menggabungkan seluruh fitur **Must Have** dalam satu alur operasional yang dapat diuji.

# 1. Use Case Detail

| Atribut                 | Detail                                                                                                                                                                      |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID**                  | UC-01                                                                                                                                                                       |
| **Nama Use Case**       | Pemantauan Kepatuhan Masker Secara Real-Time                                                                                                                                |
| **Aktor Utama**         | Petugas keamanan/resepsionis                                                                                                                                                |
| **Tujuan**              | Memantau status penggunaan masker pengunjung secara otomatis melalui kamera dan mencatat hasil deteksi                                                                      |
| **Pre-kondisi**         | 1. Sistem website dapat diakses.<br>2. Perangkat memiliki kamera.<br>3. Petugas dapat menggunakan sistem.<br>4. Kamera memiliki kondisi yang memungkinkan wajah terdeteksi. |
| **Post-kondisi sukses** | Hasil deteksi wajah dan status masker ditampilkan secara real-time serta hasil deteksi dicatat sebagai log.                                                                 |
| **Post-kondisi gagal**  | Jika kamera tidak dapat diakses, sistem menampilkan pesan kesalahan dan tidak mengalami crash.                                                                              |

## Skenario Utama — Happy Flow

1. Petugas membuka sistem pemantauan pada website.
2. Petugas mengaktifkan akses kamera.
3. Sistem memeriksa ketersediaan kamera.
4. Sistem menerima **live feed** dari kamera.
5. Ketika wajah pengunjung masuk ke area kamera, sistem mendeteksi wajah.
6. Sistem melakukan klasifikasi status masker pada wajah yang terdeteksi.
7. Sistem menghasilkan salah satu status: **"Pakai Masker"** atau **"Tidak Pakai Masker"**.
8. Sistem menampilkan hasil deteksi secara real-time kepada petugas.
9. Sistem mencatat hasil deteksi secara otomatis.
10. Log minimal berisi **timestamp dan status masker** serta data demografis apabila tersedia sesuai kebutuhan sistem.
11. Proses pemantauan kembali dilakukan untuk wajah berikutnya tanpa memerlukan pencatatan manual oleh petugas.

---

# 2. Acceptance Criteria

## Skenario 1 — Deteksi dan Pencatatan Berhasil

**Given**

* Kamera tersedia dan dapat diakses oleh sistem.
* Terdapat satu wajah pengunjung yang masuk ke live feed.
* Kondisi kamera memungkinkan wajah terdeteksi.

**When**

* Sistem mendeteksi wajah dan melakukan klasifikasi status masker.

**Then**

* Wajah berhasil terdeteksi.
* Sistem menghasilkan status **"Pakai Masker"** atau **"Tidak Pakai Masker"**.
* Hasil deteksi ditampilkan kepada petugas dalam waktu **<1 detik per wajah**.
* Hasil deteksi dicatat secara otomatis.
* Log memiliki minimal **timestamp dan status masker**.
* Gambar wajah mentah **tidak disimpan secara permanen**.

**Traceability:** FR-01, FR-02, FR-05, FR-06, NFR-02, NFR-05, NFR-06.

---

## Skenario 2 — Kamera Gagal Diakses / Fallback

**Given**

* Petugas membuka fitur pemantauan.
* Perangkat tidak memberikan akses kamera atau kamera tidak tersedia.

**When**

* Sistem mencoba mengakses kamera.

**Then**

* Sistem mendeteksi bahwa kamera tidak dapat digunakan.
* Sistem menampilkan **pesan kesalahan yang jelas** kepada petugas.
* Sistem **tidak mengalami crash**.
* Sistem tidak menjalankan proses deteksi wajah ketika tidak terdapat live feed.
* Petugas tetap dapat mengetahui bahwa proses pemantauan belum dapat dilakukan.

**Target pengujian:** Penanganan kondisi kamera gagal harus berhasil pada **100% skenario pengujian kamera gagal**.

**Traceability:** FR-08, NFR-04.

---

### Ringkasan Kriteria Utama

| Parameter                 |                                      Kriteria |
| ------------------------- | --------------------------------------------: |
| Deteksi wajah             | Berhasil ketika wajah tersedia pada live feed |
| Status masker             |                    Pakai / Tidak Pakai Masker |
| Latensi hasil             |                            **<1 detik/wajah** |
| Pencatatan                |                                      Otomatis |
| Data minimal log          |                     Timestamp + status masker |
| Penyimpanan gambar mentah |                                **0 permanen** |
| Penanganan kamera gagal   |                      **100% kasus pengujian** |
| Sistem saat kamera gagal  |                                   Tidak crash |
