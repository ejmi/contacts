import json
import os
import sys
 
def welcome():
    print "Welcome to your contacts!"
 
def file_exist(filename):
    if os.path.isfile(filename):
        return True
    else:
        return False
 
def create_f(filename):
    with open(filedb, 'w') as f:
        pass
 
 
def load_f(filename):
    with open(filename, 'a+') as f:
        return json.load(f)
 
def dump_f(filedb, contacts):
    with open(filedb, 'w') as f:
        json.dump(contacts, f)
 
 
def contacts_count(contacts):
    return len(contacts)
 
 
 #-----------------
def user_input():  
    number = ''  
    numbers = [1, 2, 3, 4, 5, 6]
 
    while True:
        try:
            number = int(raw_input("Input number here... "))
        except ValueError:
            pass
 
        if number not in numbers:
            print "You can choose between 1-6."
        else:
            return number
 
#------------------
 
def print_menu():
    print "What do you want to do?"
    print """
  -------------------------
  |Press:                 |
  | 1. show all contacts  |
  | 2. search             |
  | 3. add new contact    |
  | 4. edit contact       |
  | 5. delete contact     |
  | 6. exit               |
  -------------------------
  """
 
 
 # ----- 1 -----
def show_contacts(contacts):
  print "-"*30
  for i in range(1, len(contacts)+1):
    print "%d. Name: %-15s Surname: %-15s email: %-20s phone: %s" % (i, contacts[i-1]['name'], contacts[i-1]['surname'], contacts[i-1]['mail'], contacts[i-1]['phone_number'])
  print "-"*30
 
 
# ----- 2 -----
def print_contact(contact):
  print "-"*30
  print"Name: %-20sSurname: %-20sMail: %-25sPhone Number: %-12s" % (contact['name'],contact['surname'],contact['mail'],contact['phone_number'])
  print "-"*30
 
def search(contacts):
  print "Please, select your search criteria:"
  print "a) Name\nb) Surname\nc) Mail\nd) Phone number"
 
  while True:
    letter = raw_input("Your choice: ").lower()
    if letter == 'a':
      criteria = "name"
      break
    elif letter == 'b':
      criteria = "surname"
      break
    elif letter == 'c':
      criteria = "mail"
      break
    elif letter == 'd':
      criteria = "phone_number"
      break
    else:
      print "Please, choose a, b, c or d..."
   
  search_for = raw_input("Please specify phrase to search: ")
 
  if search_for and criteria:
    result = search_data(contacts, criteria, search_for)
 
  if result:
    print "Contact found!"
    print_contact(result)
    return result
  else:
    print "Sorry, nothing found."
    return None
 
def search_data(contacts, criteria, search_for):
  result = [element for element in contacts if element[criteria] == search_for]
  if not result:
    return None
  else:
    return result[0]
 
 
# ----- 3 -----
def input_new_contact():
    name = raw_input("Please, give a contact's name: ")
    surname = raw_input("Please, give a contact's surname: ")
    mail = raw_input("Please, give a contact's email: ")
    phone_number = raw_input("Please, specify contact's phone number: ")
    return return_new_contact(name, surname, mail, phone_number)
 
def add_contact(contacts):
    new_contact = input_new_contact()
    contacts.append(new_contact)
    # counter
    contacts_count(contacts)
    print "Added {}".format(new_contact)
    return contacts
 
# return contact's dict
def return_new_contact(name, surname, mail, phone_number):
    return {'name':name, 'surname':surname, 'mail':mail, 'phone_number':phone_number}
   
 
 
# ----- 4 -----
def edit_contact(contacts):
    print "Which contact do you want to edit?"
    show_contacts(contacts)
    numb = ''
    n = contacts_count(contacts)
    while True:
        try:
            numb = int(raw_input("Please, give a number: "))
        except ValueError:
            pass
        numb -= 1
        if numb >= 0 and numb < n:
            print "What do you want to edit?"
            break
        else:    
            print "There's no such contact"
 
    print "Choose letter: \n a) Name \n b) Surname \n c) Mail \n d) Phone number"
    letter = ''
    letters = ['a', 'b', 'c', 'd']
    while True:
        try:
            letter = raw_input("Please, give a letter: ").lower()
            if letter not in letters:
                print "There is no such letter to choose"
            else:
                break
        except ValueError:
            pass
 
    if letter == 'a':      
        contacts[numb]['name'] = raw_input("Please, give a new name: ")
    elif letter == 'b':
        contacts[numb]['surname'] = raw_input("Please, give a new surname: ")
    elif letter == 'c':
        contacts[numb]['mail'] = raw_input("Please, give a new e-mail: ")
    else:
        contacts[numb]['phone_number'] = raw_input("Please, give a new phone number: ")
    print "Contact was changed\n"
 
# ----- 5 -----
def delete_contact(contacts):
    print "Which contact do you want to delete?"
    show_contacts(contacts)
    numb = ''
    n = contacts_count(contacts)
    while True:
        try:
            numb = int(raw_input("Please, give a number: "))
        except ValueError:
            pass
        numb -= 1
        if numb >= 0 and numb < n:
            print "Deleted",  contacts.pop(numb)
            break
        else:    
            print "There's no such contact"
       
 
 
# ----- main -----
if __name__ == "__main__":
    filedb = 'database.json'
    contacts = []
    welcome()
 
    if file_exist(filedb):
        print "File {} exists. I will try now to read the content..".format(filedb)
        try:
            contacts = load_f(filedb)
        except:
            print "Couldn't import the json data."
            contacts = []
    else:
        print "File {} doesn't exist. Will create one.".format(filedb)
        create_f(filedb)
 
    while True:
        print_menu()
        choice = user_input()
        if choice == 1:
            show_contacts(contacts)
        elif choice == 2:
            search(contacts)
        elif choice == 3:
            add_contact(contacts)
            print contacts
        elif choice == 4:
            edit_contact(contacts)
        elif choice == 5:
            delete_contact(contacts)
        elif choice == 6:
            dump_f(filedb, contacts)  
            sys.exit(0)
        else:
            print "What happend?"