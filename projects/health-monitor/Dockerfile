# specify base image:
FROM python:3.13-slim

# set work directory to:
WORKDIR /home/app

# copy contents from local dir ./app to container's dir /home/app.
COPY ./app /home/app

# update container's system package manager
# install with python's package manager (pip) libraries needed for app.
RUN apt-get update && pip install flask psutil prometheus-client

# open container port:
EXPOSE 5000

# run command 'python3 app.py' to start server
CMD ["python3", "app.py"]