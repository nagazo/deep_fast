FROM python:3.11

WORKDIR /code

COPY src/deep_fast/main_esther.py /code/
COPY run.sh /code/run.sh

RUN apt update
RUN apt install -y vim

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade git+https://github.com/nagazo/deep_fast.git@kwj/241004

CMD ["sh", "run.sh"]
