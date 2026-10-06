ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
ALLOWED_LETTERS = ALPHABET + ALPHABET.lower()


def normalize_cedilla_letters(text):
    text = text.replace("Ş", "Ș").replace("ş", "ș")
    text = text.replace("Ţ", "Ț").replace("ţ", "ț")
    return text


def read_key():
    while True:
        value = input("Enter numeric key (1-30): ")
        try:
            key = int(value)
        except ValueError:
            print("Key must be an integer from 1 to 30.")
            continue

        if 1 <= key <= 30:
            return key

        print("Key must be an integer from 1 to 30.")


def read_message():
    while True:
        message = normalize_cedilla_letters(input("Enter message: "))
        invalid_character = None

        for character in message:
            if character != " " and character not in ALLOWED_LETTERS:
                invalid_character = character
                break

        if invalid_character is not None:
            print(
                f"Invalid character {invalid_character!r}. "
                "Allowed: letters A-Z, Ă, Â, Î, Ș, Ț, and spaces."
            )
            continue

        return message.upper().replace(" ", "")


def read_keyword():
    while True:
        keyword = normalize_cedilla_letters(input("Enter keyword: "))
        invalid_character = None

        for character in keyword:
            if character not in ALLOWED_LETTERS:
                invalid_character = character
                break

        if invalid_character is not None:
            print(
                f"Invalid character {invalid_character!r}. "
                "Allowed in the keyword: letters A-Z, Ă, Â, Î, Ș, Ț."
            )
            continue

        keyword = keyword.upper()
        if len(keyword) < 7:
            print(
                "Keyword must contain at least 7 Romanian letters "
                "(A-Z, Ă, Â, Î, Ș, Ț)."
            )
            continue

        return keyword


def build_permuted_alphabet(keyword):
    permuted_alphabet = []

    for letter in keyword:
        if letter not in permuted_alphabet:
            permuted_alphabet.append(letter)

    for letter in ALPHABET:
        if letter not in permuted_alphabet:
            permuted_alphabet.append(letter)

    return "".join(permuted_alphabet)


def transform(message, key, alphabet, decrypt=False):
    result = ""

    for letter in message:
        position = alphabet.index(letter)
        if decrypt:
            new_position = (position - key) % len(alphabet)
        else:
            new_position = (position + key) % len(alphabet)
        result += alphabet[new_position]

    return result


def main():
    while True:
        print("\nChoose a cipher:")
        print("1 - Caesar cipher")
        print("2 - Caesar cipher with a keyword")
        print("0 - Exit")
        cipher_choice = input("Your choice: ")

        if cipher_choice == "0":
            break
        if cipher_choice not in ("1", "2"):
            print("Choose 1, 2, or 0.")
            continue

        operation = input("Choose operation: 1 - encrypt, 2 - decrypt: ")
        while operation not in ("1", "2"):
            print("Choose 1 to encrypt or 2 to decrypt.")
            operation = input("Your operation: ")

        key = read_key()
        alphabet = ALPHABET

        if cipher_choice == "2":
            keyword = read_keyword()
            alphabet = build_permuted_alphabet(keyword)
            print("Permuted alphabet:", alphabet)

        message = read_message()
        result = transform(message, key, alphabet, decrypt=(operation == "2"))

        if operation == "1":
            print("Result (ciphertext):", result)
        else:
            print("Result (plaintext):", result)


if __name__ == "__main__":
    main()
