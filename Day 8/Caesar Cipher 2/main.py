alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(dir_val, text, shift):
    cipher_text = ""
    for letter in text:
        shifted_position = alphabet.index(letter) + dir_val * shift
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the {'encoded' if dir == 1 else 'decoded'} result: {cipher_text}")

dir_val = 0
if direction == "encode":
    dir_val = 1
elif direction == "decode":
    dir_val = -1

caesar(dir_val, text, shift)


