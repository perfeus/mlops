# Use the official image as a parent image
FROM jenkins/jenkins:lts
# Switch to the root user
USER root
# Install the necessary packages for python environment
RUN apt-get update && apt-get install -y python3 python3-pip
# Switch back to the jenkins user
USER jenkins