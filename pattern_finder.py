def isphonenumber(text):
    if  len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-' :
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-' :
        return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True
print('444-555-4242 is phone number: ')
print(isphonenumber('444-555-4242'))
print('joshi joshi is phone no. : ')
print(isphonenumber('joshi joshi'))

message = 'call me at 444-555-0090 tomorrow, if not 445-554-1000'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isphonenumber(chunk):
        print('phone no. found: '+ chunk)
print('done')


