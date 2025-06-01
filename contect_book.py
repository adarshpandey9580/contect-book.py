cb={}
print("1.Create contact\n2.View contact\n3.Update Contact\n4.Delete Contact\n5.Search Contact\n6.Count Contact\n7.Exit")
while True:
    choice=int(input("Enter the choice: "))
    if choice == 1:
        name= input("Enter the name of user:")
        if name in cb:
            print(f"{name} is already exist")
        else:
          age=int(input("Enter the age:"))
          email =input("Enter the email:")
          P_num=int(input("Enter you number"))
          cb[name]={"age":age,"email":email,"Phone_number":P_num}
          print(f"Contact Name {name} is created:")

    elif choice == 2:
        name= input("Enter the name of user :")
        P_num= int(inpu("enter phone number"))
        for name,P_num in cb:
            print(f"Name:{name},Age:{age},email:{email},Phone_number:{P_num}")
        else:
            print(f"{name}not found")
            
    elif choice == 3:
        name= input("Enter the name of user:")
        if name in cb:
          age=int(input("Enter the Updated age:"))
          email =input("Enter the Updated email:")
          P_num=int(input("Enter you Updated number:"))
          cb[name]={"age":age,"email":email,"Phone_number":P_num}
          print(f"Contact Name {name} is Updated:")
        else:
          print(f"Contact name {name} is not found:")
             
    elif choice == 4:
        name= input("Enter the name of user:")
        if name in cb:
           del cb[name]
        else:
            print(f"Contact name {name} is not found:")
        
    elif choice == 5:
        search_name=input("enter the name to be search:")
        found=False
        for name ,contact in cb.items():
            if search_name.lower() in name.lower():
                print(f"FOUND THE CONTACT\nName:{name},Age:{age},email:{email},Phone_number:{P_num}")
            else:
                print("No contact is found:")
                
    elif choice == 6:
        length=len(cb)
        print(f"you have {length} contact in your phonebook:")
        
    elif choice == 7:
        print("Thankyou for using the applition:")
        break

    else:
        print("invalid input")
