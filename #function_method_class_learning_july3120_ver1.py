#function_method_class_learning_july312023

import json

x = input("sign-up, log-in or quit",)
sign = "sign-up"
log = "log-in"
#print(x)

if x == sign:
    #print ("sign-up")
    user1_name = input("input name",)
    user1_username = input("input username",)
    user1_password = input("input password",)
    user1 = ('{'+('"name":"{}","username":"{}","password":"{}"').format(user1_name, user1_username, user1_password)+'}')
    print(user1)
    user1_str = str(user1)
    with open('user1.txt', 'w') as user1_text:
        user1_text.write(user1_str)
        user1_text.close()
    # with open('user1.txt', 'r') as user1_text:
    #     user1_text_content = user1_text.readlines()
    # #user1_dict = dict(user1_text_content)
    # print(user1_text_content)
    # print(type(user1_text_content))
    # user1_text.close()
elif x == log:
    print ("log-in")
    with open('user1.txt', 'r') as user1_text:
        user1_text_content = user1_text.readline()
        user1_text.close()
    print(user1_text_content)
    print(type(user1_text_content))
    user1_dict = json.loads(user1_text_content)
    #print(user1_dict)
    #print(type(user1_dict))
    input_username = input("input username",)
    if input_username == user1_dict["username"]:
        input_password = input("input password",)
        if input_password == user1_dict["password"]:
            print("log-in successful")
        else:
            print("incorrect password")
    else:
        print("wrong username")
elif x == ("quit"):
    print ("quit")
else:
    print ("invalid input, try again")