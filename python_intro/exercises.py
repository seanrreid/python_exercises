numbers = [1, 2, 3, 4, 5, 99, 2600, 300]
test_stuff = "Sean"

print(numbers)
numbers.reverse()
print(numbers)

string_list = []
for letter in test_stuff:
    string_list.append(letter)
print(string_list)
string_list.reverse()
print(string_list)

new_string = ""
for letter in string_list:
    new_string += letter
print(new_string)
