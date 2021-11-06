from app import app
from error_handles import forbidden
from config import mysql
from flask import jsonify, request
import requests

nodesList = ["192.168.0.124"]
ackList = ["WAIT"]


@app.route('/ack', methods=['GET'])
def acknowledge():
    try:
        message = request.args["status"]
        ackList[0] = str(message) # Returns ACK state


    except Exception as e:
        print(e)
        return "Invalid Request Parameters"

