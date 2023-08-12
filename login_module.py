#log-in module

import json

def user_login():
    with open('user1.txt', 'r') as user1_text:
        user1_text_content = user1_text.readline()
        user1_text.close()
    print(user1_text_content)
    print(type(user1_text_content))
    user1_dict = json.loads(user1_text_content)
    
    username_try_count = 0
    password_try_count = 0
    try_again = "try_again"
    cancel = "cancel"
    
    while username_try_count < 3:
        input_username = input("input username",)

        if input_username == user1_dict["username"]:
            print("username valid")

            while password_try_count < 3:
                input_password = input("input password",)

                if input_password == user1_dict["password"]:
                    login_status = ("log-in successful")
                    break
                else:
                    password_try_count += 1
                    if password_try_count == 3:
                            login_status = ("log-in failed, multiple password attempt")
                            break
                    wrong_password = input("incorrect password, try_again or cancel",)
                    while wrong_password != try_again and wrong_password != cancel:
                        print("incorrect input try again")
                        wrong_password = input("incorrect password, try_again or cancel",)
                    if wrong_password == try_again:
                        print("try_again", password_try_count)
                    if wrong_password == cancel:
                        print("log-in cancelled")
                        login_status = ("log-in failed, incorrect password")
                        break
            break
                                    
        else:
                username_try_count += 1
                if username_try_count == 3:
                    login_status = ("log-in failed, multiple username attempt")
                    break
                wrong_username = input("wrong username, try_again or cancel",)
                while wrong_username != try_again and wrong_username !=cancel:
                    print("incorrect input try again")
                    wrong_username = input("wrong username, try_again or cancel",)
                if wrong_username == try_again:
                    print("try_again", username_try_count)
                if wrong_username == cancel:
                    print("log-in cancelled")
                    login_status = ("log-in failed, incorrect username")
                    break

    return login_status 