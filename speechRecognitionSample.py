#!/usr/bin/env python3                                                                                
import requests
import speech_recognition as sr 
import pyttsx3 
class demo():
    
    def recordVoice(self):
        r = sr.Recognizer()                                                                                                                                                        
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source) 
        return audio  
    def speechToText(self,audio):
        try:
            r = sr.Recognizer()
            op = r.recognize_google(audio)
            print("You said " + op)
        except sr.UnknownValueError:
            print("Could not understand audio")
            return
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return
        return op

    def rasaOutput(self,op):
        url = "http://localhost:5009/"
        payload = "{ \"sender\": \"default\", \"message\": \""+op+" \"}"
        print(payload)
        headers = {
            'Content-Type': "application/json",
            'Cache-Control': "no-cache"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)
        return response
    # lastp = response.text.replace(' ','_')
    # os.system("espeak -ven+f4 {} ".format(lastp))

    def textToSpeech(self,response):
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        engine.say(response.text)
        engine.runAndWait() 



    def run(self,forever = True):
        while forever:
            audio = self.recordVoice()
            if audio:
                data = self.speechToText(audio)
                if data:
                    response = self.rasaOutput(data)
                    self.textToSpeech(response)
                print("press ctrl+c to stop")

if __name__ == '__main__':
    samp =demo()
    samp.run()