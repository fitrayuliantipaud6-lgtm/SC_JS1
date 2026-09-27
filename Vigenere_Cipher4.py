plaintext = "DATA AMAN"
key = "KEY"

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

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", ciphertext)