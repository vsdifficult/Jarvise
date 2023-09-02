# Jarvise 1.0 

Первая версия голосового ассистента "Джарвис" реализованная на Python. 

Главнй блок кода в jarvice.py 
```
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
```
Так же есть начатая идея управления джарвисом через телеграм бота
