contact {}

def display_contact():
  print("name\t\tcontact number")
  for key in contact:
   print("{}\t\t{}".format(key,contact.get(key)))

while True:
  choice=int(input("1. Add New Contact \n 2. Search Contact \n 3. Display contact \n 4. Edit Contact \n 5. Delete Contact\n 6.Exit\n 7. Enter your choise"))


if choice == 1:
  name input("enter the contact name")
  phone input("enter the mobile number")
  contact[name] = phone
elif choice == 2:
  search_name = input("Enter the contact name")
  if search_name in contact:
    print(search_name, "'S contact number is", contact [search_name])
else:
  print("the name is not found in contact book")
elif choice==3:
  if not contact:
    print("empty contact book")
  else:
    display_contact()
elif choice==4:
  edit_contact = input("Enter the contact to be Edited")
  if edit_contact in contact:
    phone = input("Enter thc Nobile Munber")
    contact[edit_contact] = phone
    print("Contact Updatedi`)
    display_contact()
  else:
    print("The Nane 1s not- found in Contact Book") 
    del_contact = input("Enter the-Contact to be Deletod.") 
    if del_contact in contact: 
      confirn = input("Do: You Want to Dolete this Contact y/n7")
      if confirn = y' or confirn == "y': 
         contact.pop(del_contact) 
      display_contact() 
    else:
      print("The Nane 1s nat found in Contact Book'") 
    else: 
        break
 
