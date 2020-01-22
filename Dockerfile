FROM python:3.7.3-stretch

RUN apt-get update 
RUN apt-get install -y libpython3-dev build-essential libpcre3 libpcre3-dev 

ADD bot/ /bot/bot/
ADD run.sh  /bot/
ADD requirements.txt /bot/requirements.txt

RUN pip3 install -r /bot/requirements.txt

CMD ["python3" "/bot/run.sh"]