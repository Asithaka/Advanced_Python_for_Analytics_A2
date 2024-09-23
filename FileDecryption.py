#codes = { "a": "%", "A" : "1"   , "b" : "@",   "B" : "2"   ,"c": "&", "C" : "3"   , "d" : "#", "D" : "4"   ,"e" : "*", "E" : "5",
#         "f": "$", "F" : "6"   , "g" : "(", "G" : "7"   ,"h": ">", "H" : "8"   , "i" : ":", "I" : "9"   ,"j" : "-", "J" : "10",
#         "k": "{", "K" : "'11'", "l" : ")", "L" : "'12'","m": "/", "M" : "'13'", "n" : "!", "N" : "'14'","o" : "_", "O" : "'15'",
#          "p": "]", "P" : "'16'", "q" : "?",   "Q" : "'17'","r": "+", "R" : "'18'", "s" : "`", "S" : "'19'","t" : "~", "T" : "'20'",
#          "u": "[", "U" : "'21'", "v" : "<",   "V" : "'22'","w": "|", "W" : "'23'", "x" : "=", "X" : "'24'","y" : ",", "Y" : "'25'",
#          "z": "}", "Z" : "'26'"} 

codes = { "a": "`", "A" : "1", "b" : "~", "B" : "2",   "c": "!", "C" : "3",    "d" : "@", "D" : "4"   ,"e" : "#", "E" : "5",
          "f": "$", "F" : "6", "g" : "%", "G" : "7",   "h": "^", "H" : "8",    "i" : "&", "I" : "9"   ,"j" : "*", "J" : "0",
          "k": "(", "K" : ";", "l" : ")", "L" : "'","m": "-", "M" : "_", "n" : "+", "N" : "=","o" : "{", "O" : "}",
          "p": "[", "P" : "]", "q" : "|", "Q" : "Γ", "r": ":", "R" : "ψ", "s" : "σ", "S" : "<","t" : ",", "T" : ">",
          "u": ".", "U" : "?", "v" : "/", "V" : "¥","w": "€", "W" : "¢", "x" : "£", "X" : "♦","y" : "§", "Y" : "©",
          "z": "™", "Z" : "Ω", '.' : "Σ", ":" : "μ"} 


infile = open('encrypted.txt','r',encoding='utf-8')

file_content = infile.read()

my_list = file_content.split()

decrypted_words = []

for word in my_list:

    decrypted_word =''

    for letter in word:

        for k,v in codes.items():

            if letter == v:

               decrypted_word = decrypted_word + k

    decrypted_words.append(decrypted_word)

#print(decrypted_words)

original =''

for item in decrypted_words:

    original += item

    original += ' '

# original +='.'

print(original)