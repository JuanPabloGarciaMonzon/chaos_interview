
![Image and Preview Themes on the toolbar](https://cdn-images-1.medium.com/fit/t/1600/480/0*W_0hjvwqxUuWvosc) 

![Image and Preview Themes on the toolbar](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFYNjfqzX8R4mlKur-K_NLR5BPxKX6gkf7rvbR8mQ4Cv8Fw-M3wgdgbYIL2KCGesyelvM&usqp=CAU)   
# Chaos Mesh Interview
The purpose of this repository is to be presented as an interview for the mentorship program of Chaos Mesh on LFX Mentorship 2021 fall. 


<u>In this project were used some technologies like:</u> 
* Prometheus 
* Grafana
* Docker
* Docker Compose 

<u>In the backend the tools used were:</u>
* A server created on Python Flask.

* A .sh file with a script to make request to the endpoints of the server. 

<u>The main flow of the application is like this:</u>
* First we need to clone, or download the code from the repository
* We travel to the main folder and we run the "docker-compose" file.
    * **sudo docker-compose up**

***<small>This will make run the whole application. (Flask Server, Prometheus, Grafana and Grafana Dashboard).</small>***

* Then we change directory to the "back" folder and run the "test.sh" file, with the command

    * **/bin/bash test.sh**

***<small>This will run a while loop that will call to the 3 main endpoints (/info/host/, /info/uptime and /info/load).</small>***

* Then after preparing the enviroment, we use our favorite browser and type the next URLs, and, depending on our host, will be displayed different information:
* [http://localhost:23333/info/host](http://localhost:23333/info/host) (endpoint)

* [http://localhost:23333/info/uptime](http://localhost:23333/info/uptime) (endpoint)

* [http://localhost:23333/info/load](http://localhost:23333/info/load) (endpoint)
* [http://localhost:23333/metrics](http://localhost:23333/metrics) (endpoint)
* [http://localhost:3000](http://localhost:3000 (Grafana)) (Grafana)

In Grafana we will have created alredy, thanks to the grafana-dashboard service deployed in docker-compose, the panels and the connection to the Prometheus Data Source, we only have to travel to the Dashboards manage page and we will watch the behavior of the request of the two endpoints that can be measured, "Uptime" and "Load Avg".


This is in a nutshell the flow of the application, i hope I can keep working with I have learn a lot, thanks for this opportunity. 

***<small>The whole project was created using WSL2 and a Ubuntu 20.0.4 Distro..</small>***

<<<<<<< HEAD
# Video Explaining the main flow of the application
* [https://youtu.be/k7_QgtLAE6s](http://localhost:3000 (Grafana)) (Grafana)

Juan Pablo García Monzón (@JuanPabloGarc48)
=======
Juan Pablo García Monzón (@JuanPabloGarc48)
>>>>>>> 97b5fbc5c48ac7fd8e445a68041ed909aca56111
