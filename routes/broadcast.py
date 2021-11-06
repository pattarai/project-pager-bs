import pymysql
from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request


# Send Broadcast
@app.route('/message', methods=['GET'])
def send_message():
    try:
        message = request.args["display"]
        listOfNodes = [{"address": '192.168.1.25', "state": "WAIT"}, {
            "address": '192.168.1.30', "state": "WAIT"}, {"address": '192.168.1.25', "state": "WAIT"}]

        for node in listOfNodes:
            # Try and connect to the board
            try:
                repl = webrepl.Webrepl(
                    **{'host': node["address"], 'port': 8266, 'password': 'mark360'})

                try:
                    # Setting up the board for OLED Display
                    resp = repl.sendcmd(
                        "from machine import Pin, SoftI2C; import ssd1306; from time import sleep; i2c = SoftI2C(scl=Pin(5), sda=Pin(4)); oled_width = 128; oled_height = 64; oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c); ")
                    print(resp)

                    # Send OLED Message
                    resp = repl.sendcmd(
                        f"oled.text('{message}', 0, 0); oled.show()")
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
