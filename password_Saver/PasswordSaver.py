import csv
import sys

# The password file name to store the passwords to
passwordFile = "password_Saver\samplePasswordFile"
# The encryption key for the caesar cypher
encryptionKey = 16


# Caesar Cypher Encryption
def passwordEncrypt(unencryptedMessage, key):

    # Start with an empty string as our encryptedMessage
    encryptedMessage = ''

    # For each symbol in the unencryptedMessage add an encrypted symbol into the encryptedMessage
    for symbol in unencryptedMessage:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            encryptedMessage += chr(num)
        else:
            encryptedMessage += symbol
    return encryptedMessage


def loadPasswordFile(file):

    with open(file, newline='') as csvfile:
        passwordreader = csv.reader(csvfile)
        passwordList = list(passwordreader)

    return passwordList


def savePasswordFile(passwordList, file):

    with open(file, 'w+', newline='') as csvfile:
        passwordwriter = csv.writer(csvfile)
        passwordwriter.writerows(passwordList)


while True:
    print("What would you like to do:")
    print(" 1. Open password file")
    print(" 2. Lookup a password")
    print(" 3. Add a password")
    print(" 4. Save password file")
    print(" 5. Print the encrypted password list (for testing)")
    print(" 6. Quit program")
    print("Please enter a number (1-6)")
    choice = input()

    if(choice == '1'):  # Load the password list from a file
        passwords = loadPasswordFile(passwordFile)

    if(choice == '2'):  # Lookup at password
        print("Which website do you want to lookup the password for?")
        for word in passwords:
            print(word[0])
        passwordToLookup = input()
        for i in passwords:
            if str(passwordToLookup) == str(i[0]):
                print(passwordEncrypt(i[1], -16))

    if(choice == '3'):
        print("What website is this password for?")
        website = input()
        print("What is the password?")
        unencryptedPassword = input()
        encryptedPassword = passwordEncrypt(unencryptedPassword, encryptionKey)
        passwords2 = [website, encryptedPassword]
        passwords.append(passwords2)

    if(choice == '4'):  # Save the passwords to a file
        savePasswordFile(passwords, passwordFile)

    if(choice == '5'):  # print out the password list
        for keyvalue in passwords:
            print(', '.join(keyvalue))

    if(choice == '6'):  # quit our program
        sys.exit()
