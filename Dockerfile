FROM python:3.8

WORKDIR /01_study

COPY ./requirements.txt /01_study/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /01_study/requirements.txt

COPY ./app /01_study/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]