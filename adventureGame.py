
# Update this text to match your story.
start = '''
Fireboy and Watergirl are stuck in Mt.Everest, they are looking for a way out
before Fireboy fizzes out and Watergirl freezes, help them get home!
'''

print(start)

start = "How do they get to the other side: up or through?"
print("Type 'up' to go up or 'through' to go through.") # Update to match your story.
user_input = input()
if user_input == "up":
    print("Fireboy:'OH NO! WE WENT TOO FAR UP!'") # Update to match your story.
    print("Watergirl:'NOW WE'RE IN SPACE!'")
    print("*both die without proper oxygen*")

elif user_input == "through":
    start = '''
    You choose to go through and the siblings go through the mountain into
    this dark cave.
    '''
    print("Watergirl:'It's so dark and cold in here.'")
    print("Fireboy:'Oh look, a fortune cookie!'")
    print("Watergirl:*picks up cookie and reads fortune* (The fortune is the way out!)")
while(user_input != "up" and user_input != "through"):
    print("Sorry, that isn't a valid input. Try again:")
    user_input=input()

start = '''
It's up to you, the player, to guess a number from 1 to 5 to get the
siblings home. Wrong number and they'll be stuck in the cave forever!
'''
choice = 3
userGuess = input("put in a number")
userGuess = int(userGuess)
while (userGuess != choice):
    print("Try again.")
    userGuess = input()
    userGuess = int(userGuess)
    #print (userGuess)
if (userGuess == choice):
    print("Correct!Lucky guess... they can go home now.")
