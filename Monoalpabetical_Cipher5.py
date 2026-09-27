tabel_asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tabel_substitusi = "QWERTYUIOPASDFGHJKLZXCVBNM"

pesan = input("Masukkan pesan: ")

ciphertext = ""

for huruf in pesan.upper():
    if huruf in tabel_asli:
        posisi = tabel_asli.index(huruf)
        ciphertext += tabel_substitusi[posisi]
    else:
        ciphertext += huruf

print("Pesan asli :", pesan)
print("Hasil enkripsi :", ciphertext)