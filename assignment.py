
print("Hi! I'm a bot. What's your name?")

name = input("What's your name?: ")
print("You have a nice name.")


age = input("How old are you?: ")
print("So you are " + age + "." + " Nice!")


ques = input("Do you know you are running a python code?: ")
Yes = "yes"
No = "no"
if ques == Yes:
    print("That's nice, you're my python buddy now.")
else: 
    print("Oh, well this is called a python program.")

      
ques1 = input("Are you schooling?: ")
Yes = "yes"
No = "no"
if ques1 == Yes:
    print("Cool, what school do you attend?")
    ques2 = input("What's the name of your school?: ")
    ques3 = input("What are you studying?: ")
    print("Alright. It was nice knowing you " + name + "!" + " Have a nice day.")
else: 
     print("Alright then. It was nice knowing you " + name + "!" + " Have a nice day.")
    