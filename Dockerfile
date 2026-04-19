FROM python:3.13.2-alpine3.21

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m manage collectstatic

CMD chmod +x ./start.sh ; ./start.sh
