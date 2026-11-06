FROM python:3.14-slim

WORKDIR /opt/app-root/src

COPY requirements.txt /opt/app-root/src/

USER root

RUN python -m pip install --upgrade pip

RUN python -m pip install --no-cache-dir -r requirements.txt

USER 1001

COPY . /opt/app-root/src

ENV FLASK_APP=app
ENV PORT=3000

EXPOSE 3000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3000"]
