import string

alfabet = string.ascii_uppercase
substitusi = alfabet[::-1]


def enkripsi(teks):
    hasil = ""

    for karakter in teks.upper():
        if karakter in alfabet:
            posisi = alfabet.index(karakter)
            hasil += substitusi[posisi]
        else:
            hasil += karakter

    return hasil


def dekripsi(teks):
    hasil = ""

    for karakter in teks.upper():
        if karakter in substitusi:
            posisi = substitusi.index(karakter)
            hasil += alfabet[posisi]
        else:
            hasil += karakter

    return hasil


pesan = input("Masukkan pesan: ")

ciphertext = enkripsi(pesan)
plaintext = dekripsi(ciphertext)

print("Ciphertext :", ciphertext)
print("Dekripsi    :", plaintext)