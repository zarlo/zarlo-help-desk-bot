FROM python:3.7.3-stretch

RUN apt-get update 
RUN apt-get install -y libpython3-dev build-essential libpcre3 libpcre3-dev 

ADD app/ /app/app/
ADD run.sh  /app/
ADD requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

CMD ["python3" "/app/run.sh"]