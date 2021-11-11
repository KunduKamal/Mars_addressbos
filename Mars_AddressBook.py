# inisialize address book
# mbook = { 'name':{"Name":<value>, "age":<value>, "Dob": <value>,"PhoneNo":<value>} }
mbook={} 
quit_enable = 0

# do u want to print data or quiet
message="select your choice from below:\n \
        to enter new data input: 1 \n \
        to modify data: 2 \n \
        to remove data: 3 \n \
        to show existing data: 4 \n \
        to show all data: 5 \n \
        to exit the program: q \n \
        "
while (not quit_enable):

    print (message)
    # get user input for option 
    mode_select = input("Enter Option:")            #; print(type(mode_select)) 

    # check user option 
    if mode_select == "1":
        t_name = input("Enter the User Name:")
        t_age = input("Enter the User Age:")
        t_dob = input("Enter the User Date of Birth:")
        t_Ph_N = input("Enter the User Phone Number:")
        mbook[t_name] = {"Name":t_name,"Age":t_age,"Dob":t_dob,"PhoneNo":t_Ph_N} #Data storage
        

    elif mode_select == "2":
        t_name = input("Enter the name you want to modify:")
        u_info = mbook[t_name]
        print ( "Enter which information you want to modify: \
            select your choice from below:\n \
            to modify date of birth: 1 \n \
            to modify Phone No: 2 \n \
            to modify Age: 3 " )
            # to modify Name input: 4 ")
        
        t_modify = input("Input choise: ")
        if ( t_modify == "1"):
            t_mod_dob = input("Enter the new Date of Birth: ")
            u_info["Dob"] = t_mod_dob
        elif ( t_modify == "2"):
            t_mod_phn = input("Enter the new Phone Number: ")
            u_info["PhoneNo"] = t_mod_phn
        elif ( t_modify == "3"):
            t_mod_age = input("Enter the new Age: ")
            u_info["Age"] = t_mod_age
        # elif ( t_modify == "4"):
        #     t_mod_name = input("Enter the new Name: ")
        #     u_info["Name"] = t_mod_name
        else:  print ("Invalid input. Please input betwee 1 ~ 4.")

        mbook[t_name] = u_info      # store the modified data
        
    elif mode_select == "3":
        t_name = input("Enter the name you want to remove:")
        u_info = mbook[t_name]
        print ( "Enter which information you want to remove: \
            select your choice from below:\n \
            to remove date of birth: 1 \n \
            to remove Phone No: 2 \n \
            to remove Age: 3 " )
        t_remove = input("Input choise: ")
        if t_remove == "1":
            u_info["DOb"] = "-"
        elif t_remove == "2":
            u_info["PhoneNo"] = "-"
        elif t_remove == "3":
            u_info["age"] = "-"

        mbook[t_name] = u_info

    elif mode_select == "4":
        t_name = input("Enter the name you want to see:")
        if mbook.has_key(t_name):
            print(mbook[t_name])
        else:
            print("The information of ", t_name, "is not in the book")
 
    elif mode_select == "5":
        print(mbook) 

    elif mode_select=="q":
        quit_enable = 1
        print("Bye.")
        # break
    else:
        pass


#print(mbook)
