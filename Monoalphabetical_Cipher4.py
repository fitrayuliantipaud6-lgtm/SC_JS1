plaintext = input("Masukkan plaintext: ")

tabel_asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tabel_substitusi = "QWERTYUIOPASDFGHJKLZXCVBNM"

# Enkripsi
ciphertext = ""

for huruf in plaintext.upper():
    if huruf in tabel_asli:
        posisi = tabel_asli.index(huruf)
        ciphertext += tabel_substitusi[posisi]
    else:
        ciphertext += huruf

print("Ciphertext :", ciphertext)


# Dekripsi
hasil_dekripsi = ""

for huruf in ciphertext:
    if huruf in tabel_substitusi:
        posisi = tabel_substitusi.index(huruf)
        hasil_dekripsi += tabel_asli[posisi]
    else:
        hasil_dekripsi += huruf

print("Dekripsi   :", hasil_dekripsi)