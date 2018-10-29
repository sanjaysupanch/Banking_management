import textwrap
def Encryption(number):
    for count in range(len(number), 12):
        number+="x"
    my_list = textwrap.wrap(number, 3)
    my_updated_list = []
    my_updated_list1 = []
    for k in range(3):
        for i in range(len(my_list)):
            my_updated_list.append(my_list[i][k])
    for i in range(0, 12, 4):
        my_updated_list1.append(my_updated_list[i]+my_updated_list[i+1]+my_updated_list[i+2]+my_updated_list[i+3])

    my_updated_list1 = "".join(my_updated_list1)
    return my_updated_list1

def Decryption(number, virtual):
    my_list = textwrap.wrap(number, 4)
    my_updated_list = []
    my_updated_list1 = []
    for k in range(4):
        for i in range(len(my_list)):
            my_updated_list.append(my_list[i][k])
    for i in range(0, 12, 3):
        my_updated_list1.append(my_updated_list[i]+my_updated_list[i+1]+my_updated_list[i+2])

    my_updated_list1 = "".join(my_updated_list1)
    my_updated_list1 = my_updated_list1[0:len(virtual)]
    print(my_updated_list1)


def main():
    num = input()
    name = Encryption(num)
    print(name)
    Decryption(name, num)
if __name__ == "__main__":
    main()