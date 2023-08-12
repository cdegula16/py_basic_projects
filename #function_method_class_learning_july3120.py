#function_method_class_learning_july312023
#flow
#textbox for input either to proceed or quit
#if proceed textbox for inout either to sign-up, log-in or quit
#

import json

import signup_module
import login_module
        
while True:
    status = input("proceed or quit\n",)
    if status == ("proceed"):
        x = input("sign-up, log-in or exit",)
        sign = "sign-up"
        log = "log-in"

        if x == sign:
            print("sign-up")
            user_signup_return = signup_module.user_signup()
            print(user_signup_return)
            print(type(user_signup_return))
            print("sign-up successful")

        elif x == log:
            print ("log-in")
            user_login_return = login_module.user_login()
            print(user_login_return)
            if user_login_return == "log-in successful":
                print ("welcome to you may choose an app")
                chosen_app = input("input geometry or exit",) 

        elif x == ("exit"):
            print ("good_bye")

        else:
            print ("invalid input, try again")

    elif status == ("quit"):
        print("system_terminated")
        break

    else:
        print("invalid input try again")
    

    