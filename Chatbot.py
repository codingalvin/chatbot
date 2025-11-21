#import libraries, set up ANSI escape and variable
import random,time,datetime
BOLD = '\033[1m'
END = '\033[0m'
go=True
  
#startup phrase
startgreetings=["Hello, this is Gary. Feel free to ask anything. ", "Hi!, How can I help you today? ","Welcome!, what can I do for you today? "]
print(BOLD+random.choice(startgreetings)+END)

while go:
#var setup
    userinput=input()
    output=""
    itisajoke=False
    idk=False

#leave
    checkleavecount=0
    findleave=["leave","exit","sleep","goodbye","bye","Bye","Sleep","shut","Shut"]
    for _ in findleave:
        if findleave[checkleavecount] in userinput:
            output="Bye and have a nice day!"
            go=False
        checkleavecount=checkleavecount+1

#favorite colour
    checkfavoritecount=0
    findfavorite=["favorite colour","Favorite colour","favourite colour","Favourite colour","Favourite color", "Favorite color","favorite color","favourite color"]
    for _ in findfavorite:
        if findfavorite[checkfavoritecount] in userinput:
            output="My favourite colour is blue, like the sky."
        checkfavoritecount=checkfavoritecount+1

#greetings
    checkgreetingcount=0
    findgreeting=["hi","Hi","hello","Hello","Hey","hey"]
    for _ in findgreeting:
        if findgreeting[checkgreetingcount] in userinput:
            greetingvocab=["Hi","Hello", "What's up?","How are you doing?" ]
            output=random.choice(greetingvocab)
        checkgreetingcount=checkgreetingcount+1

#time
    def timeprint():
        now = datetime.datetime.now()
        currenttime = now.strftime("%H:%M:%S")
        output="It is currently "+currenttime +"."
        return output

    checktimecount=0
    findtime=["time","time"]
    for _ in findtime:
        if findtime[checktimecount] in userinput:
             output=timeprint()
        checktimecount=checktimecount+1

#whomadeyou
    whomadeyou=["I am made by Alvin."]
    checkwhomadeyoucount=0
    findwhomadeyou=["who made you","Alvin","Who made you",]
    for _ in findwhomadeyou:
        if findwhomadeyou[checkwhomadeyoucount] in userinput:
            output=random.choice(whomadeyou)
        checkwhomadeyoucount=checkwhomadeyoucount+1    

#date
    def dateprint():
        now = datetime.datetime.now()
        currentdate = now.strftime("%A, %B %d")
        output="Today is "+currentdate +"."
        return output

    checkdatecount=0
    finddate=["date","date"]
    for _ in finddate:
        checkdate=finddate[checkdatecount]
        if checkdate in userinput:
             output=dateprint()
        checkdatecount=checkdatecount+1
        
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
    for _ in findfeeling:
        if findfeeling[checkfeelingcount] in userinput:
            output=feelingsprinting()
        checkfeelingcount=checkfeelingcount+1

#who
    who=["I am Gary, your personal assistant. ","This is Gary, your pal. "]
    checkwhocount=0
    findwho=["you","You","who are you","Who are you"]
    for _ in findwho:
        if findwho[checkwhocount] in userinput:
            output=random.choice(who)
        checkwhocount=checkwhocount+1

#joke
    checkjokecount=0
    findjoke=["joke","Jokes","Joke","Jokes"]
    for _ in findjoke:
        checkjoke=findjoke[checkjokecount]
        if checkjoke in userinput:
            itisajoke=True
        checkjokecount=checkjokecount+1

    if itisajoke:
        jokesquestions=["Why was Cinderealla so bad at Soccer?","What do you call a fish without an eye?"]
        jokesanswers=["She kept running away from the ball!","Fsh."]
        randomjokenumber=random.randint(0,len(jokesquestions)-1)#subtracted by 1
        print(BOLD+jokesquestions[randomjokenumber]+END)
        time.sleep(2)
        print(BOLD+jokesanswers[randomjokenumber]+" Haha!"+END)
#error message
    elif output=="":
        print(BOLD+"This is a very good response, but I need more detailed information from you."+END)
        idk=True
#outputprinting
    if itisajoke==False and idk==False:
        print(BOLD+output+END)
