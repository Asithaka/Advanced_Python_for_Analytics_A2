infile = open('sometext.txt','r')

file_contents = infile.read()

#file_list=list(file_contents)

my_list = file_contents.split()

# print(my_list)

my_dict =  {}

# for word in my_list:
    
#     if word not in my_dict:

#         my_dict[word] = 1

#     else:
#          my_dict[word] +=  1

# print(my_dict)


for word in my_list:

    my_dict[word] = my_dict.get(word,0) +1

print(my_dict)