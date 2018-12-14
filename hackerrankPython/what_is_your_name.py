def print_full_name(a, b):
    if len(a) <= 10 and len(b) <= 10:
        print('Hello {} {}! You just delved into python.'.format(a,b))

if __name__ == '__main__':
    first_name = input('What is your first name : ')
    last_name = input('What is your last name : ')
    print_full_name(first_name, last_name)