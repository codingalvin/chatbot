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
    checkleavelist=0
    leavelist=["leave","exit","sleep","goodbye","bye","Bye","Sleep","shut","Shut"]
    for x in leavelist:
        checkleave=leavelist[checkleavelist]
        if checkleave in userinput:
            output="Bye and have a nice day!"
            go=False
        checkleavelist=checkleavelist+1

#greetings
    def greetingprinting():
        greetingvocab=["Hi","Hello", "What's up","How are you doing" ]
        randomgreeting = random.choice(greetingvocab)
        output=randomgreeting
        return output
    
    checkgreetinglist=0
    greetinglist=["hi","Hi","hello","Hello","Hey","hey",]
    for x in greetinglist:
        checkgreeting=greetinglist[checkgreetinglist]
        if checkgreeting in userinput:
             output=greetingprinting()
        checkgreetinglist=checkgreetinglist+1

#clock
    def clockprint():
        now = datetime.now()
        currenttime = now.strftime("%H:%M:%S")
        output="It is currently"+currenttime +"."
        return output

    checkclocklist=0
    clocklist=["time","time"]
    for x in clocklist:
        checkclock=clocklist[checkclocklist]
        if checkclock in userinput:
             output=clockprint()
        checkclocklist=checkclocklist+1

#feeling
    def feelingsprinting():
        feelingvocab=["I am good","I am feeling wonderful", "I am doing amazing" ]
        feelingvocab2=["thanks", "how about you","hope your doing well too."]
        randomfeeling1 = random.choice(feelingvocab)
        randomfeeling2 = random.choice(feelingvocab2)
        output=randomfeeling1+", "+randomfeeling2
        return output

    if "Doing" in userinput:
        output=feelingsprinting()
    if "doing" in userinput:
        output=feelingsprinting()
    if "feeling" in userinput:
        output=feelingsprinting()
    if "Feeling" in userinput:
        output=feelingsprinting()
    if "how are you" in userinput:
        output=feelingsprinting()
    if "How are you"in userinput:
        output=feelingsprinting()   

#who
    who=["I am Gary, your personal assistant. ","This is Gary, your pal. "]
    checkwholist=0
    wholist=["you","You","who are you","Who are you"]
    for x in wholist:
        checkwho=wholist[checkwholist]
        if checkwho in userinput:
            randomwho = random.choice(who)
            output=randomwho
        checkwholist=checkwholist+1
 
#joke
    checkjokelist=0
    jokelist=["joke","Jokes","Joke","Jokes"]
    for x in jokelist:
        checkjoke=jokelist[checkjokelist]
        if checkjoke in userinput:
            itisajoke=True
        checkjokelist=checkjokelist+1

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