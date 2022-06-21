import re

def validat_phone(phone):

    x = re.search("(^09[0-9]{9}$)", phone)

    if x:
        return True
    else:
        return False