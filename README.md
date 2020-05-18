# Web app with Streamlit + Tensorflow
This repo shows a minimal example to build your web app with Streamlit + Tensorflow. It has been designed following the microservices architecture. Two services are available:
* The front end of the app is build with [Streamlit](https://www.streamlit.io)
* The back end deploys a pretrained Tensorflow model as servable thanks to [Tensorflow Serving](https://www.tensorflow.org/tfx/guide/serving).

![Web app image](/img/wombat.png)

Once the app is running you can pass the link of an image from the web. Tap on the *Classify* button and immediately it tells you the class of the image :dizzy:

## Instructions to run the web app

It is assumed you have [Docker](https://www.docker.com) installed. Then:
1. Clone this repository with 
`git clone https://github.com/mlgxmez/streamlit_tf_app.git`
2. Go to the root folder of the repo and type in your terminal
`docker-compose up -d`
3. Open the web browser and visit 
`localhost:8503`

The web app is now running in your computer. It's up to you how you want to extend the project. I would encourage you to read the Dockerfiles and the script running the app to see how all the files work together :gear:

4. To shut down your containers at once type
`docker-compose down`
