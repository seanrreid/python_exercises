title = "G reen Lantern Corp"
# STOP = 10
# This next variable will increment
counter = 0

while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter += 1
