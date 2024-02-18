FROM python:3.11.3

ENV PYTHONUNBUFFERED 1

RUN mkdir /algo_ide

WORKDIR /algo_ide

ADD . /algo_ide/

RUN python -m pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
