import textwrap
def Encryption(number):
    if(len(number) < 50):
        for i in range(len(number), 50):
            number += "x"
    my_list = textwrap.wrap(number, 5)
    my_updated_list = []
    my_updated_list1 = []
    for k in range(5):
        for i in range(len(my_list)):
            my_updated_list.append(my_list[i][k])
    for i in range(0, 50, 5):
        my_updated_list1.append(my_updated_list[i]+my_updated_list[i+1]+my_updated_list[i+2]+my_updated_list[i+3] + my_updated_list[i+4])
    my_updated_list1 = "".join(my_updated_list1)
    return my_updated_list1

def Decryption(number, virtual):
    my_list = textwrap.wrap(number, 10)
    my_updated_list = []
    my_updated_list1 = []
    for k in range(10):
        for i in range(len(my_list)):
            my_updated_list.append(my_list[i][k])
    my_updated_list = my_updated_list[0:len(virtual)]
    my_updated_list = "".join(my_updated_list)
    return my_updated_list

def encryption(string):
    z = []
    for i in string:
        z.append(ord(i))
    y = "|".join(str(x) for x in z)
    return y

def decryption(name):
    li = list(name.split("|"))    
    new_li = []
    for i in range(len(li)):
        new_li.append(chr(int(li[i])))
    new_li = "".join(new_li)
    return new_li
def finalencrypt(password):
    return Encryption(encryption(password))
def finaldecrypt(password, temp):
    return decryption(Decryption(password,temp))
