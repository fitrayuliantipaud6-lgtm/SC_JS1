def caesar_enkripsi(teks, key):
    hasil = ""

    for karakter in teks:
        if karakter.isalpha():
            posisi = ord(karakter.upper()) - ord('A')
            posisi_baru = (posisi + key) % 26
            hasil += chr(posisi_baru + ord('A'))
        else:
            hasil += karakter

    return hasil


def caesar_dekripsi(teks, key):
    return caesar_enkripsi(teks, -key)


pesan = input("Masukkan pesan: ")
key = int(input("Masukkan key: "))

ciphertext = caesar_enkripsi(pesan, key)
plaintext = caesar_dekripsi(ciphertext, key)

print("Ciphertext :", ciphertext)
print("Dekripsi    :", plaintext)