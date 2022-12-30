import random

character_set = range(33, 127)
password = ' '

for x in range(14):
    password += chr(random.choice(character_set))

print('Password is:', password)
