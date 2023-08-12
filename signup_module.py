#sign-up module
def user_signup():
    user1_name = input("input name",)
    user1_username = input("input username",)
    user1_password = input("input password",)
    user1 = ('{'+('"name":"{}","username":"{}","password":"{}"').format(user1_name, user1_username, user1_password)+'}')
    #print(user1)
    #user1_str = str(user1)
    with open('user1.txt', 'w') as user1_text:
        user1_text.write(user1)
        user1_text.close()
    with open('user1.txt', 'r') as user1_text:
        user1_text_content = user1_text.readline()
        user1_text.close()
    return user1_text_content