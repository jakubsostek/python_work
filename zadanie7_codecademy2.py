def username_generator(first_name,last_name):
    if len(first_name) < 3:
        first_part = first_name
    else:
        first_part = first_name[0:3]

    if len(last_name) < 4:
        second_part = last_name
    else:
        second_part = last_name[0:4]

    return first_part + second_part

def password_generator(user_name):
    password = ""
    for i in range(len(user_name)): password += user_name[i-1]
    return password

print(password_generator("AbeSimp"))
