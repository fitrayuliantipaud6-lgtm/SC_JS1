plaintext = "KRIPTOGRAFI"
key = "KEY"

ciphertext = ""

for i in range(len(plaintext)):
    nilai_plaintext = ord(plaintext[i]) - ord('A')
    nilai_key = ord(key[i % len(key)]) - ord('A')

    nilai_ciphertext = (nilai_plaintext + nilai_key) % 26

    ciphertext += chr(nilai_ciphertext + ord('A'))

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", ciphertext)