
# Fungsi untuk menyusun jadwal berdasarkan prioritas
def jadwal_kegiatan (kegiatan):
    # Urutkan aktivitas berdasarkan prioritas
    sortir_kegiatan = sorted(kegiatan, key=lambda x: x['kepentingan'])
    
    # List untuk menyimpan jadwal
    jadwal = []
    
    # Tambahkan aktivitas ke dalam jadwal sesuai urutan prioritas
    for aktivitas in sortir_kegiatan:
        jadwal.append(aktivitas['nama'])

    
    return jadwal


# Daftar aktivitas dengan prioritas (semakin kecil angkanya, semakin tinggi prioritasnya)
kegiatan = [
    {"nama": "Jalan Ke taman", "kepentingan": 1},
    {"nama": "Membuat Tugas", "kepentingan": 2},
    {"nama": "Datang ke Kampus", "kepentingan": 3},
    {"nama": "Makan", "kepentingan": 4},
]

# Memanggil fungsi dan mencetak jadwal
print(f"Daftar Kegiatan\n {kegiatan}\n\n")
jadwal_harian  = jadwal_kegiatan(kegiatan)
print(f"Jadwal Harian\n {jadwal_harian}")
