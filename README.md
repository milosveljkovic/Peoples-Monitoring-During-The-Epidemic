# Runner-Monitoring

## Getting Started

1. Clone repo
2. Open project 
3. In project root open console and type in 'pip install' (this will add all dependencies to app.)
4. Then change path from root to /clientApp/web and type in 'npm install'
5. In folder db you will find to files called 'iot_path.sql and iot_runner.sql' , you should import it in your DB. I'm using a
MySql in this project.
6. Change a constants from app.py : 'DB_LOCALHOST','DB_NAME','DB_PASSWORD'.. 
7. In project you will notice directory 'services', there you can find microservices (python apps)
8. Every microservice should start(run) on different PORT
9. Start each microservice: in terminal be sure you are in services/service1 path, type in $ python app.py (for every service)
8. Start client: in terminal be sure you are in clientApp/web, type in $ npm start

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

