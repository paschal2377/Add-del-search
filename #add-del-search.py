#add-del-search.py
import json
import os

def add_person():
    # Getting input from user
    name = input("Name:")
    age = input("Age:")
    email = input("Email:")
    mobile_number = input("Mobile Number:") 
    
     # Returning person details in a dictionary
    person = {"Name": name,"Age": age,"Email": email,"Mobile Number": mobile_number}
    return person

def display_people(people):
    for i,person in enumerate(people):
         # Displaying each contact's details
        print(i+1,".",person["Name"],person["Age"],person["Email"],person["Mobile Number"])
    
def delete_contacts(people):
    display_people(people)
    
    while True:
        number = input("Enter a number to delete:")
        try:
            number = int(number)# Converting to integer for comparison
            if number <= 0 or number > len(people):
                print("Invalid number -> out of range!")
            else:
                people.pop(number-1)# Deleting the contact by index        
                print("Deleted!")
    
                break
        except ValueError:
            print("Invalid number!") 
   

def search(people):
     
    search_name = input("Search for a name:")
    results = []
    # Searching for matching names
    for person in people:
        name = person["Name"]
        if search_name in name:
            results.append(person)
    display_people(results)

# Main program
print("Welcome to the Contact Management System!\n")
print()

#Checking if contacts.json exists or create an empty one if not
if not os.path.exists("contacts.json"):
    with open("contacts.json", "w") as f:
        json.dump({"contacts": []}, f, indent=4)
        print("Created a new contacts.json file.")

# loading contacts 
try:
    with open("contacts.json", "r") as f:
        people = json.load(f).get("contacts", [])  # Load contacts from file
except (FileNotFoundError, json.JSONDecodeError):
    people = []

while True:
    print ("Contact List:", {len(people)})

    command = input("You can 'Add','Delete' or 'Search' and click 'q'for Quit!!! ")
    
    if command == "add":
        person = add_person()
        people.append(person)
        
    elif command == "delete":
        delete_contacts(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command!")

# Saving updated contacts back to the file
 
try:
    with open ("contacts.json","w") as f:
        json.dump({"contacts": people},f,indent=4)
except IOError as e:
    print(f"Error writing to the file: {e}")

        


        