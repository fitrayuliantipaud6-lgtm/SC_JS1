import string

alfabet = string.ascii_uppercase
alfabet_rahasia = "QWERTYUIOPASDFGHJKLZXCVBNM"


def enkripsi(teks):
    hasil = ""

    for karakter in teks.upper():
        if karakter in alfabet:
            posisi = alfabet.index(karakter)
            hasil += alfabet_rahasia[posisi]
        else:
            hasil += karakter

    return hasil


def dekripsi(teks):
    hasil = ""

    for karakter in teks.upper():
        if karakter in alfabet_rahasia:
            posisi = alfabet_rahasia.index(karakter)
            hasil += alfabet[posisi]
        else:
            hasil += karakter

    return hasil


pesan = input("Masukkan pesan: ")

ciphertext = enkripsi(pesan)
plaintext = dekripsi(ciphertext)

print("Ciphertext :", ciphertext)
print("Dekripsi    :", plaintext)