# Analisis dan Implementasi Algoritma Edmonds-Karp (Maximum Flow)

Repositori ini berisi implementasi algoritma Edmonds-Karp dari awal (*from scratch*) untuk menghitung aliran maksimum (*Maximum Flow*) pada jaringan graf berarah. 

Proyek ini disusun sebagai bagian dari **Tugas Analisis Algoritma Komputasi, Magister Teknik Informatika (Semester Ganjil 2026)**.

**Disusun oleh:**  
- **Nama:** Muhammad Alwi  
- **NIM:** D082261023  

---

## 📌 Deskripsi Proyek
Algoritma Edmonds-Karp adalah spesifikasi dari metode Ford-Fulkerson yang menggunakan pencarian Breadth-First Search (BFS) untuk menemukan *augmenting path* terpendek. Penggunaan BFS menjamin bahwa kompleksitas waktu algoritma secara matematis terikat pada $\mathcal{O}(V \cdot E^2)$, membuatnya independen dari besaran nilai kapasitas aliran pada graf.

Proyek ini membuktikan kompleksitas tersebut melalui implementasi kode murni dan pengujian empiris (eksperimen).

## 📂 Struktur Repositori
- `edmonds_karp.py` : Kode sumber utama. Memuat logika BFS, iterasi algoritma Edmonds-Karp manual, skenario *test case* kecil, dan *script* eksperimen kinerja.
- `hasil_eksperimen.png` : Gambar grafik hasil perbandingan waktu eksekusi empiris dengan estimasi teoretis.
- `README.md` : Panduan dan dokumentasi repositori.

## 🛠️ Persyaratan Lingkungan (*Prerequisites*)
Kode inti algoritma (pencarian jalur dan kalkulasi graf sisa) berjalan murni tanpa pustaka eksternal. Namun, untuk keperluan modul eksperimen dan pembangkitan graf acak, diperlukan beberapa pustaka berikut:
- **Python 3.8+**
- **NetworkX** (sebagai generator graf dan pembanding validasi algoritma)
- **Matplotlib** (sebagai visualisator data ke dalam grafik)

**Langkah Instalasi Pustaka:**
Buka terminal/Command Prompt dan jalankan:
```bash
pip install networkx matplotlib
