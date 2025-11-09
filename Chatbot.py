import random
import time
from datetime import datetime
BOLD = '\033[1m'
END = '\033[0m'



def greeting():
    def greetingprinting():
        greetingvocab=["Hi","Hello", "What's up","How are you doing" ]
        randomgreeting = random.choice(BOLD+greetingvocab+END)
        print(randomgreeting)
    
    if "hi" in userinput:
        greetingprinting()
    elif "Hi" in userinput:
        greetingprinting()
    elif "Hello" in userinput:
        greetingprinting()
    elif "hello" in userinput:
        greetingprinting()
    elif "Hey" in userinput:
        greetingprinting()
    elif "hey" in userinput:
        greetingprinting()


def clock():
    def clockprint():
        now = datetime.now()
        currenttime = now.strftime("%H:%M:%S")
        print("It is currently", currenttime ,".")

    if "time" in userinput:
        clockprint()
    elif "Time" in userinput:
        clockprint()

def who():
    who=["I am Gary, your personal assistant. ","This is Gary, your pal. "]
    if "you" in userinput:
        randomwho = random.choice(who)
        print(BOLD+randomwho+END)

    if "You" in userinput:
        randomwho = random.choice(who)
        print(BOLD+randomwho+END)

def joke():
    def jokeprinting():
        jokesquestions=["Why was Cinderealla so bad at Soccer?","What do you call a fish without an eye?"]
        jokesanswers=["She kept running away from the ball!","Fsh."]
        randomjokenumber=random.randint(0,1)
        randomjokequestion=jokesquestions[randomjokenumber]
        randomjokeanswer=jokesanswers[randomjokenumber]
        print(BOLD+randomjokequestion+END)
        time.sleep(2.5)
        print()
        print(BOLD+randomjokeanswer," Haha!"+END)

    if "joke" in userinput:
        jokeprinting()
    if "Joke" in userinput:
        jokeprinting()
    if "Jokes" in userinput:
        jokeprinting()
    if "jokes" in userinput:
        jokeprinting()
        

def feelings():
    def feelingsprinting():
        feelingvocab=["I am good","I am feeling wonderful", "I am doing amazing" ]
        feelingvocab2=["thanks", "how about you","hope your doing well too."]
        randomfeeling1 = random.choice(feelingvocab)
        randomfeeling2 = random.choice(feelingvocab2)
        print(BOLD + randomfeeling1,", ",randomfeeling2 + END)

    if "Doing" in userinput:
        feelingsprinting()
        
    if "doing" in userinput:
        feelingsprinting()
        
    if "feeling" in userinput:
        feelingsprinting()
        
    if "Feeling" in userinput:
        feelingsprinting()
        
    if "how are you" in userinput:
        feelingsprinting()
        
    if "How are you"in userinput:
        feelingsprinting()
        

def iam():
    splitedinput=""
    splitedinput=userinput.split()
    if "I" in splitedinput:
        splitedinput.remove("I")
    if "i" in splitedinput:
        splitedinput.remove("i")
    if "am" in splitedinput:
        splitedinput.remove("am")
    if "My" in splitedinput:
        splitedinput.remove("My")
    if "my" in splitedinput:
        splitedinput.remove("my")
    if "name" in splitedinput:
        splitedinput.remove("name")
    if "is" in splitedinput:
        splitedinput.remove("is")
    print(BOLD+splitedinput+END)
        
 



startgreetings=["Hello, this is Gary. Feel free to ask anything. ", "Hi!, How can I help you today? ","Welcome!, what can I do for you today? "]
randomgreet = random.choice(startgreetings)

print(BOLD+randomgreet+END)

while True:
    userinput=input("Type here")
    greeting()
    clock()
    who()
    joke()
    feelings()
 





