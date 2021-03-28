import random
import string
import base64
import hashlib


class PasswordGenerator:
    # abcdefghijklmnopqrstuvwxyz
    LOWERCASE_ALPHABET_LIST = [x for x in string.ascii_lowercase]

    # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    UPPERCASE_ALPHABET_LIST = [x for x in string.ascii_uppercase]

    # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    SPECIAL_CHARACTOR_LIST = [x for x in string.punctuation]
    def __init__(self, length, lowerCase=True, upperCase=True, specialChars=False, removeChars=None):  
        self.passwordLength = length
        self.lowerCase = lowerCase
        self.upperCase = upperCase
        self.specialChars = specialChars
        self.useableCharactors = []
        self.charsRemoved = []

        if removeChars != None:
            if not isinstance(removeChars, (list, tuple)): raise TypeError("removeChars must be a list or tuple.")
            for item in removeChars:
                self.charsRemoved.append(item)

        if self.upperCase:
            for item in self.UPPERCASE_ALPHABET_LIST:
                if item not in self.charsRemoved:
                    self.useableCharactors.append(item)

        if self.lowerCase:
            for item in self.LOWERCASE_ALPHABET_LIST:
                if item not in self.charsRemoved:
                    self.useableCharactors.append(item)
        
        if self.specialChars:
            for item in self.SPECIAL_CHARACTOR_LIST:
                if item not in self.charsRemoved:
                    self.useableCharactors.append(item)


    def getRandomChar(self, charList):
        if not isinstance(charList, (list, tuple)): raise TypeError("charList must be a list or tuple.")
        return random.choice(random.choices(charList, k=5))

    def generatePassword(self):
        password = ""

        for _ in range(self.passwordLength):
            password += self.getRandomChar(self.useableCharactors)

        return password

    def reorderPassword(self, password):
        if not isinstance(password, str): raise TypeError("password must be a list or tuple.")
        currentPasswordItems = [x for x in password]
        newPassword = ""

        for _ in range(len(currentPasswordItems)):
            newChar= self.getRandomChar(currentPasswordItems)
            currentPasswordItems.remove(newChar)
            newPassword +=newChar

        return newPassword



if __name__ == "__main__":
    toRemove = ["'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "`"]
    pwg = PasswordGenerator(length=100, lowerCase=True, upperCase=True, specialChars=True, removeChars=toRemove)

    password = pwg.generatePassword()
    print(password)

    password = pwg.reorderPassword(password)
    print(password)