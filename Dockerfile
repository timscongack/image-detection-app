FROM python:3.9-slim as python-base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py app/detector.py app/database.py app/yolov3.weights app/yolov3.cfg app/coco.names .
RUN python -c 'from database import init_db; init_db()'

FROM node:14 as node-base

WORKDIR /app

COPY app/express-app/package.json app/express-app/package-lock.json ./
RUN npm install
RUN npm rebuild sqlite3 --build-from-source

COPY app/express-app .
COPY app/images ./images

COPY start.sh .
RUN chmod +x start.sh

EXPOSE 3007

CMD ["sh", "-c", "./start.sh"]