import time
import datetime
from pygame import mixer
mixer.init()
mixer.music.set_volume(0.7)

def eye():
    with open("eyes.txt","a") as f:
        mixer.music.load("eyes.mp3")
        mixer.music.play()
        print(f.write("\n"+str(datetime.datetime.now())+" : "))
        print(f.write(input()))
        mixer.music.pause()
def water():
    with open("water.txt","a") as f:
        mixer.music.load("water.mp3")
        mixer.music.play()
        print(f.write("\n"+str(datetime.datetime.now())+" : "))
        print(f.write(input()))
        mixer.music.pause()
def exercise():
    with open("exercise.txt","a") as f:
        mixer.music.load("exercise.mp3")
        mixer.music.play()
        print(f.write("\n"+str(datetime.datetime.now())+" : "))
        print(f.write(input()))
        mixer.music.pause()
x=1
while x<8:
    for i in range(0,3):
        time.sleep(1)
        if i==0:
            print("Give some rest for your eyes")
            eye()
            time.sleep(2700)
        elif i==1:
             print("Take a break do some physical work")
             exercise()
             time.sleep(3600)
        elif i==2:
            print("Have some water")
            water()
        else:
            print("\n")
    x += 1
print("you have been working for 8 hrs go home and relax :)")
