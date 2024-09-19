
codes = { "A": "%", "a" : "1" , "B" : "@", "b" : "2" ,"C": "&", "c" : "3" , "D" : "#", "d" : "4" ,"E" : "*", "e" : "5",
          "F": "$", "f" : "6" , "G" : "(", "g" : "7" ,"H": ">", "h" : "8" , "I" : ":", "i" : "9" ,"J" : "-", "j" : "10",
          "K": "{", "k" : "11", "L" : ")", "l" : "12","M": "/", "m" : "13", "N" : "!", "n" : "14","O" : "_", "o" : "15",
          "P": "}", "p" : "16", "Q" : "?", "q" : "17","R": "+", "r" : "18", "S" : "`", "s" : "19","T" : "~", "t" : "20",
          "U": "[", "u" : "21", "V" : "<", "v" : "22","W": "|", "w" : "23", "X" : "=", "x" : "24","Y" : ",", "y" : "25",
          "Z": "]", "z" : "26"} 

infile =open('info_security-1.txt','r')

file_content = infile.read()

my_list = file_content.split()


#encrypted_sentence = []  
 

for word in my_list:

    encrypted_word = [] 

    for i in range(len(word)):

        if word[i] in codes:

            encrypted_letter = codes[word[i]]

            encrypted_word.append(encrypted_letter)

    print(encrypted_word)

# outfile = open('encrypted.txt','w')

