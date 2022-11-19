"""
We wish to create a program that will help Beep and Bop find a way to escape.

The program should start by defining a function that has the name escape_by and which takes 1 parameter named plan.
The function should do the following:
    If the parameter plan has the value "jumping over" then the message "We cannot escape that way! The boulder is too big!"should be displayed.
   Otherwise if the parameter plan has the value "running around" then the message "We cannot escape that way! The boulder is moving too fast!" should be displayed.
    Otherwise if the parameter plan has the value "going deeper" then the message "That might just work! Let's go deeper!" should be displayed.
    Otherwise the message "We cannot escape that way! The boulder is in the way!" should be displayed.
Finally, the program should contain three calls to your escape function as follows:

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")        

An example run of such a program is shown below:

We cannot escape that way! The boulder is too big!
We cannot escape that way! The boulder is moving too fast!
That might just work! Let's go deeper!
"""


def escape_by(plan):

  if (plan == "jumping over"):
    print("We cannot escape that way! The boulder is too big!")
  elif (plan == "running around"):
    print("We cannot escape that way! The boulder is moving too fast!")
  elif (plan == "going deeper"):
    print("That might just work! Let's go deeper!")
  else:
    print("We cannot escape that way! The boulder is in the way!")


escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("xyz")