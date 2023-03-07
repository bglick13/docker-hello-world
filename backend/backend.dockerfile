FROM python:3.9

RUN mkdir /app
WORKDIR /app

RUN apt update
RUN pip install --upgrade pip

COPY ./backend /app/
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app
CMD [ "python", "-u", "main.py" ]