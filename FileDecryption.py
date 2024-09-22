codes = { "a": "%", "A" : "1"   , "b" : "@",   "B" : "2"   ,"c": "&", "C" : "3"   , "d" : "#", "D" : "4"   ,"e" : "*", "E" : "5",
          "f": "$", "F" : "6"   , "g" : "∫", "G" : "7"   ,"h": ">", "H" : "8"   , "i" : ":", "I" : "9"   ,"j" : "-", "J" : "10",
          "k": "€", "K" : "'11'", "l" : "Ω", "L" : "'12'","m": "/", "M" : "'13'", "n" : "!", "N" : "'14'","o" : "_", "O" : "'15'",
          "p": "¥", "P" : "'16'", "q" : "?",   "Q" : "'17'","r": "+", "R" : "'18'", "s" : "`", "S" : "'19'","t" : "~", "T" : "'20'",
          "u": "µ", "U" : "'21'", "v" : "<",   "V" : "'22'","w": "|", "W" : "'23'", "x" : "=", "X" : "'24'","y" : ",", "Y" : "'25'",
          "z": "₹", "Z" : "'26'"} 



infile = open('encrypted.txt','r')

file_content = infile.read()

my_list = file_content.split()

     
for word in my_list:

    decrypted_word =[]

    for letter in word:

        for k,v in codes.items():

            if letter == v:

                decrypted_word.append(k)
    
    print (decrypted_word)