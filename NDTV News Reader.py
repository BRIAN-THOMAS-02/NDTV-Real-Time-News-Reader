import re
from bs4 import BeautifulSoup
import requests
import speech_recognition as sr
import playsound
import pyttsx3
import pyaudio
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print("")
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 165
engine.setProperty('rate', newVoiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get_audio():
    import speech_recognition as sr
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print(" ")
        print("Listening...")
        audio = rObject.listen(source, phrase_time_limit=5)

        try:
            text = rObject.recognize_google(audio, language='en-us')
            print("You said... :", str.capitalize(text))
            print(" ")
            return text

        except:
            print(" ")
            print("Could not understand you Brian, PLease try again !")
            speak("Could not understand you Brian, PLease try again !")
            print(" ")
            return 0


website = requests.get('https://www.ndtv.com/')
soup = BeautifulSoup(website.content, 'html.parser')
print(soup.title.string)


def news_top_scroll():
    #text = soup.find("h1").get_text()
    print("")
    print("-------------------------------------------------------------Top News-------------------------------------------------------------")
    speak("Top News")
    print("")
    print(soup.find('div', class_='cont_cmn big_mid').get_text())
    speak(soup.find('div', class_='cont_cmn big_mid').get_text())
    print(soup.find('div', class_='sponscont').get_text())
    speak(soup.find('div', class_='sponscont').get_text())
    print(soup.find('div', class_='comn_cnt').get_text())
    speak(soup.find('div', class_='comn_cnt').get_text())
    print(soup.find('div', class_='wid_stry').get_text())
    speak(soup.find('div', class_='wid_stry').get_text())
    print(soup.find('div', class_='shd_grd').get_text())
    speak(soup.find('div', class_='shd_grd').get_text())
    top_scroll_links = []
    for link in soup.findAll('a', attrs={'href': re.compile("topscroll")}):         #re.compile is for finding out text with common word "topscroll"
        top_scroll_links.append(link.get('href'))
        final_top_scroll_links = '\n'.join(top_scroll_links)
        top_scroll_list = final_top_scroll_links.split()
    print(top_scroll_list[0])


def big_stories():
    print("")
    print("-------------------------------------------------------------"+(soup.find('h2', class_='section_head').get_text())+"-------------------------------------------------------------")
    #speak(soup.find('h2', class_='section_head').get_text())
    print("")
    print(soup.find('div', class_='cont_cmn big-story-1227').get_text())
    speak(soup.find('div', class_='cont_cmn big-story-1227').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("bigstory")}):
        links.append(link.get('href'))
        final_links = '\n'.join(links)
        big_stories_list = final_links.split()                  #converting to list not spliting!!!!!
        x = big_stories_list[0]                                 #calling the first element in the list!!!
    print(x)


def top_stories():
    print("")
    print(
        "-------------------------------------------------------------Top Stories-------------------------------------------------------------")
    print("")
    print(soup.find('div', class_='featured_cont').get_text())                  #best way to extract specfic text
    speak(soup.find('div', class_='featured_cont').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("topstories")}):
        links.append(link.get('href'))
        final_top_stories_links = '\n'.join(links)
        top_stories_list = list(final_top_stories_links.split())
        s = top_stories_list[0]
    print(s)
    print("")


def li():
    for a in soup.findAll('div', class_='featured_cont'):
        a = a.get_text()
        print(a)


def opinion():
    print("")
    print(
        "-------------------------------------------------------------Opinion-------------------------------------------------------------")
    print("")
    #speak("Opinion")
    print(soup.find('div', class_='opinion_opt opinion-165').get_text())
    speak(soup.find('div', class_='opinion_opt opinion-165').get_text())
    #print(soup.find('div', class_='description').get_text())
    links = []
    for link in soup.findAll('a', attrs={'href': re.compile("ndtv_opinion")}):
        links.append(link.get('href'))
        opinion_links = '\n'.join(links)
        opinion_list = list(opinion_links.split())
        s = opinion_list[0]
    print(opinion_links)              #will give all the links
    #print(s)                         #will give only first link
    print("")

news_top_scroll()
big_stories()
top_stories()
#li()
opinion()