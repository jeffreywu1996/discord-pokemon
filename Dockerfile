FROM python:3.9.14-alpine3.16

WORKDIR /pokemon

COPY requirements.txt .
RUN pip3 install --no-deps google-cloud-firestore
RUN pip3 install -r requirements.txt
RUN pip3 install firebase_admin -U

COPY . .

CMD python3 poke_bot.py
