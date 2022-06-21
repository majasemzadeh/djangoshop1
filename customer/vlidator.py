import re


def validat_phone(phone):

    x = re.search("(^09[0-9]{9})", phone)
    print(x)
    if x:
        return True
    else:
        return False


def convert_phone(phone):
    phone = str(phone)
    phone1 = ''
    for i in phone:
        if i=='۰':
            phone1 += '0'
        elif i== '۱':
            phone1 += '1'
        elif i== '۲':
            phone1 += '2'
        elif i== '۳':
            phone1 += '3'
        elif i== '۴':
            phone1 += '4'
        elif i== '۵':
            phone1 += '5'
        elif i== '۶':
            phone1 += '6'
        elif i== '۷':
            phone1 += '7'
        elif i== '۸':
            phone1 += '8'
        elif i== '۹':
            phone1 += '9'
        else:
            return False
        phone = int(phone1)
        x = re.search("(^09[0-9]{9})", phone)
        print(x)
        if x:
            return True
        else:
            return False