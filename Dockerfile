FROM python:3
ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/

RUN apt-get update && apt-get -y install postgresql
RUN pip install pipenv
RUN pipenv install --system

# Expose is NOT supported by Heroku
# EXPOSE 8000

# Run the image as a non-root user
RUN useradd -m myuser
USER myuser

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku			
CMD gunicorn --bind 0.0.0.0:$PORT CouncilTag.wsgi --log-file -