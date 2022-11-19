print("Program Started!")
print("Please enter an ASCII code:")
code = int(input())  #This will convert the string to integer

# The program should then check that the number is in the range 32 - 126 (inclusive) i.e. the printable characters.  You should use the keyword in and the built-in function range to help you with this.
# Version-1
"""
if (code >= 32 and code <= 126):
  print("The character represented by the ASCII code {} is: {}".format(
    code, chr(code)))
else:
  print("Sorry input a given range")
"""
# Version -2
# use of in and range
# range1 = range(5) # This will return a sequence of number starting from 0 upto 4 with increment of 1
# 0,1,2,3,4
# range2 = range(1,8) This will return a sequence of number starting from 1 upto 7 with increment of 1
# range3 = range(4, 10, 2) This will return a sequence of number starting from 4 upto 9 with increment of 2
# 4, 6, 8
# range(start, stop, step) # stop-1
print("The character represented by the ASCII code {} is: {}".format(
  code, chr(code)))

print("Lives: {}".format(chr(code) * 10))

if (code in range(32, 127)):
  print("The character represented by the ASCII code {} is: {}".format(
    code, chr(code)))
else:
  print("Sorry input a given range")

print("Program Ended!")
