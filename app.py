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
        message = request.args["message"]        
        url = "https://discord.com/api/webhooks/890522840821006366/Ol38KeLTe2aXel4y2ECnDLuiDdilNYiEjrhMYHTKp8FsGyVPn6CFHD5HwM-7nCR8ww0B"
        payload = json.dumps({
        "content": message
        })
        headers = {
        'Content-Type': 'application/json',
        'Cookie': '__cfruid=b882f9b808096b92c166f27597787a81fff7a4cf-1632389271; __dcfduid=88e1af7c1c5011ecbc9842010a0a066c; __sdcfduid=88e1af7c1c5011ecbc9842010a0a066c8b54e6b16757ef5e34f069e7077c55d22b13cb99c9f9a5a17bafc3d214f0e507'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        return "success"
    except Exception as e:
        print(e)

# Setting Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)