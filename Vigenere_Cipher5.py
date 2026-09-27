plaintext = input("Masukkan plaintext: ").upper()
key = input("Masukkan key: ").upper()

# =====================
# ENKRIPSI
# =====================

ciphertext = ""
index_key = 0

for huruf in plaintext:
    if huruf.isalpha():
        nilai_plaintext = ord(huruf) - ord('A')
        nilai_key = ord(key[index_key % len(key)]) - ord('A')

        nilai_ciphertext = (nilai_plaintext + nilai_key) % 26

        ciphertext += chr(nilai_ciphertext + ord('A'))

        index_key += 1
    else:
        ciphertext += huruf

print("Ciphertext :", ciphertext)


# =====================
# DEKRIPSI
# =====================

hasil_dekripsi = ""
index_key = 0

for huruf in ciphertext:
    if huruf.isalpha():
        nilai_ciphertext = ord(huruf) - ord('A')
        nilai_key = ord(key[index_key % len(key)]) - ord('A')

        nilai_plaintext = (nilai_ciphertext - nilai_key) % 26

        hasil_dekripsi += chr(nilai_plaintext + ord('A'))

        index_key += 1
    else:
        hasil_dekripsi += huruf

print("Dekripsi   :", hasil_dekripsi)