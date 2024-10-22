import random
import string

pass_length=12
charValues = string.ascii_letters + string.digits + string.punctuation
password= ""

#list comprehension
#res =.join([random.choice(charValues) for i in range(pass_len)])

for i in range(pass_length):
    password +=random.choice(charValues)

print("Your random password is",password)