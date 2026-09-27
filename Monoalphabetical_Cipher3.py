ciphertext = "RQZQ"

tabel_asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tabel_substitusi = "QWERTYUIOPASDFGHJKLZXCVBNM"

plaintext = ""

for huruf in ciphertext:
    if huruf in tabel_substitusi:
        posisi = tabel_substitusi.index(huruf)
        plaintext += tabel_asli[posisi]
    else:
        plaintext += huruf

print("Ciphertext :", ciphertext)
print("Plaintext  :", plaintext)