import string
alpha = list(string.ascii_uppercase)

txt = 'Enter a positive shift value: '
while True:
    try:
        shift = int(input(txt))
        break
    except ValueError:
        txt = 'Please, enter a shift integer: '

txt = 'Enter 1 to encrypt and 2 to decrypt: '
while True:
    try:
        flag = int(input(txt))
        if flag in [1,2]:break
        else: raise ValueError
    except ValueError:
        txt = 'Please enter 1 to encrypt and 2 to decrypt: '

message = input('Please enter your message: ').upper()

shift = shift % 26

encrypt = {}
decrypt = {}
for idx, letter in enumerate(alpha):
    encrypt[letter] = alpha[(idx + shift)%26]
    decrypt[alpha[(idx + shift)%26]] = letter

if flag == 1:
    encrypt_msg = ''
    for letter in message:
        encrypt_msg += encrypt.get(letter,letter)
    print(message, encrypt_msg)
else:
    decrypt_msg = ''
    for letter in message:
        decrypt_msg += decrypt.get(letter,letter)
    print(message, decrypt_msg)


