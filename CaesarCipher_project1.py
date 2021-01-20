# File: CaesarCipher.py
# Student: Ahmet Nalcaci
# UT EID: an27394
# Course Name: CS303E
# Unique Number: 50695
#
# Date Created: 10/7/2020
# Date Last Modified: 10/7/2020
# Description of Program: project 1 let us to encrypts and decrypts text


def main():
    
    command = input("Enter Caesar cipher command (encrypt/decrypt): ").lower()
    if (command == "encrypt"):
        print("You’ve asked to encrypt.")
        shiftValue = int(input("Please enter shift value (0 .. 25): "))
        
        if (shiftValue < 0) or (shiftValue > 25):
            print("Illegal shift value: ", shiftValue)
        else:
            encryptText = input("Please enter text to encrypt: ")
            encryptTexttwo = ""
            #for loop let us encrypt a text
            for i in range(len(encryptText)):
                #if statements makes the text decide if the text is lower or upper or something else 
                if 64 < ord(encryptText[i]) < 91:
                    
                    W = ord(encryptText[i]) - ord('A')     
                    X = (W + shiftValue) % 26           
                    Y = X + ord('A')             
                    Z = chr( Y )
                    encryptTexttwo += Z
                    
                elif 96 < ord(encryptText[i]) < 123:
                    
                    W = ord(encryptText[i]) - ord('a')     
                    X = (W + shiftValue) % 26           
                    Y = X + ord('a')             
                    Z = chr( Y )
                    encryptTexttwo += Z
                    
                else:
                    encryptTexttwo += encryptText[i]
            print(encryptTexttwo)
                                                                
    elif (command == "decrypt"):
        print("You’ve asked to decrypt.")
        shiftValue = int(input("Please enter shift value (0 .. 25): "))
        
        if (shiftValue < 0) or (shiftValue > 25):
            print("Illegal shift value: ", shiftValue)
        else:
            decryptText = input("Please enter text to decrypt: ")
            decryptTexttwo = ""
            #for loop let us decryp a text
            for i in range(len(decryptText)):
                #if statements makes the text decide if the text is lower or upper or something else 
                if 64 < ord(decryptText[i]) < 91:
                    
                    W = ord(decryptText[i]) - ord('A')     
                    X = (W - shiftValue) % 26           
                    Y = X + ord('A')             
                    Z = chr( Y )
                    decryptTexttwo += Z
                    
                elif 96 < ord(decryptText[i]) < 123:
                    
                    W = ord(decryptText[i]) - ord('a')     
                    X = (W - shiftValue) % 26           
                    Y = X + ord('a')             
                    Z = chr( Y )
                    decryptTexttwo += Z
                    
                else:
                    decryptTexttwo += decryptText[i]
            print(decryptTexttwo)
        
    else:
        print("Unrecognized command:", command)
        
main()


