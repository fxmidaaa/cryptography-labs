"""Laboratory work 3, task 3.2: Vigenere cipher for Romanian text."""


ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
ALLOWED_LETTERS = ALPHABET + ALPHABET.lower()
MINIMUM_KEY_LENGTH = 7


def normalize_romanian_letters(text):
    # Старые варианты Ş и Ţ заменяем современными румынскими буквами Ș и Ț.
    text = text.replace("Ş", "Ș")
    text = text.replace("ş", "ș")
    text = text.replace("Ţ", "Ț")
    text = text.replace("ţ", "ț")
    return text


def contains_only_letters(text):
    # Проверяем символы до перевода в верхний регистр.
    for character in text:
        if character not in ALLOWED_LETTERS:
            print("Invalid character:", repr(character))
            print("Allowed: A-Z, a-z, Ă, Â, Î, Ș, Ț and their lowercase forms.")
            return False

    return True


def read_key():
    while True:
        key = input("Enter key (at least 7 letters, without spaces): ")
        key = normalize_romanian_letters(key)

        if not contains_only_letters(key):
            continue

        if len(key) < MINIMUM_KEY_LENGTH:
            print("The key must contain at least 7 letters.")
            continue

        return key.upper()


def read_message():
    while True:
        message = input("Enter message or ciphertext: ")
        message = normalize_romanian_letters(message)

        # По условию удаляем пробелы, затем переводим буквы в верхний регистр.
        message = message.replace(" ", "")

        if message == "":
            print("The message must contain at least one letter.")
            continue

        if not contains_only_letters(message):
            continue

        return message.upper()


def encrypt_message(message, key):
    encrypted_message = ""

    for message_position in range(len(message)):
        message_letter = message[message_position]

        # После последней буквы ключа снова используем первую.
        key_position = message_position % len(key)
        key_letter = key[key_position]

        # Код буквы — ее позиция в румынском алфавите, от 0 до 30.
        message_code = ALPHABET.index(message_letter)
        key_code = ALPHABET.index(key_letter)

        # Шифрование: C = (M + K) mod 31.
        encrypted_code = (message_code + key_code) % len(ALPHABET)
        encrypted_letter = ALPHABET[encrypted_code]

        encrypted_message = encrypted_message + encrypted_letter

    return encrypted_message


def decrypt_message(ciphertext, key):
    decrypted_message = ""

    for ciphertext_position in range(len(ciphertext)):
        ciphertext_letter = ciphertext[ciphertext_position]

        key_position = ciphertext_position % len(key)
        key_letter = key[key_position]

        ciphertext_code = ALPHABET.index(ciphertext_letter)
        key_code = ALPHABET.index(key_letter)

        # Расшифровка: M = (C - K) mod 31.
        # В Python остаток при положительном делителе не бывает отрицательным.
        decrypted_code = (ciphertext_code - key_code) % len(ALPHABET)
        decrypted_letter = ALPHABET[decrypted_code]

        decrypted_message = decrypted_message + decrypted_letter

    return decrypted_message


def main():
    while True:
        print("\nVigenere cipher for the Romanian alphabet")
        print("1 - Encrypt")
        print("2 - Decrypt")
        print("0 - Exit")

        operation = input("Choose an operation: ")

        if operation == "0":
            break

        if operation not in ("1", "2"):
            print("Choose 1, 2 or 0.")
            continue

        key = read_key()
        message = read_message()

        if operation == "1":
            result = encrypt_message(message, key)
            print("Ciphertext:", result)
        else:
            result = decrypt_message(message, key)
            print("Decrypted message:", result)


if __name__ == "__main__":
    main()
