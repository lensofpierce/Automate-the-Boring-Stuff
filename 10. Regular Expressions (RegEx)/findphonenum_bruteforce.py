# Find the presence of a phone number by brute force

def isPhoneNumber(text):    # 415-555-XXXX (US and Can Phone Numbers)
# Step 1: check for the number of characters (10 digits + 2 dashes)
    if len(text) != 12:
        return False
# Step 2: check for the validity of the area code (first 3 digits)
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
# Step 3: check for the presence of a dash
    if text[3] != '-':
        return False
# Step 4: do Step 2 and 3 for the remaining digits and dashes
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
        
# Step 5: confirm it is a phone number once all statements are satisfied

# Bonus: Create a message with two phone numbers
print('write a Phone Number: ')
phoneNum = input()
if isPhoneNumber(phoneNum) == True:
    print('Yes, it is.')
else:
    print('No.')
print('Write a message asking someone to call you at your Phone Numbers: ')

message = input()


# BS1: create a variable for finding the number that is initially false
foundNumber = False
# BS2: check every 12 digit chunk of characters starting from the first letter
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone Number found! It is: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('*meep morp* I cannot find any phone numbers. *_*')

# Tip: return True and return False are highly utilized in these programs
