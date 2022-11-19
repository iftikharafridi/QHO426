"""
We wish to create a program that listens for sounds in the cave.

The program should start by defining a function that has the name listen and which takes 0 parameters.
The function should do the following:
    Ask the user to enter a word representing a sound.
    Display the message "That was a loud" followed by the word entered by user and an exclamation mark.
Finally, the program should contain a call to your function listen

An example run of such a program is shown below:

What sound did I hear?
rumble

That was a loud rumble!

"""


# My listen function
def listen():
  # Display a message
  print("What sound did I hear")
  sound = input()  # Gettign input from a user
  # Displaying a message on screen
  print("That was a lound {}!".format(sound))


# Calling a function
listen()
print("Lets try again2")
listen()
print("Lets try again3")
listen()
print("Lets try again4")
listen()

