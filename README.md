# Calculator-app
A simple calculator app with built using Python pyramid framework.

## Overview

This application has a small MicroService which does simple calculation from input and shows the output. This is a simple HTTP web service built on a standard Python Pyramid framework with a single endpoint which displays results of our calculation. 

## Getting Setting

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

 - Please note that ths is not a production applicaiton. 

## Pre-requisites

Before you begin with setup, ensure the following is installed to your system:

* [Python 3.7 or greater]
* [Python Pip, the package manager]
* [Docker]
* [Git and a GitHub account]
* [Swagger for API documentaion] 
* [Built and tested on Macbook and Windows]

## Steps to install and run app in a development environment

- Run the below command on your terminal to clone the github repositoty on your local machine:

```
git clone https://github.com/ShardaND/zaaksysteem.git
```
- Start your Docker instance 

- Move (cd) to the project directory "zaaksystem" in terminal

```
cd zaaksysteem
```
- Execute command docker-compose build

```
docker-compose build
```

- Now execute command docker-compose up

```
docker-compose up
```

Your application is now running.

- To view your app running, visit this link : http://localhost:6543/calculator 

To make an API request and test your applicaiton. Please follow the below steps: 

## On Chrome Browser

- On the browser, copy and paste the below url to see the results being displayed on the screen :
    - http://localhost:6543/calculator/add?operand1=3&operand2=5

Try to test more options by changeing the "operand1" and "operand2" values. 

## On Swagger 
 
- To view the Swager API documentation: , please visit this link 
 on Chrome Browser http://localhost:8000/#/

- Now add a CORS extension on your chrome broswer to run the swagger (in http) using the below link: 
    - https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en 
- Start CORS ( from the above chrome extension) before you run the swagger
- Visit this link (http://localhost:8000/#/) and change the Swagger scheme from default "https" to "http" 

![image](https://user-images.githubusercontent.com/32950886/82655505-915f8980-9c22-11ea-8f57-6705c3a9ac53.png)

- Next try to click on the Swagger API /calculator/add
- click on try out button on the right and add 2 numbers in the form field below ( operand 1 and operand 2).

Sample working API application is below:

![image](https://user-images.githubusercontent.com/32950886/82655845-19459380-9c23-11ea-830c-a581ae317996.png)


## Using Postwoman 

Postwoman is an free open source, fast and beautiful API request builder:

- https://postwoman.io/

## Author

* **Sharda Deshmukh** - *Initial work* - [Sharda Deshmukh](https://github.com/ShardaND)


## Acknowledgement

* Inspirations from 
    - https://github.com/ShardaND/pyramid_swagger
    - https://github.com/ShardaND/todopyramid

## Contribution Guidelines
 
 In order to contribute to this repository, please follow the below steps : 
 - Look for the to-do list below 
 - Fork the repository
 - Make changes to the forked repository
 - Send a pull request with your suggested changes and its benefits

## To-do

- Implement the app in a DDD way 
- Develop the API to work on https (add CORS in the back-end)
- Add tests
- Add more operations; like substract, divide, etc. 
- add a front end layer  









