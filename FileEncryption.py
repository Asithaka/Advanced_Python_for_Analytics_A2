
#codes = { "a": "%", "A" : "1"   , "b" : "@", "B" : "2"   ,"c": "&", "C" : "3"   , "d" : "#", "D" : "4"   ,"e" : "*", "E" : "5",
#         "f": "$", "F" : "6"   , "g" : "'('", "G" : "7"   ,"h": ">", "H" : "8"   , "i" : ":", "I" : "9"   ,"j" : "-", "J" : "10",
#          "k": "'{'", "K" : "'11'", "l" : "')'", "L" : "'12'","m": "/", "M" : "'13'", "n" : "!", "N" : "'14'","o" : "_", "O" : "'15'",
#         "p": "'100'", "P" : "'16'", "q" : "?", "Q" : "'17'","r": "+", "R" : "'18'", "s" : "`", "S" : "'19'","t" : "~", "T" : "'20'",
#          "u": "'['", "U" : "'21'", "v" : "<", "V" : "'22'","w": "|", "W" : "'23'", "x" : "=", "X" : "'24'","y" : ",", "Y" : "'25'",
#         "z": "']'", "Z" : "'26'"} 

codes = { "a": "`", "A" : "1", "b" : "~", "B" : "2",   "c": "!", "C" : "3",    "d" : "@", "D" : "4"   ,"e" : "#", "E" : "5",
          "f": "$", "F" : "6", "g" : "%", "G" : "7",   "h": "^", "H" : "8",    "i" : "&", "I" : "9"   ,"j" : "*", "J" : "0",
          "k": "(", "K" : ";", "l" : ")", "L" : "'","m": "-", "M" : "_", "n" : "+", "N" : "=","o" : "{", "O" : "}",
          "p": "[", "P" : "]", "q" : "|", "Q" : "Γ", "r": ":", "R" : "ψ", "s" : "σ", "S" : "<","t" : ",", "T" : ">",
          "u": ".", "U" : "?", "v" : "/", "V" : "¥","w": "€", "W" : "¢", "x" : "£", "X" : "♦","y" : "§", "Y" : "©",
          "z": "™", "Z" : "Ω", '.' : "Σ", ":" : "μ"} 

infile =open('info_security-1.txt','r', encoding='utf-8')

file_content = infile.read()

my_list = file_content.split()


encrypted_sentence = []   

for word in my_list:

    encrypted_word = [] 

    for i in range(len(word)):

        if word[i] in codes:

            encrypted_letter = codes[word[i]]

            encrypted_word.append(encrypted_letter)
           
    encrypted_sentence.append(encrypted_word)


print(encrypted_sentence)

outfile = open('encrypted.txt','w', encoding='utf-8')

for item in encrypted_sentence:

    for j in range(len(item)):

        outfile.write(f"{item[j]}")
       
    outfile.write(" ")

#outfile.write(".") 

outfile.close()

