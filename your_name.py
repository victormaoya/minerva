
def capitalize_name(r_name):
    
    r_name_list = r_name.split()
    capitalized_name_list = []

    for name in r_name_list:
        capitalized_name = name.capitalize()
        capitalized_name_list.append(capitalized_name)

    return capitalized_name_list

def user_name_handle(l_name):
    user_name = l_name.lower()
    handle = '@'+user_name
    return handle


def details():

    raw_name = input('Enter Your Name: ')

    capitalized_name_list = capitalize_name(raw_name)
    
    first_name = capitalized_name_list[0]
    last_name = capitalized_name_list[-1]
    middle_name = ' '.join(capitalized_name_list[1:-1])
    user_name = user_name_handle(last_name)

    print(
        f'First Name: {first_name}\n',
        f'Midddle Name(s): {middle_name}\n',
        f'Surname: {last_name}\n'
        f'username: {user_name}'
    )

details()
