FROM docker.io/python:3.8-buster
LABEL maintainer="Logan Endes <>lge9081@g.rit.edu>"

WORKDIR /app
ADD ./ /app
COPY ./requirements.txt requirements.txt
RUN apt-get -yq update && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app/

EXPOSE 8080
 
CMD [ "python3", "tracker.py"]

