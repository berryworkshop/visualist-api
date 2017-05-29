FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-upload
MAINTAINER Allan Berry "allan.berry@gmail.com"
WORKDIR /app
VOLUME /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 5000
