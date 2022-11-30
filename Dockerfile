FROM python:latest
RUN apt-get -y update

# WORKDIR /usr/app/src

COPY requirements.txt requirements.txt
COPY sample.mp3 .
RUN pip install -r requirements.txt
RUN apt-get install ffmpeg -y

COPY file.py .

CMD [ "python", "file.py" ]