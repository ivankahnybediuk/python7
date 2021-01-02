

"""
Task 1
A simple function
Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print “My favorite movie is named {name}”.
"""


def favorite_movie(movie):
    return f'My favorite movie is named "{movie}"'


def print_movie(string_to_print):
    print(string_to_print)


if __name__ == '__main__':
    your_movie = input('Enter name of your favorite movie \n')
    print_movie(favorite_movie(your_movie))

"""
Task 2
Creating a dictionary
Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys. Make the function print out the values of the dictionary to make sure that it works as intended.
"""


def make_country(name, capital):
    country_dict = {"name": name.capitalize(), "capital": capital.capitalize()}
    return country_dict


def print_country(country_dict):
    print(country_dict)


if __name__ == '__main__':
    print_country(make_country('Ukraine', 'Kyiv'))

"""
Task 3
A simple calculator.
Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
the call make_operation(‘+’, 7, 7, 2) should return 16
the call make_operation(‘-’, 5, 5, -10, -20) should return 30
the call make_operation(‘*’, 7, 6) should return 42
"""


def make_operation(operator, *args):
    count = args[0]
    for i in range(1, len(args)):
        if operator == "+":
            count += args[i]
        elif operator == "-":
            count -= args[i]
        elif operator == "*":
            count *= args[i]
    return count


if __name__ == '__main__':
    print(make_operation("+", 1, 2, 3))
    print(make_operation("-", 12, 3, 4, -1))
    print(make_operation("*", 2, 4, 3))