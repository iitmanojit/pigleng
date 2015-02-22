#!/usr/bin/python
######### english-piglatin.py ##############
# English to Piglatin Translator
# License: GNU GPL v2
# https://github.com/iitmanojit/pigleng
############################################
vowels='aeiouAEIOU'
englishText=str(raw_input("Enter text in English: ")).split()        
for word in englishText:
    if word[0:1] in vowels:
        print word+'yay'+' ',
    else:
        i=0
        for Char in word:
                if Char in vowels:
                        break
                i=i+1
       
        print  word[i:]+word[:i]+'ay'+' ',
            
            
			
	
