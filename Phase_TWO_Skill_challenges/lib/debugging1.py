"""
hello debugging
# def say_hello(name):
#     return f"hello {name}"

# name = "Kay"

# print(f"hello {name}")
"""

"""
cipher debugging - impossible!

def encode(text, key):
    cipher = make_cipher(key)
    print(f"cipher is {cipher}")

    ciphertext_chars = []
    for i in text:
        if i != "a":
            ciphered_char = chr(65 + cipher.index(i))
            ciphertext_chars.append(ciphered_char)
            print(f"ciphered chars are {ciphered_char}")
    return "".join(ciphertext_chars)



def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)

"""
factorial debugging

def factorial(n):
    product = n
    print(f"at the start product is {product}")
    while n > 2:
        n -= 1
        # print(f"we multiply {product} by {n}")
        product *= n
        # print(f"we get {product}")
    
    return product
"""

# print(f"""
#  Running: factorial(5)
# Expected: 120
#   Actual: {factorial(5)}
# """)

# print(f"""
#  Running: factorial(3)
# Expected: 6
#   Actual: {factorial(3)}
# """)

# print(f"""
#  Running: factorial(7)
# Expected: 5040
#   Actual: {factorial(7)}
""")

"""




def get_most_common_letter(text):
    counter = {}
    print(text)
    for char in text:
        if char != " ":
            counter[char] = counter.get(char, 0) + 1
    print(f"dictionary being used it {counter}")
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(f"letter is printing {letter}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")