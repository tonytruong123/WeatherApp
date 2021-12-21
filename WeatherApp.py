import tkinter as tk #for the gui: to create the theme for the canvas
from tkinter import Label
import time #format some variable
import requests #for the js
from PIL import Image, ImageTk


#  https://openweathermap.org/current
#   my api: 99256fdd85c6de79b3ccdbc3bb18eca7, 12d02cb722709709e0889db756957fca

def getWeather(canvas):
    #get the input from the user
    city = fieldtext.get()
    #api from the website, 2 inputs: api key and the city
    api ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=12d02cb722709709e0889db756957fca"
    #JSON is a syntax for storing and exchanging data.
    # https://www.delftstack.com/howto/python/python-get-json-from-url/#:~:text=Get%20and%20Access%20JSON%20Data%20in%20Python%201,format.%20...%203%20Access%20the%20JSON%20Data.%20
    # The first step we have to perform here is to fetch the JSON data using the requests library.
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    min_temp = int(json_data['main']['temp_min'] -273.15)   
    max_temp = int(json_data['main']['temp_max'] -273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['pressure']
    wind_speed = json_data['wind']['speed']
    #strftime: Convert a time tuple to a string according to a format specification
    # %I:%M:%M: hours minute seconds in 12 hour format
    # %H:%M:%M: hours minute seconds in 24 hour format
    sunrise = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%M", time.gmtime(json_data['sys']['sunset'] - 21600))
    
    #we will define two strings to carry our data
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind_speed) + "\n" + "Sun Rise: " + str(sunrise)  + "\n"  + "Sun Set: " + str(sunset) 
    
    #config is used to access an object's attributes after its initialisation.
    # config is used to access an object's attributes after its initialisation. For example, here, you define
    # l = Label(root, bg="ivory", fg="darkgreen")
    # but then you want to set its text attribute, so you use config:
    #l.config(text="Correct answer!")
    label1.config(text = final_info)
    label2.config(text = final_data)
    
canvas = tk.Tk()
canvas.title("Weather App")
canvas.geometry("700x600")
canvas.config(bg = 'White')

# For single widgets, the answer is no: you cannot use both pack() and grid() inside one widget. But you can use both for different widgets, even if they are all inside the same widget. For instance:

# my_canvas=tk.Canvas(window1,width=540,height=420,bd=0)
# my_canvas.create_image(270,210,image=bg,anchor="center")
# my_canvas.pack(fill="both",expand=True)            
# originallbl = tk.Label(my_canvas, text="Original", width=15).grid(row=1,column=1)
# original = tk.Entry(my_canvas, width=15).grid(row=1,column=2)

img = Image.open("C:/Users/Tony Truong/Documents/PythonProject/weatherpicture.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)
Label(canvas, image = img, bg="white").pack()

#poppins is a type of font
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

fieldtext = tk.Entry(canvas, justify = 'center', font = t)
#The pack() geometry manager organizes widgets in blocks before placing them in the parent widget
fieldtext.pack(pady = 20)
#focus on the input from the user. The user does not need to move the cursor to type in
fieldtext.focus()
#on every enter hit, we will call the function to display the weather info of the input city
fieldtext.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()