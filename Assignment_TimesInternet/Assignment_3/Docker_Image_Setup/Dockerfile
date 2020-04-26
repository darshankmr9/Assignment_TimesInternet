FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r dependency.txt
EXPOSE 8001
CMD python ./App.py
