# cipher.py

def clean_key(key):
    return ''.join(filter(str.isalpha, key.upper()))

def encrypt_vigenere(plain_text, key):
    key = clean_key(key)
    result, j = '', 0
    for char in plain_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
            j += 1
        else:
            result += char
    return result

def decrypt_vigenere(cipher_text, key):
    key = clean_key(key)
    result, j = '', 0
    for char in cipher_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[j % len(key)]) - ord('A')
            result += chr((ord(char) - base - shift + 26) % 26 + base)
            j += 1
        else:
            result += char
    return result
