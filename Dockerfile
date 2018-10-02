FROM python:3.6

WORKDIR /home

COPY . .

RUN pip install -e .

WORKDIR /home/aiohttp

CMD [ "python","App.py" ]
