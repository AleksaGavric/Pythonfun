import random
import time
import webbrowser

# make a file which contains the links to be opened
randsite = open("links.txt", "r").read().splitlines()

def alarm_fun():
    # get alarm time
    al_time = input(">>>Enter alarm time (format H:M):  ")

    try:
        if al_time == "":
            al_time = input(">>>Please enter alarm time *(format H:M)*:  ")
        if al_time[0:2].isdecimal() and (al_time[3:]).isdecimal():
            print(">>>Alarm set. Please keep this window running if alarm hasn't yet gone off.")
    except ValueError:
        al_time = input(">>>Input alarm time (format H:M):  ")

    while True:
        now = time.strftime("%H:%M")
        if now == al_time:
            webbrowser.open(random.choice(randsite))
            break
    else:
        quit()


alarm_fun()
