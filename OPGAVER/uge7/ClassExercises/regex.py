import re
with open('./addresses.txt') as f:
    addresses = f.read()

# print(addresses)

# all names in the list above
namesList = re.compile(r'\^[a-zA-Z ]+$')
names = namesList.findall(addresses)
print('The names of persons: {}'.format(names))
# all telephone numbers
telephoneList = re.compile(r'\d{2} \d{2} \d{2} \d{2}')
phoneNumbers = telephoneList.findall(addresses)
print('These are the telephone numbers: {}'.format(phoneNumbers))
# all zip codes
# all city names with corresponding zip code
# all street names
