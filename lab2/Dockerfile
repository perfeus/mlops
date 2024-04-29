# Use the official image as a parent image
FROM jenkins/jenkins:lts
# Switch to the root user
USER root
# Install the necessary packages for python environment
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv
# RUN python3 -m venv /opt/env
# Switch back to the jenkins user
USER jenkins 