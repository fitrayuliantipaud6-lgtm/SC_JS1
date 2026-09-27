plaintext = "DATA AMAN"
key = 3

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