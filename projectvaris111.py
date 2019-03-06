#gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate’s text-to-speech 
#First we load all the required library for the implementation of javaris
from gtts import gTTS
#Library for performing speech recognition, so that it can decode the humman voice.2
import speech_recognition as sr
import os
#used pygame for opening a new window with the image of as the program opens..
import pygame
#This module provides regular expression matching operation
import re
#modules provide a high level interface to allow displaying web based documents
import webbrowser
import pyttsx
#used for javris to show time
import time
#used for sending mails..
import smtplib
engine = pyttsx.init()
# initialize game engine
# to have our game
pygame.init()
window_width=1200
window_height=1200
animation_increment=0
clock_tick_rate=0
# Open a window with given dimensions given.
size = (window_width, window_height)
screen = pygame.display.set_mode(size)
# Set title to the window
pygame.display.set_caption("Own Javaris")
#dead variable for game events..
dead=False
clock = pygame.time.Clock()
background_image = pygame.image.load("attach.jpg").convert()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def talkToMe(audio):
    "speaks audio passed as argument"
    speak(audio)
    print(audio)
#mycommand fucntion recognizes what i said if any occurs due to network issuse it raise exception.
def myCommand():
    "listens for commands"
    #Record Audio
    r = sr.Recognizer()
    #the same as in File Handling we open the file in the same way we allow microphone of system to open 
    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    #Speech recognition using Google Speech Recognition 
    #default API key r.recognize_google(audio,key=Google_speech_api_key)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

#from the mycommand function it return command what i said and perform the instruction on my requirement..
def assistant(command):
    #by using python time it will the time for you..
    if "show time" in command:
        apply=time.ctime()
        speak(apply)
     #it will open the website for you.   
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass

    elif 'How are you' in command:
        talkToMe('Just doing my thing')
    elif 'project' in command:
        speak("Opening Your Project Sir.")
        speak('Group Members are, Sitanshu Tripathi, Shubham Sinha, Shobhit Dixit, Vivek Vikram Singh and Javaris.')
        url="http://127.0.0.1:8000/"
        webbrowser.open(url)
        speak('Request Accepted Sir Openiing Your Project.')
    elif 'shutdown' in command:
        speak('ok sir')
        speak('closing all systems')
        speak('disconnecting to servers')
        speak('going offline')
        speak('Thank\'s  All')
        quit()
        
    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'tiger' in recipient:
            talkToMe('What is your message ?')
            content = myCommand()

            #init gmail SMTP
	        #Ports 465 and 587 are intended for email client to email server communication - sending email
            #587 sma should accept only after authentication
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('vivekvikram778@gmail.com', 'Jesus.Mary10')

            #send message
            mail.sendmail('Shobhit', 'shobhit00dixit@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent Sir  .')

        else:
            talkToMe('I don\'t know what you mean!')


		 
speak('I am ready for your command sir')
#loop to continue executing multiple commands
while(dead==False):
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
            dead = True
    screen.blit(background_image,[0, 0])
    pygame.display.flip()
    clock.tick(clock_tick_rate)
    #here we call assistant fn and pass mycommand as a agrument
    assistant(myCommand())
