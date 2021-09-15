'''
@Author: Ayur Ninawe
@Date: 09-09-2021
@Last Modified by: Ayur Ninawe
@Last Modified time: 09-09-2021
@Title : Program to get data from api and sendinf it to topic using kafka producer.
'''

from time import sleep
from kafka import KafkaProducer
from alpha_vantage.timeseries import TimeSeries
import random
import json
import sys
from decouple import config
from loggerfile import logger


def dataGrabber():
    try:
        ticker = 'GOOGL'
        keys = "4394I92D63PSMEVS"
        time = TimeSeries(key=keys, output_format='json')
        data, metadata = time.get_intraday(symbol=ticker, interval='1min', outputsize='full')
        return data
    except Exception as e:
        logger.info(e)
        sys.exit(1)


def messagePublisher(producerKey, key, data_key):
    keyBytes = bytes(key, encoding='utf-8')
    producerKey.send("stockml", json.dumps(data[key]).encode('utf-8'), keyBytes)
    print("Message Published!")


def kafkaProducerConnect():
    try:
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        return producer
    except Exception as e:
        logger.info(e)


if __name__ == "__main__":
    data = dataGrabber()
    if len(data) > 0:
        kafkaProducer = kafkaProducerConnect()
        for key in sorted(data):
            messagePublisher(kafkaProducer, key, data[key])
            sleep(3)