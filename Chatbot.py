#import libraries, set up ANSI escape and variable
import random
import time
from datetime import datetime
BOLD = '\033[1m'
END = '\033[0m'
go=True

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
        
#startup phrase
startgreetings=["Hello, this is Gary. Feel free to ask anything. ", "Hi!, How can I help you today? ","Welcome!, what can I do for you today? "]
randomgreet = random.choice(startgreetings)
print(BOLD+randomgreet+END)

while go==True:
#var setup
    userinput=input()
    output=""
    itisajoke=False
    idk=False

#leave
    checkleavecount=0
    findleave=["leave","exit","sleep","goodbye","bye","Bye","Sleep","shut","Shut"]
    for x in findleave:
        checkleave=findleave[checkleavecount]
        if checkleave in userinput:
            output="Bye and have a nice day!"
            go=False
        checkleavecount=checkleavecount+1

#greetings
    def greetingprinting():
        greetingvocab=["Hi","Hello", "What's up","How are you doing" ]
        randomgreeting = random.choice(greetingvocab)
        output=randomgreeting
        return output
    
    checkgreetingcount=0
    findgreeting=["hi","Hi","hello","Hello","Hey","hey",]
    for x in findgreeting:
        checkgreeting=findgreeting[checkgreetingcount]
        if checkgreeting in userinput:
             output=greetingprinting()
        checkgreetingcount=checkgreetingcount+1

#clock
    def clockprint():
        now = datetime.now()
        currenttime = now.strftime("%H:%M:%S")
        output="It is currently"+currenttime +"."
        return output

    checkclockcount=0
    findclock=["time","time"]
    for x in findclock:
        checkclock=findclock[checkclockcount]
        if checkclock in userinput:
             output=clockprint()
        checkclockcount=checkclockcount+1

#feeling
    def feelingsprinting():
        feelingvocab=["I am good","I am feeling wonderful", "I am doing amazing" ]
        feelingvocab2=["thanks", "how about you","hope your doing well too."]
        randomfeeling1 = random.choice(feelingvocab)
        randomfeeling2 = random.choice(feelingvocab2)
        output=randomfeeling1+", "+randomfeeling2
        return output

    checkfeelingcount=0
    findfeeling=["doing","Doing","feeling","Feeling","how are you", "How are you"]
    for x in findfeeling:
        checkfeeling=findfeeling[checkfeelingcount]
        if checkfeeling in userinput:
            output=feelingsprinting()
        checkfeelingcount=checkfeelingcount+1

#who
    who=["I am Gary, your personal assistant. ","This is Gary, your pal. "]
    checkwhocount=0
    findwho=["you","You","who are you","Who are you"]
    for x in findwho:
        checkwho=findwho[checkwhocount]
        if checkwho in userinput:
            randomwho = random.choice(who)
            output=randomwho
        checkwhocount=checkwhocount+1
 
#joke
    checkjokelist=0
    findjoke=["joke","Jokes","Joke","Jokes"]
    for x in findjoke:
        checkjoke=findjoke[checkjokelist]
        if checkjoke in userinput:
            itisajoke=True
        checkjokecount=checkjokecount+1

    if itisajoke==True:
        jokesquestions=["Why was Cinderealla so bad at Soccer?","What do you call a fish without an eye?"]
        jokesanswers=["She kept running away from the ball!","Fsh."]
        randomjokenumber=random.randint(0,1)
        randomjokequestion=jokesquestions[randomjokenumber]
        randomjokeanswer=jokesanswers[randomjokenumber]
        print(BOLD+randomjokequestion+END)
        time.sleep(2.5)
        print(BOLD+randomjokeanswer+" Haha!"+END)
#error message
    elif output=="":
        print(BOLD+"This is a very good response, but I need more detailed information from you."+END)
        idk=True
#outputprinting
    if itisajoke==False and idk==False:
        print(BOLD+output+END)