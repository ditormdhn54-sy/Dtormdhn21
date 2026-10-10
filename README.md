# Sistem Pemantau Kepatuhan Masker Berbasis AI

Tugas mata kuliah Intelligent Mobile and Web Application Development.
Mahasiswa: Dito Ramadhan (2395114035)

## Struktur
- `requirements/` : PRD & SRS (Pertemuan 2)
- `functional/` : User Story & Use Case (Pertemuan 3)
- `docs/api`, `docs/db` : OpenAPI, API contract, ERD (Pertemuan 5)
- `docs/postman`, `docs/security`, `docs/prompt-log` : Postman collection, audit OWASP, log prompt (Pertemuan 5-6)
- `backend/` : source code FastAPI modular (Router -> Service -> Repository), JWT auth, patch anti-BOLA

## Menjalankan backend (Windows)
```powershell
cd backend
.\run.bat
```
`run.bat` otomatis: membuat venv, install library, menjalankan uji otomatis (`smoke_test.py`), lalu menyalakan server.
Dokumentasi interaktif: http://127.0.0.1:8000/docs

Tanpa konfigurasi apa pun aplikasi memakai SQLite (file `maskcare.db` dibuat otomatis).
Untuk PostgreSQL, isi `DATABASE_URL` di `backend/.env` (lihat `.env.example`) dan `pip install asyncpg`.

## Manual
```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python smoke_test.py
uvicorn app.main:app --reload
```
