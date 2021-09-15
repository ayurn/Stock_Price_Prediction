'''
@Author: Ayur Ninawe
@Date: 10-09-2021
@Last Modified by: Ayur Ninawe
@Last Modified time: 11-09-2021
@Title : Program to plot the live predicted values using flask app.
'''

from flask import Flask, render_template, make_response
from datetime import datetime
import time
import json
import Consumer
import sys
from loggerfile import logger

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    try:
        pred_price, actual_price, date_time = Consumer.StockPricePrediction(Consumer.LoadModel)
        date_time = int(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S').strftime('%s')) * 1000
        data = [date_time, pred_price, actual_price]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
        time.sleep(2)
        return response
    except Exception as e:
        logger.info(e)
        sys.exit(1)


if __name__ == ("__main__"):
    #for deploying app locally
    #app.run(host='127.0.0.1', port=5000)
    
    #for deploying on EC2 instance
    app.run(host='0.0.0.0', port=8080)