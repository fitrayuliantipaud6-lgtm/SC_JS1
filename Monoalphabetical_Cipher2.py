plaintext = "HALO TEMAN"

tabel_asli = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tabel_substitusi = "QWERTYUIOPASDFGHJKLZXCVBNM"

ciphertext = ""

for huruf in plaintext:
    if huruf in tabel_asli:
        posisi = tabel_asli.index(huruf)
        ciphertext += tabel_substitusi[posisi]
    else:
        ciphertext += huruf

print("Plaintext  :", plaintext)
print("Ciphertext :", ciphertext)