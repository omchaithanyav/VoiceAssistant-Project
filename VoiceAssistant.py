import speech_recognition as sr 
import playsound 
import os
from gtts import gTTS 
from selenium import webdriver
import wolframalpha
import pyjokes
from datetime import datetime
import cv2
from PIL import Image
import time


num = 1
def voice(output):
    global num
  
    num += 1
    print("Siya: ", output)
  
    toSpeak = gTTS(text = output, lang ='en', slow = False)
    
    file = str(num)+".mp3" 
    toSpeak.save(file)
      
    playsound.playsound(file, True) 
    os.remove(file)
    
    
    
def getting_audio():
  
    rObject = sr.Recognizer()
    audio = ''
  
    with sr.Microphone() as source:
        print("Say something")
          
        audio = rObject.listen(source, phrase_time_limit = 4) 
  
    try:
        text = rObject.recognize_google(audio, language ='en-US')
        print("user: ", text)
        return text
  
    except:
  
        voice("Sorry, I Could not understand ,PLease do try again !")
        return 0
    



def open_application(input):
  
    if "chrome" in input:
        voice("Opening Google Chrome")
        os.startfile(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Chrome')
        return
    
    elif "spyder" in input:
        voice("Opening Spyder")
        os.startfile(r'C:\Users\apega\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anaconda3 (64-bit)\Spyder (Anaconda)')
        return
    
    elif "brave" in input or "Browser" in input:
        voice("Opening Brave Browser")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave')
        return
  
    elif "discord" in input:
        voice("Opening discord")
        os.startfile(r'C:\Users\apega\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord')
        return
    
    
    elif "whats app" in input or "whatsapp" in input:
        voice("Opening WhatsApp")
        os.startfile(r'C:\Users\apega\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\WhatsApp\WhatsApp')
        return
    
  
    else:
  
        voice("Application not found")
        return




def close_application(input):
  

    
    if "spyder" in input:
        voice("Closing Spyder")
        os.system("taskkill /f /im Spyder (Anaconda).exe")
        return

    elif "chrome" in input:
        voice("Closing Chrome Browser")
        os.system("taskkill /f /im Chrome.exe")
    
    elif "brave" in input or "Browser" in input:
        voice("Closing Brave Browser")
        os.system("taskkill /f /im Brave.exe")
  
    elif "discord" in input:
        voice("Closing discord")
        os.system("taskkill /f /im Discord.exe")
        return
    elif "whats app" in input or "whatsapp" in input:
        voice("Closing WhatsApp")
        os.system("taskkill /f /im WhatsApp.exe")
        return
    
  
    else:
  
        voice("Application is not found opened")
        return



def shut_down(input):
    voice("bye bye")
    os.system("shutdown /s /t 1")


def restart(input):
    voice("restarting Windows")
    os.system("shutdown /r /t 1")


def capture(input):
        camera = cv2.VideoCapture(0)
        for i in range(1):
            return_value, image = camera.read()
            contrast = 0
            brightness = 100
            cv2.imwrite('new_image'+str(i)+'.png', image)
            im = Image.open(r"new_image0.png") 
            im.show()
        del(camera)
        
        
        
def record(input):       
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
           voice("Recording stoped")
           break
    vid.release()
    cv2.destroyAllWindows()


def sleep(input):
    voice("Going to sleep mode")
    time.sleep(10)
    voice("Terminating sleep mode")
    

def translate(input):
    from googletrans import Translator
    translator = Translator()
    voice((translator.translate(input.lower()[18:], dest = 'hi')).text)    


def search(input):
  
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
  
    if 'youtube' in input.lower():
  
        voice("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return
  
    elif 'wikipedia' in input.lower():
  
        voice("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return
  
    else:
  
        if 'google' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        elif 'search' in input:
  
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))
  
        else:
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))
  
        return



def input_given(input):
    try:
        if 'search' in input.lower() or 'play' in input.lower():
        
            search(input.lower())
            return
  
        elif "who are you" in input:
            speak = "Hey, i am Siya, your personal voice assistant, I am here to help your with your tasks."
            voice(speak)
            return
        
        elif "who developed you" in input or "who created you" in input:
            voice("I have been developed by a Data Scientist named Om Chaithanya Vuppalapati")
            return
  
        elif "siri" in input.lower() or "google assistant" in input.lower():
            speak = "hmmm... technically they are my competitors."
            voice(speak)
            return
        
        elif "who is your boyfriend" in input or "who is your girlfriend" in input or "are you single" in input:
            speak = "i am happily single."
            voice(speak)
            return
        
        elif "excuse me" in input:
            speak = "you are excused"
            voice(speak)
            return
        
        
        elif "speak tamil" in input.lower() or "know tamil" in input.lower() or "understand tamil" in input.lower():
            speak = "aama thala enaku tamil pesaradu teriyum"
            voice(speak)
            return
        
        
        elif 'joke' in input.lower():
            speak = pyjokes.get_joke()
            voice(speak)
            return
        
        elif "mail" in input.lower() or "email" in input.lower():
            speak = "Sorry, i am not yet capable to perform this function"
            voice(speak)
            return
        
        elif 'shut down' in input.lower():
            voice("Shuting Down your Device")
            shut_down(input.lower())
            return
        
        elif 'restart' in input.lower():
            voice("Restarting your Device")
            restart(input.lower())
            return

        
        elif 'capture' in input.lower():
            voice("capturing image")
            capture(input.lower())
            voice("image captured and saved.")
            return
        
        elif 'record' in input.lower():
            voice("starting to record")
            record(input.lower())
            return

        elif "sleep" in input.lower() or 'rest' in input.lower():
            sleep(input)
            return
        
        elif "translate to hindi" in input.lower():
            voice("ok, translating.")
            translate(input)
            return


        elif "calculate" in input.lower():

            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            voice("The answer is " + answer)
            return

        elif 'time' in input.lower():
            now = datetime.now()
            speak = 'The current time is %d hours %d minutes' % (now.hour, now.minute)
            voice(speak)
            return

        elif 'today' in input.lower():
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            now = datetime.now()
            day = days[now.weekday()]
            voice(day)
            
  
        elif 'open' in input.lower():
              
            open_application(input.lower()) 
            return
        
        elif 'close' in input.lower():
              
            close_application(input.lower()) 
            return
        
        
        else:
  
            voice("I can search the web for you, Do you want to continue?")
            ans = getting_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search(input)
            else:
                return
            
        
    except :
  
        voice("sorry, I don't understand, you want me to search in web ?")
        ans = getting_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search(input)
            
            
class MyAssistant():
    
    if __name__ == "__main__":
        
        
        voice("Hi i am Siya, your personal voice assistant, What should i call you ?")
        name = getting_audio()

        try:
            if "I am" in name[0:4]:
                voice("Hello " + str(name[5:]) + '.')

            elif "call me" in name[0:7]:
                voice("Hello " + str(name[8:]) + '.')

            elif "you can call me" in name[0:15]:
                voice("Hello " + str(name[16:]))


            elif name != 0:
                voice("Hello " + str(name) + '.')

            else:
                voice("Hello")

        except:
            voice("Hello")
              
        while(1):
          
                voice("How can i help you?")
                text = getting_audio()
      
                if text == 0:
                    continue
      
                elif "exit" in str(text) or "bye" in str(text) or "stop" in str(text) or "terminate" in str(text):
                    voice("bye buddy, "+ "have a great time"+'.')
                    break
            
                else:
                    input_given(text)
       
    
    
