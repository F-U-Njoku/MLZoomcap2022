FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app
COPY ["homework/", "./"]

RUN pipenv install --system --deploy

EXPOSE 9600

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9600", "predict:app"]