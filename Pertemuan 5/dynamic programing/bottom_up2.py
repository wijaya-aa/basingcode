def household_chores(chores):
    # chores adalah daftar tugas-tugas yang perlu dikerjakan
    compelte_chores = []
    for chore in chores:
        compelte_chores.append(chore)
        print(f"menyelesaikan : {chore}")
    return compelte_chores


# contoh pengunaan
chores = ['mencuci piring', 'menyapu lantai', 'mencuci baju', 'mengelap meja']

completed = household_chores(chores)
print(f"pekerjaan yang telah selesai: {completed}")