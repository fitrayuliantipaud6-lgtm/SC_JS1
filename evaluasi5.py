def vigenere_enkripsi(teks, key):
    hasil = ""
    indeks_key = 0

    for karakter in teks.upper():
        if karakter.isalpha():
            nilai_plaintext = ord(karakter) - ord('A')
            nilai_key = ord(key[indeks_key % len(key)]) - ord('A')

            nilai_cipher = (nilai_plaintext + nilai_key) % 26

            hasil += chr(nilai_cipher + ord('A'))
            indeks_key += 1
        else:
            hasil += karakter

    return hasil


def vigenere_dekripsi(teks, key):
    hasil = ""
    indeks_key = 0

    for karakter in teks.upper():
        if karakter.isalpha():
            nilai_cipher = ord(karakter) - ord('A')
            nilai_key = ord(key[indeks_key % len(key)]) - ord('A')

            nilai_plain = (nilai_cipher - nilai_key) % 26

            hasil += chr(nilai_plain + ord('A'))
            indeks_key += 1
        else:
            hasil += karakter

    return hasil


pesan = "PERTEMUAN TIM JAM 9"
key = "DATA"

ciphertext = vigenere_enkripsi(pesan, key)
plaintext = vigenere_dekripsi(ciphertext, key)

print("Pesan      :", pesan)
print("Key        :", key)
print("Ciphertext :", ciphertext)
print("Dekripsi   :", plaintext)