#This program says hello and asks for my name

print ("Hello, World!")

print ("What is your name?") #ask for their name
myName = raw_input()
print ("It is good to meet you, " + myName)
print ("WThe length of your name is: ")
print (len(myName))

print ("What is your age?") # ask for their age
myAge = raw_input()
print ("You will be " + str(int(myAge) + 1 ) + " in a year.")