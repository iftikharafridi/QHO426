print("Program Started!")
print("Please enter a letter:")
character = input()
if (len(character) == 1):
  print("The ASCII code for {} is: {}".format(character, ord(character)))
else:
  print("Sorry input a single character")

print("Program Ended!")
