# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:16:47 2022

@author: ronni
"""

#variables

def encoder():
    message = input("Enter a message:")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = "?.,! :;\"\'\\><`~"
    encoded_messo = ""
    
    for letter in message:
        if letter not in punctuation:
            letter_index = alphabet.find(letter)
            encoded_messo += alphabet[(letter_index + 9) % 26]
            
        else:
            encoded_messo += letter
            
    print(encoded_messo)
    
encoder()


ask_to_continue = input("Do you want to decode the message?(Yes / No) ")

ask_to_continue = ask_to_continue.upper()

if ask_to_continue == "YES":
    def decoder():
        encoded_messo = input("Enter the encoded message:")   
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        punctuation = "?.,! :;\"\'\\><`~"
        decoded_messo = ""
        
        for letter in encoded_messo:
            if not letter in punctuation:
                letter_index = alphabet.find(letter)
                decoded_messo += alphabet[(letter_index - 9) % 26]
            else:
                decoded_messo += letter
                
        print(decoded_messo)
        
    decoder()
    
else:
    pass





