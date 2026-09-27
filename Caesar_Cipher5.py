plaintext = input("Masukkan pesan: ")
key = int(input("Masukkan key: "))

# Enkripsi
ciphertext = ""

for huruf in plaintext:
    if huruf.isalpha():
        nilai = ord(huruf.upper()) - ord('A')
        nilai_baru = (nilai + key) % 26
        ciphertext += chr(nilai_baru + ord('A'))
    else:
        ciphertext += huruf

print("Ciphertext :", ciphertext)