def return_10():
    return 10

def add(first_number, second_number):
    return first_number + second_number
    

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def length_of_string(string):
    string = "A string of length 21"
    string_length = len(string)
    return string_length

def join_string(string_1, string_2):
    string_1 = "Mary had a little lamb, "
    string_2 = "its fleece was white as snow"
    joined_string = string_1 + string_2
    return joined_string

def add_string_as_number(first_number, second_number):
    return int(first_number) + int(second_number)

def number_to_full_month_name(number_of_month):
    months = {
        1 : "January",
        2 : "February",
        3 : "March",
        4 : "April",
        5 : "May",
        6 : "June",
        7 : "July",
        8 : "August",
        9 : "September",
        10 : "October",
        11 : "November",
        12 : "December",
    }
    result = months[number_of_month]
    return result

def number_to_short_month_name(month_number):
    months_shortened = {
        1 : "Jan",
        2 : "Feb",
        3 : "Mar",
        4 : "Apr",
        5 : "May",
        6 : "Jun",
        7 : "Jul",
        8 : "Aug",
        9 : "Sep",
        10 : "Oct",
        11 : "Nov",
        12 : "Dec",
    }
    result = months_shortened[month_number]
    return result

##Extension

def volume_of_cube(length_of_cube):
    result = length_of_cube * length_of_cube * length_of_cube
    return result

def reversed_string(forward_string):
    reversed_text = forward_string[::-1]
    return reversed_text

def fahrenheit_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp-32) * 5/9







