# def kembalian_koin(koin, jumlah):
#     koin.sort(reverse= True) #Urutkan koin dari yang terbesar ke terkecil
#     hasil = []
#     for k in koin:
#         while jumlah >= k:
#             jumlah -= k
#             hasil.append(k)

#     if jumlah != 0 :
#         return None #Jika tidak bisa memberikan kembalian dengan koin yang ada 
    
#     return hasil

# koin =[100, 200, 500, 1000]
# jumlah = 2100

# print(kembalian_koin(koin, jumlah))



# Daftar aktivitas dengan prioritas (semakin kecil angkanya, semakin tinggi prioritasnya)
activities = [
    {"name": "Meeting with client", "priority": 1},
    {"name": "Write report", "priority": 2},
    {"name": "Check emails", "priority": 3},
    {"name": "Lunch", "priority": 4},
    {"name": "Team meeting", "priority": 1}
]

# Fungsi untuk menyusun jadwal berdasarkan prioritas
def schedule_activities(activities):
    # Urutkan aktivitas berdasarkan prioritas
    sorted_activities = sorted(activities, key=lambda x: x['priority'])
    
    # List untuk menyimpan jadwal
    schedule = []
    
    # Tambahkan aktivitas ke dalam jadwal sesuai urutan prioritas
    for activity in sorted_activities:
        schedule.append(activity['name'])
    
    return schedule

# Memanggil fungsi dan mencetak jadwal
daily_schedule = schedule_activities(activities)
print("Jadwal harian:", daily_schedule)
