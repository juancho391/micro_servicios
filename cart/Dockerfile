FROM python:3.12

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requeriments.txt
EXPOSE 8080 
CMD ["python", "manage.py","runserver","0.0.0.0:8080"]
