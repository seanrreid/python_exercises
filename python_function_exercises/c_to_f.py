#  F = (C * 9/5) + 32

user_input = int(input("Enter a temperature in Celsius: "))
user_input_2 = int(input("Enter a temperature in Fahrenheit"))

def convert_temp_f(celcius):
    return (celcius * 9/5) + 32

def convert_temp_c(fahrenheit):
    return (fahrenheit - 32 ) * 5/9

farhrenheit = convert_temp_f(user_input)
celcius = convert_temp_c(user_input_2)

print(farhrenheit)
print(celcius)