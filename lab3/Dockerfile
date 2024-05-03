FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv
WORKDIR /app
COPY . .
ENV PATH=/app/venv/bin/:${PATH}
RUN pip3 install -r /app/requirements.txt
CMD ["/app/venv/bin/python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
