# AutoML
ML-OPS
A complete description all the steps followed while deploying the model will be explained in the section. 
Firstly, we will create a model.py file in any IDE (Integrated Development Environment) and after running the file, it will generate a pickle file named as linear_regresssion.pkl. 
Next, we must create a file named app.py which will contain the code for our flask app. We must upload our dataset height_weight.csv. 
The next part is the creation of Dockerfile, within this file we will input all the commands we need to run on the command line to assemble an image. 
The next file we must create is the yaml file for Kubernetes deployment, Kubernetes services and the Cloud build. yaml is a language file used to create configuration for programming languages. 
The next step is creating a github repository and uploading the files we have created into the repo. After organizing the files on github, we must connect our github repo with our cloud build and the Google cloud platform.
We also must create a requirements.txt file with the libraries and requirements.
Kubernetes is an open-source system, and we will be using it to automate the deployment of our application. 
After finishing the creation of files, we will be ready to deploy our application. 
Now, as the next step we must create a Kubernetes cluster named kube (any other name according to your preference) with the help of command line interface and we set the number of nodes to 1. 
We must mention this name in google cloud yaml file. 
Lastly, we must create a trigger that will act when we make a change to our source code and push that to the github repository. 
This will trigger the cloudbuild trigger and the model will be deployed. 
We can check the logs to confirm the docker image being built and the pushed to the google container registry. 
If the build fails, the logs will mention the error. Once the build is successfully completed, we can see the pods being deployed.
Finally, an endpoint will be created and using the end point we will test our application. We will be passing the values through URL concatenation.
___________________________________________________________________________________________________________________________________________________________________
