FROM python:3.11-slim

# environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# work directory
WORKDIR /code

# dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /code/