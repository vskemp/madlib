# Prompt the user for the missing words to a Madlib sentence using the input function. You will make up your own Madlib sentence, but here's an example:

# ____(name)____'s favorite subject in school is ____(subject)____.
# With the above given sentence, this is what a user session might look like:

# $ python madlib.py
# Please fill in the blanks below:
# ____(name)____'s favorite subject in school is ____(subject)____.
# What is name? Marty
# What is subject? math
# Marty's favorite subject in school is math.

print("Please fill in the blanks below:")
mad_name = input("What is name? ")
mad_subject = input("What is subject? ")
print((mad_name) + "'s favorite subject in school is " + (mad_subject) + ".")

