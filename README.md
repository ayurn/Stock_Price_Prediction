# Stock Price Prediction Project

This project focuses on predicting Google stock price on real time data. I used past 10 years worth of historical Google (GOOGL) stock data for training and built an effective model for predicting stock prices and displayed the predictions on webpage using Flask, Kafka and Highcharts.

![GitHub issues](https://img.shields.io/github/issues/ayurn/Stock_Price_Prediction?color=FF3D37&label=Issues&style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/ayurn/Stock_Price_Prediction?color=5DFF00&label=Last%20Commit&style=plastic)

![Python 3.6](https://img.shields.io/badge/python-3.6.9-orange) ![pip-3](https://img.shields.io/badge/pip-20.0.2-green) ![Python-Kafka 2.0.2](https://img.shields.io/badge/kafka--python-2.0.2-red) ![Pyspark 3.1.2](https://img.shields.io/badge/pyspark-3.1.2-yellowgreen) ![s3fs 0.4.2](https://img.shields.io/badge/s3fs-0.4.2-blue) ![pandas 1.3.3](https://img.shields.io/badge/pandas-1.3.3-green)
![alpha-vantage 2.3.1](https://img.shields.io/badge/alpha--vantage-2.3.1-critical) ![boto3 1.18.42](https://img.shields.io/badge/boto3-1.18.42-ff69b4) ![Flask 2.0.1](https://img.shields.io/badge/Flask-2.0.1-009e73)

![GIF](readme_resources/readme_resources_stock_prediction_chart.gif)

#

## Prerequisites:

- Python3
```
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
```

#

## What the project does and how it was made?
- This project has been built using Python3 to help predict the future stock close prices of Google stock with the help of Machine Learning and Data Visualization in real time.
- To start, I created an AWS account and created a user with all access.
- Downloaded the Amazon CLI on my system and then added the AWS access keys to be accessed globally.
- Next I started creating python script to create a bucket and upload the downloaded CSV file onto the AWS bucket. To do this, I needed to install the boto3.

#### ***What is boto3?***
***Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.***

#### ***What is Amazon S3 Bucket?***
***An Amazon S3 bucket is a public cloud storage resource available in Amazon Web Services' (AWS) Simple Storage Service (S3), an object storage offering. Amazon S3 buckets, which are similar to file folders, store objects, which consist of data and its descriptive metadata.***

- After creating and uploading my CSV file, I fetched the file from my S3 bucket with the help of Pandas.
- Since no data is clean and has missing values, it needs to be cleaned.
- Now after the data has been cleaned, we can now built a model using Machine Learning. Keep in mind, the less data we use the higher chances of underfitting occur and the more data we use, the higher chances of overfitting occur. So we need to choose the data not more, not less.
- The model building process has been done using PySpark’s mlib Library.

#### ***What is PySpark?***
***Apache Spark is written in Scala programming language. To support Python with Spark, Apache Spark community released a tool, PySpark. Using PySpark, you can work with RDDs in Python programming language also. It is because of a library called Py4j that they are able to achieve this.***

- I used Linear Regression to train the model and used the Regression Evaluator to give the accuracy of my model.
- After the successfull buliding of my model, I needed to check if it works on real data. For that I registered on a website called AlphaVantage and generated the key to access the live data from their site.

#### ***What is AlphaVantage?***
***Alpha Vantage Inc. is a company that provides realtime and historical stock APIs as well as forex (FX) and digital/crypto currency data feeds.***

- Now comes the fun part of testing the model using Data Visualization.
- For this, firstly I had to install Apache Zookeeper and Apache Kafka.

#### ***What is Apache Zookeeper?***
***ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them, which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.***

#### ***What is Apache Kafka?***
***Apache Kafka is a distributed publish-subscribe messaging system and a robust queue that can handle a high volume of data and enables you to pass messages from one end-point to another. Kafka is suitable for both offline and online message consumption. Kafka messages are persisted on the disk and replicated within the cluster to prevent data loss. Kafka is built on top of the ZooKeeper synchronization service. It integrates very well with Apache Storm and Spark for real-time streaming data analysis.***

- To display the prediction in real time, we first need to start the Zookeeper server and then start the Kafka server.
- I created the Producer and Consumer scripts in Python3 and ran them through Flask app.

#### ***What is Flask?***
***Flask is a web application framework written in Python. Flask is based on the Werkzeug WSGI
toolkit and Jinja2 template engine. The Flask framework uses Werkzeug as one of its bases. Werkzeug is a WSGI toolkit, which implements requests, response objects, and other utility functions. This enables building a web framework on top of it. Web Server Gateway Interface (WSGI ) is a specification for a universal interface between the web server and the web applications. It has been adopted as a standard for Python web application development. Jinja2 is a popular templating engine for Python. A web templating system combines a template with a certain data source to render dynamic web pages.***

- Finally, to display the graph I used Highcharts JS in my HTML file and styled it through CSS.

#

Using ALPHA VANTAGE API to predict google stock price.

- Using [ALPHA VANTAGE](https://www.alphavantage.co/) to genrate API Key.

- Using this API key to Download Google Stock Price data for each 1 min interval.

- [Create S3 bucket](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-creating-buckets.html) using boto3. (Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage AWS services, such as EC2 and S3. Boto provides an easy to use, object-oriented API, as well as low-level access to AWS services.)

- After creating [bucket upload](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html) **stock data** into bucket using boto3.

-  Reading data from S3 and doing some preprocessing.

- After preprocessing train a Linear Regression model and save model weights.

- Installing [kafka and zookeeper](https://tecadmin.net/install-apache-kafka-ubuntu/) into system and install [python-kafka](https://pypi.org/project/kafka-python/)

- Start zookeeper and kafka server into local system and connect python-kafka to local host.
    ```
    $cd $KAFKA_HOME
    
    $./bin/zookeeper-server-start.sh config/zookeeper.properties
    $./bin/kafka-server-start.sh config/server.properties

    ```

- **Create a Topic in Kafka**

    Create a topic in kafka using below query. Before create kafka topic you go to kafka folder.
    ```
    $cd $KAFKA_HOME

    $./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic stockml
    ```
    
    The replication-factor describes how many copies of data will be created. As we are running with a single instance keep this value 1.

    Set the partitions options as the number of brokers you want your data to be split between. As we are running with a single broker keep this value 1.

    You can create multiple topics by running the same command as above. After that, you can see the created topics on Kafka by the running below command:

    ```
    bin/kafka-topics.sh --list --zookeeper localhost:2181
    ```

- **Send Messages to Kafka**

    The **producer** is the process responsible for put data into our Kafka. The Kafka comes with a command-line client that will take input from a file or from standard input and send it out as messages to the Kafka cluster. The default Kafka sends each line as a separate message.

    ```
    bin/kafka-console-producer.sh --broker-list localhost:9092 --topic stockml
    ```

- **Using Kafka Consumer**

    Kafka also has a command-line consumer to read data from the Kafka cluster and display messages to standard output.

    The first argument is the topic, numtest in our case.
    
    bootstrap_servers=[‘localhost:9092’]: same as our producer

    ```
    bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic stockml --from-beginning
    ```
- **Now using python KafkaProducer to connect the local kafka host**

    bootstrap_servers=[‘localhost:9092’]: sets the host and port the producer should contact to bootstrap initial cluster metadata. It is not necessary to set this here, since the default is localhost:9092.

- **Using KafkaConsumer to predict stocks data**

    Using **KafkaConsumer** to get data from producer. After geting data we load save model which save previously when train the model. Using these model we predict close value.

- **Create Flask API**

    In flask I have created 2 URL:

    1. "/" for main page which rander stockgraph.html template for showing predicting close and actual close value.
    2. "/data" this is for send data to index.html page for showing graph.

## How To Run

- First start zookeeper and kafka server.
- Run producer file. (``` python3 producer.py ```)
- Run app file. (``` python3 app.py ```)
