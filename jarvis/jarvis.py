from mains.system import start_opera, start_telegram,discord,  start_visual_studio, github, sys_shot_down
from configs.comm import commands 

import os, sys, shutil, telebot 
import speech_recognition as sr 

r = sr.Recognizer()

# Устанавливаем источник звука на микрофон 
mic = sr.Microphone()
    
def main(reg, micro): 
    
# Записываем звук с микрофона
    with micro as source:
    # Подстраиваем уровень шума
       reg.adjust_for_ambient_noise(source)
    
       while True:
        # Слушаем и распознаем речь
          audio = reg.listen(source)
        
          try:
            # Распознаем речь
            text = reg.recognize_google(audio, language="ru")
            print("Распознанный текст:", text)  
            
            for text in commands: 
                if text == "Выключи компьютер": 
                    sys_shot_down() 
                
                elif text == "github":  
                    github() 
                    
                elif text == "гитхаб": 
                    github() 
                    
                elif text =="Github": 
                    github() 
                    
                elif text == "Гитхаб": 
                    github()          
                
                elif text == "Запусти Telegram": 
                    start_telegram() 
                    
                elif text == "Telegram": 
                    start_telegram() 
                
                elif text == "Запусти Оперу": 
                    start_opera() 
                
                elif text == "Запусти Visual Studio": 
                    start_visual_studio() 
                
                elif text == "Запусти vs": 
                    start_visual_studio() 
                    
                elif text == "Запусти VS": 
                    start_visual_studio()  
                
                elif text == "Запусти discord": 
                    discord() 
                
                elif text == "Запусти дискорд": 
                    discord() 
          except: 
                return "er"

            

if __name__ == "__main__": 
    main(r, mic)