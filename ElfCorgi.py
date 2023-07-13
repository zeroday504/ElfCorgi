import requests
from bs4 import BeautifulSoup
import os

print("               ____ _    ____    ____ ____ ____ ____ _") 
print("               |___ |    |___    |    |  | |__/ | __ |") 
print("               |___ |___ |       |___ |__| |  \ |__] |")
print("--------------------------------------------------------------------------")
print("            CLI for Elf Qrin's sock puppet account generator")
print('\n')
        

def attribute_formatter(a, b):
    count = 0
    if "Password hash (MD5)" in b:
        y = b.replace("Password hash (MD5)", "Password hash (MD5): ")
        return y
    elif "Password hash (SHA1)" in b:
        y = b.replace("Password hash (SHA1)", "Password hash (SHA1): ")
        return y      
    elif "Car License Plate" in b:
        y = b.replace("Car License Plate", "Car License Plate: ")
        return y
    elif "Credit Car" in b:
        y = None
    else:        
        y = b.replace(a, a + ": ")
        return y
   

        

gender = input("Select gender of sock puppet account (m or f): ")

print("\nEstablishing connection to Elf Qrin's Lab...")
web_request=requests.get("https://www.elfqrin.com/fakeid.php?gender=" + gender)

if web_request.status_code == 200:
        print("\nSuccessful connection, generating sock puppet account...\n")
else:
        print("\nUnsuccessful connection, try again\n")

soup = BeautifulSoup(web_request.text, "html.parser")

header = soup.find_all("td")
count = 0
attribute_array=["Gender", "First name", "Middle name", "Last name", 
"Initials", "Mother's Maiden name", "Birthday", "Birthplace", "Zodiacal sign", "User name", "Password", "Password hash (MD5)", "Password hash (SHA1)", "E-Mail", "Phone", "Address", "SSN", "PassportNo.", "Driver License", "Car", "Car License Plate", "Hair color", "Eyes color", 
"Height", "Weight", "Shoe Size", "Blood Type", "Religion", "Political side", "Favorite Color", "Favorite Comfort Food", "Favorite Cereal", 
"Favorite Season", "Favorite Animal", "Lucky Number", "Preparer Tax Identification Number (PTIN)", "Interim PTIN (temporary PTIN)", "Employer Identification Number (EIN)", "Individual Taxpayer Identification Number (ITIN)", "Adoption Taxpayer Identification Number (ATIN)"]
delete_me = open("delete_me.txt", "a")

for lines in header:
    count = count + 1
    if lines.name == 'td':
        attribute = lines.text
        if count < 2:
            delete_me.write(attribute)
delete_me.close()

delete_me = open("delete_me.txt", "r")
sock_puppet_file = open("sockpuppetfile.txt", "a")
count = 0
for line in delete_me:
    for x in attribute_array:
        if x in line:
            index = attribute_array.index(x)
            while count == index:
                output = attribute_formatter(x, line)
                print(output)
                sock_puppet_file.write(output)
                count = count + 1

delete_me.close()
os.remove("delete_me.txt")
print('\nOutput has been saved in the current directory as sockpuppetfile.txt')
