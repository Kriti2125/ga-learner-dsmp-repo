# --------------
##File path for the file 
file_path 


#Code starts here

#write a function to read the file
def read_file(path):
    file = open(file_path, 'r')
    sentence = file.read()
    file.close()
    return sentence

#Function call
sample_message = read_file(file_path)


# --------------
#Code starts here
file_path_1
file_path_2

    
#Calling the function from previous task
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)
print(message_1)
print(message_2)

#Function to take two parameters for messages
def fuse_msg(message_a, message_b):
    quotient = (int(message_b)//int(message_a))
    return str(quotient)

#function call
secret_msg_1 = fuse_msg(message_1, message_2)
print("Quotient of floor division is :", secret_msg_1)



# --------------
#Code starts here
file_path_3
sub = '0'
#Function calling from 1st task
message_3 = read_file(file_path_3)
print("Message in file 3 : ", message_3)

#function to substitue value 
def substitute_msg(message_c):
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub =  'Marine Biologist' 
    return sub      

#Function call for substitute msg
secret_msg_2 = substitute_msg(message_3)
print("Substituting the message in file 3", secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here

#Reading the msg from file 4 and 5 with read_file function
message_4 = read_file(file_path_4)
print("Message_4 is : ", message_4)

message_5 = read_file(file_path_5)
print("Message_5 is : ", message_5)

#Function to compare the messages
def compare_msg(message_d, message_e):
    c_list = [" "]
    #Splitting the messgae into words
    a_list = message_d.split(" ")
    #print(a_list)
    b_list= message_e.split(" ")
    #print(b_list)
    #for x in a_list:
        #if x not in b_list:
            #c_list += x
    #print("Words that are not in b_list are : ", c_list)
    c_list = [word for word in a_list if word not in b_list]

    #Joing the words
    final_msg = " ".join(c_list)
    return(final_msg)

secret_msg_3 = compare_msg(message_4, message_5)
print("The final msg is : ",secret_msg_3)








# --------------
#Code starts here
file_path_6

#read the file 6
message_6 = read_file(file_path_6)
print("Message 6 is : ", message_6)

#Function to extract the msg
def extract_msg(message_f):
    a_list = message_f.split(' ')
    #print(a_list)
    even_word = lambda x : (len(x)%2 == 0)
    #print(even_word)
    b_list = filter(even_word, a_list)
    #print(b_list)
    final_msg = " ".join(b_list)
    return final_msg

#extract function calling
secret_msg_4 = extract_msg(message_6)
print("Final msg 4 is :", secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

secret_msg = " ".join(message_parts)
#print(secret_msg)

#Function write_file
def write_file(secret_msg, path):
    f = open(path, 'a+')
    f.write(secret_msg)
    f.close()

#function call
write_msg = write_file(secret_msg, final_path)
print(secret_msg)




