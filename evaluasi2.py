def caesar(teks, key):
    hasil = ""

    for karakter in teks:
        if karakter.isalpha():
            posisi = ord(karakter.upper()) - ord('A')
            posisi_baru = (posisi + key) % 26
            hasil += chr(posisi_baru + ord('A'))
        else:
            hasil += karakter

    return hasil


pesan = input("Masukkan kode pengumuman: ")
key = int(input("Masukkan key: "))

ciphertext = caesar(pesan, key)

print("Hasil enkripsi:", ciphertext)