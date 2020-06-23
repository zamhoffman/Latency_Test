from flask import Flask
from flask import request
import time

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():

    if not request.get_data:
        return "error", 400
    print("here is the image!!!!!!!!!!!", request.get_data)
    task = {
        'received timestamp' : time.time()
    }
    return task, 201
