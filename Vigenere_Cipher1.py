plaintext = "T"
key = "S"

nilai_plaintext = ord(plaintext) - ord('A')
nilai_key = ord(key) - ord('A')

nilai_ciphertext = (nilai_plaintext + nilai_key) % 26

ciphertext = chr(nilai_ciphertext + ord('A'))

print("Plaintext  :", plaintext)
print("Key        :", key)
print("Ciphertext :", ciphertext)