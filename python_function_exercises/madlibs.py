def madlib(name, subject):
    the_madlib = "Your name is %s and your favorite subject is %s" % (name, subject)
    return the_madlib

my_story = madlib("Sean", "English")
print(my_story)