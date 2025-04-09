def shift_char(char: str, shift: int) -> str:
    if char.isspace():
        return char
    char = char.lower()
    if char.isalpha():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        return chr((ord(char) + shift) % 256)


def encrypt(plaintext: str, key: int) -> str:
    return ''.join(map(lambda c: shift_char(c, key), plaintext))


def decrypt(ciphertext: str, key: int) -> str:
    return ''.join(map(lambda c: shift_char(c, -key), ciphertext))


def main():
    key = int(input("Enter shift key: "))
    plaintext = input("Enter text to encrypt: ")
    encrypted = encrypt(plaintext, key)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted, key))


if __name__ == "__main__":
    main()
