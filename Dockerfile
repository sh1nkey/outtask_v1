FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install --upgrade setuptools wheel
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
