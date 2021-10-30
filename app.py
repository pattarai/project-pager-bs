from flask import Flask, request
from flask.helpers import send_from_directory
import os, requests, json

app = Flask(__name__, static_url_path='', static_folder='.')
app.config['CORS_HEADERS'] = 'Content-Type'

# CORS section
@app.after_request
def after_request_func(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response
# end CORS section

import error_handles

# Add your API endpoints here
from routes import users
# from routes import cars
# ...

@app.route('/')
def get_endpoint_function():
    try:
        res = "<h1 style='position: fixed; top: 50%;  left: 50%; transform: translate(-50%, -50%);'>FLASK API HOME</h1>"
        return res

    except Exception as e:
        print(e)


# Send message to discord
@app.route('/message', methods=['GET'])
def send_message():
    try:
        message = request.args["display"] 
        listOfNode = ['192.168.1.25', '192.168.1.25','192.168.1.25']
        
        # Try and connect to the board
        try:
            repl=webrepl.Webrepl(**{'host':'192.168.1.25','port':8266,'password':'mark360'})
            
            try:
                # Setting up the board for OLED Display
                resp=repl.sendcmd("from machine import Pin, SoftI2C; import ssd1306; from time import sleep; i2c = SoftI2C(scl=Pin(5), sda=Pin(4)); oled_width = 128; oled_height = 64; oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c); ")
                print(resp)

                # Send OLED Message
                resp=repl.sendcmd(f"oled.text('{message}', 0, 0); oled.show()")
                return "Successfully Displayed in OLED"

            except Exception as e:
                print(e)
                return "Command Failed to Execute"

        except Exception as e:
            print(e)
            return "WebREPL connection failed"

    except Exception as e:
        print(e)
        return "Invalid Request Parameters"

# Setting Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)
