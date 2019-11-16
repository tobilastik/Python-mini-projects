from random import SystemRandom

sr = SystemRandom()


def generatePassword(length, validChars=None):
    if validChars is None:
        validChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        validChars += validChars.lower() + "1234567890"

    password = ""
    counter = 0

    while counter < length:
        rnum = sr.randint(0, 128)
        char = chr(rnum)
        if char in validChars:
            password += chr(rnum)
            counter += 1
    return password


print("Automatically generated password", generatePassword(15))
