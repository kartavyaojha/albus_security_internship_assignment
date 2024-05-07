import secrets
import string

letters=string.ascii_letters
digits=string.digits
special_char=string.punctuation

selection_list=letters+digits+special_char

pass_len=12
password=""
for i in range(pass_len):
    password+=''.join(secrets.choice(selection_list))

print("generated pass:",password)
