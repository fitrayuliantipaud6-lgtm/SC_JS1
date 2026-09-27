plaintext = "KRIPTO"
key = 7

# Enkripsi
ciphertext = ""

for huruf in plaintext:
    if huruf.isalpha():
        nilai = ord(huruf) - ord('A')
        nilai_baru = (nilai + key) % 26
        ciphertext += chr(nilai_baru + ord('A'))
    else:
        ciphertext += huruf

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", ciphertext)


# Dekripsi
hasil_dekripsi = ""

for huruf in ciphertext:
    if huruf.isalpha():
        nilai = ord(huruf) - ord('A')
        nilai_baru = (nilai - key) % 26
        hasil_dekripsi += chr(nilai_baru + ord('A'))
    else:
        hasil_dekripsi += huruf

print("Dekripsi   :", hasil_dekripsi)