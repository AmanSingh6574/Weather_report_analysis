import requests
import pyttsx3
import time

speech=pyttsx3.init()


city_name=input("Enter the city name : \n")
API_key="ENTER YOUR API KEY"

url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
weather=requests.get(url)
weather_json=weather.json()


def callspeech():
    speech.runAndWait()
    time.sleep(1.2)

if weather_json['cod']=="404":
    print(f"Invalid city {city_name} : Plese check your city name")
    
else:
    temp_city=round(((weather_json['main']['temp'])-273.15),3)
    weather_discription=weather_json['weather'][0]['description']
    humidity=weather_json['main']['humidity']
    wind=weather_json['wind']['speed']
    timeperiod=time.asctime(time.localtime())

    speech.say(f"The weather forcasting for {city_name} is")
    callspeech()

    speech.say("time period")
    callspeech()
    print(timeperiod)
    speech.say(timeperiod)
    callspeech()
    print("----------------------------------------------------------")
    speech.say('weather status')
    speech.runAndWait()
    print(f"The weather states for {city_name} is : {weather_discription}")
    speech.say(f"The weather states for {city_name} is : {weather_discription}")
    callspeech()
    print("----------------------------------------------------------")
    speech.say("Temperature")
    speech.runAndWait()
    print(f"The temperature for {city_name} in deg cecilus is : {temp_city}")
    speech.say(f"The temperature for {city_name} in deg celcius is : {temp_city}")
    callspeech()
    print("----------------------------------------------------------")
    speech.say("humidity")
    speech.runAndWait()
    print(f"The humidity for {city_name} is : {humidity}")
    speech.say(f"The humidity for {city_name} is : {humidity}")
    callspeech()
    print("----------------------------------------------------------")
    speech.say("wind speed")
    speech.runAndWait()
    print(f"The wind speed for {city_name} is : {wind}")
    speech.say(f"The wind speed for {city_name} is : {wind}")
    callspeech()
    print("----------------------------------------------------------")
    speech.say("Thank you for using this python script")
    speech.runAndWait()


