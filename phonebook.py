import json
import uuid

user_id = uuid.uuid4()
def add_new_entrie():
    user = {'first_name': input('Enter a First name: ').lower(),
            'last_name': input('Enter a Last name: ').lower(),
            'phone_number': input('Enter a phone number: '),
            'city': input('Enter the city: ').lower()}
    new_data = read_file()
    new_data.update({str(user_id): user})
    write_file(new_data)

def search_result(a):
    new_x = search(a)
    if new_x is None:
        print('Sorry, user is not found!')
    else:
        print('Here you are!', new_x)

def search(a):
    my_file = read_file()
    x = input(f'Enter the {a} to search: '.replace('_', ' ')).lower()
    if a == 'full_name':
        for v in my_file.values():
            full_name = v['first_name'] + ' ' + v['last_name']
            if x == full_name:
                return v
    else:
        items = []
        for v in my_file.values():
            if x == v[a]:
                items.append(v)
        return items

def delete_record(a):
    my_file = read_file()
    x = input(f'Enter the {a} to delete: '.replace('_', ' '))
    if a == 'phone_number':
        for k, v in my_file.items():
            if x == v[a]:
                my_file.pop(k)
                write_file(my_file)

def update_record(a):
    my_file = read_file()
    x = input(f'Enter the {a} to update: '.replace('_', ' '))
    if a == 'phone_number':
        for k, v in my_file.items():
            if x == v[a]:
                y = input(f'Enter new {a} : '.replace('_', ' '))
                print('ok!', k, v)
                v[a] = y
                write_file(my_file)

def read_file():
    try:
        with open('Phonebook.txt') as file:
            temp_file = file.read()
            if temp_file == '':
                return {}
            data = json.loads(temp_file)
            return data
    except FileNotFoundError:
        print('Sorry, but the Phonebook is absent!')
        return {}

def write_file(new_data):
    with open('Phonebook.txt', 'w') as file:
        json.dump(new_data, file)

def exit_phonebook():
        with open('Phonebook.txt') as file:
            file.close()
            print('See you soon!')

def main():
    print('1-add_new_entries',
          "2-search_by_first_name",
          "3-search_by_last_name",
          "4-search_by_full_name",
          "5-search_by_telephone_number",
          "6-search_by_city",
          "7-del_by_number",
          "8-update_by_number",
          'exit-for exit',
          sep ='\n')
    x = input('Choose the operation from the list: ')
    if x == '1':
        add_new_entrie()
    elif x == '2':
        search_result('first_name')
    elif x == '3':
        search_result('last_name')
    elif x == '4':
        search_result('full_name')
    elif x == '5':
        search_result('phone_number')
    elif x == '6':
        search_result('city')
    elif x == '7':
        delete_record('phone_number')
    elif x == '8':
        update_record('phone_number')
    elif x.lower() == 'exit':
        exit_phonebook()

main()