# Use the official image as a parent image
FROM jenkins/jenkins:lts
# Specify the autor of the image
LABEL autor="Alex Izmalkin"
# Switch to the root user
USER root
# Install the necessary packages for python environment
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv
# Switch back to the jenkins user
USER jenkins 
# Copy the requirements file to the image
COPY requirements.txt $JENKINS_HOME/requirements.txt
# Create a virtual environment 
RUN python3 -m venv $JENKINS_HOME/venv
# Add the virtual environment to the PATH
ENV PATH="${JENKINS_HOME}/venv/bin:${PATH}"
# Install the required packages
RUN pip install -r $JENKINS_HOME/requirements.txt
