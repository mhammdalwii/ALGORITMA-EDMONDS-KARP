# Edmonds-Karp Max Flow Algorithm Analysis 

Repositori ini berisi implementasi algoritma Edmonds-Karp dari awal (*from scratch*) untuk menghitung aliran maksimum (*Maximum Flow*) pada graf berarah, sebagai bagian dari Tugas Analisis Algoritma Magister Teknik Informatika (Semester Ganjil 2026).

**Oleh:** Muhammad Alwi (NIM: D082261023)

## Struktur Repositori
- `edmonds_karp.py`: Kode program utama yang memuat implementasi inti algoritma Edmonds-Karp (tanpa menggunakan *library*), 3 kasus uji manual, serta fungsi eksperimen kinerja (pengujian runtime $O(V \cdot E^2)$).
- `hasil_eksperimen.png`: Plot grafik hasil dari skenario pengujian dengan berbagai ukuran input (*node* $V$ dari 50 hingga 800) berskala.

## Ketergantungan (Dependencies)
Kode inti algoritma berjalan murni pada **Python 3.x standar** menggunakan library bawaan (`collections.deque`, `time`, `random`, `statistics`). 
Library pihak ketiga di bawah ini **hanya digunakan sebagai pembanding performa dan visualisasi grafik**, bukan sebagai logika algoritma inti:
- `networkx`
- `matplotlib`

Untuk menginstalnya, jalankan perintah:
```bash
pip install networkx matplotlib
