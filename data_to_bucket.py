'''
@Author: Ayur Ninawe
@Date: 08-09-2021
@Last Modified by: Ayur Ninawe
@Last Modified time: 08-09-2021
@Title : Program to add files to AWS S3.
'''

import boto3
from loggerfile import logger

s3 = boto3.resource(service_name = 's3')
def show_buckets():
    try:
        for bucket in s3.buckets.all():
            print(bucket.name)
    except Exception as e:
        logger.info(e)

def put_data():    
    try:
        s3.Bucket('ayurnaws').upload_file(Filename = 'google_stock_data.csv', Key = 'google_stock_data.csv')
    except Exception as e:
        logger.info(e)

if __name__ == '__main__':
    show_buckets()
    put_data()