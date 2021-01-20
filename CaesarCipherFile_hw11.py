# File: CeasarCipherFile.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50705

# Date Created:11/13/2020
# Date Last Modified:11/14/2020

# Description of Program: Ceaserian Cipher while opening files

import os.path

def encrypt(input, output_name, shift):
    output = open(output_name + '.txt', 'w')
    for line in input:
        newLine = ''
        for ch in line:
            if (64 < ord(ch) < 91) or (96 < ord(ch) < 123):
                W = ord(ch) - ord('A')     
                X = (W + shift) % 26           
                Y = X + ord('A')             
                Z = chr( Y )

                if ch.islower():
                    newLine += Z.lower()
                else:
                    newLine += Z
                
            else:
                newLine += ch
        output.write(newLine)
    output.close()


def decrypt(input, output_name, shift):
    output = open(output_name + '.txt', 'w')
    for line in input:
        newLine = ''
        for ch in line:
            if 64 < ord(ch) < 91 or (96 < ord(ch) < 123):
                W = ord(ch) - ord('A')     
                X = (W - shift) % 26           
                Y = X + ord('A')             
                Z = chr( Y )

                if ch.islower():
                    newLine += Z.lower()
                else:
                    newLine += Z
                
            else:
                newLine += ch
        output.write(newLine)
    output.close()


def main():
    # ask for a command from the user 
    operation = input('Enter Caesar cipher command (encrypt/decrypt): ')
    if operation.lower() == 'encrypt':
        print('You\'ve asked to encrypt.')
    elif operation.lower() == 'decrypt':
        print('You\'ve asked to decrypt.')
    else:
        print('Command is invalid')
        return

    # ask for a shift value from the user
    shift = int(input('Please enter shift value (0 .. 25): '))
    if not (0 <= shift <= 25):
        print('Shift value is invalid')
        return

    # ask for a file name from the user
    file_name = input('Please enter filename with text to ' + operation.lower() + ': ')
    if not os.path.isfile(file_name + '.txt'):
        print('File does not exist')
        return


    # read and process the input
    file = open(file_name + '.txt', 'r')

    if operation.lower() == 'encrypt':
        output_name = file_name + '-Enc'
        encrypt(file.readlines(), output_name, shift)

    elif operation.lower() == 'decrypt':
        output_name = file_name + '-Dec'
        decrypt(file.readlines(), output_name, shift)

    print('The input filename is', file_name)
    print('The output filename is', output_name)


main()

