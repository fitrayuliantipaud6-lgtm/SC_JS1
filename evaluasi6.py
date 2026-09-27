import string

alfabet = string.ascii_uppercase

# =========================
# CAESAR CIPHER
# =========================

def caesar(teks, key):
    hasil = ""

    for karakter in teks.upper():
        if karakter in alfabet:
            posisi = alfabet.index(karakter)
            hasil += alfabet[(posisi + key) % 26]
        else:
            hasil += karakter

    return hasil


# =========================
# MONOALPHABETICAL CIPHER
# =========================

alfabet_rahasia = "QWERTYUIOPASDFGHJKLZXCVBNM"


def monoalfabetik(teks):
    hasil = ""

    for karakter in teks.upper():
        if karakter in alfabet:
            posisi = alfabet.index(karakter)
            hasil += alfabet_rahasia[posisi]
        else:
            hasil += karakter

    return hasil


# =========================
# VIGENERE CIPHER
# =========================

def vigenere(teks, key):
    hasil = ""
    indeks_key = 0

    for karakter in teks.upper():
        if karakter in alfabet:
            p = alfabet.index(karakter)
            k = alfabet.index(key[indeks_key % len(key)])

            hasil += alfabet[(p + k) % 26]
            indeks_key += 1
        else:
            hasil += karakter

    return hasil


# =========================
# PROGRAM UTAMA
# =========================

pesan = "DOKUMEN RAPAT INTERNAL"

hasil_caesar = caesar(pesan, 3)
hasil_mono = monoalfabetik(pesan)
hasil_vigenere = vigenere(pesan, "DATA")

print("Pesan asli       :", pesan)
print("Caesar           :", hasil_caesar)
print("Monoalphabetical :", hasil_mono)
print("Vigenere         :", hasil_vigenere)