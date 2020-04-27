# Runner-Monitoring

## Getting Started

1. Clone repo
2. Open project 
3. In project root open console and type in 'pip install' (this will add all dependencies to app.)
4. Then change path from root to /clientApp/web and type in 'npm install'
5. In folder db you will find to files called 'iot_path.sql and iot_runner.sql' , you should import it in your DB. I'm using a
MySql in this project.
6. Change a constants from app.py : 'DB_LOCALHOST','DB_NAME','DB_PASSWORD'.
7. In project you will notice directory 'services', there you can find microservices (python apps)
8. Every microservice should start(run) on different PORT
9. Start each microservice: in terminal be sure you are in services/service1 path, type in $ python app.py (for every service)
8. Start client: in terminal be sure you are in clientApp/web, type in $ npm start

## Getting started Docker

1. download docker
2. build image using command:
```$ sudo docker build -t name_of_image:latest . ```
(when you run this you should be in directory where Dockerfile is-> services/path_service for example)
3. If 'build' went successfuly you shoul see message : Succes build something..
4. In this point you have your image but it is not running (check this by typing next command: $sudo docker images)
5. run your image -> $sudo docker run -it -d -p port:port [name] (name should be same like in build name_of_image)
example:
```
$sudo docker run --net=host -it -d -p 5001:5001 flask_path 
$sudo docker run --net=host -it -d -p 5000:5000 flask_runner
$sudo docker run --net=host -it -d -p 5002:5002 flask_socket
$sudo docker run -it -d -p 3000:3000 web 
```
Notes:

*You should build every microservice, so you will have 4 images on the end (check this by typing $sudo docker images )

*Docketfile is different for python(flask) and node(react).  

*You should have mysql on you system 

*flag --net=host is important beacuse we work with local DB!

## Project description

This is a demo flask project based on IOT. We demonstrated in 'Runner-Monitoring' some of flask basic functionality, how to use it 
and how to implement it in creative way. Project is some kind of monitoring dashboard where you can follow your activity during a exercise.
You have a runners-form on first 'page', fill it, submit it and then you should connect to 'live-data-stream' and then just active
Start Running button! In that moment you cant follow your activity on charts below the form. There are two kind of charts. One for your
x,y coordinates( your locations) and the second is for your current distance in KM.  Whene you reach youd goal, you'll see a 'Congratulations message'
and that mean you win a race! On second 'page-runners' you'll see a runner statistic like 'Average-speed' , 'Average-heart_rate' and much more.

### Project architecure
![Runner Form](https://i.postimg.cc/SxB7X6Qj/Untitled-Diagram.png)

### Runner Form
![Runner Form](https://i.postimg.cc/J4sSDktc/dashboard.png)

### Chart (runners activity)
![Chart](https://i.postimg.cc/sD1CYLHW/charts.png)

### Chart (runners activity , after few coordinates)
![Chart](https://i.postimg.cc/NGDQ7mg3/chart2.png)

### Runner details
![Details](https://i.postimg.cc/Kcqd8Nc8/path.png)

