FROM python:3.5-alpine

MAINTAINER Mohammed Bilal, <mohammedbilal1995@gmail.com>


EXPOSE 8080

# App configuration
WORKDIR /app
RUN mkdir -p /app
COPY requirements.txt /app

RUN pip install --upgrade pip && \
	pip install -U -r requirements.txt

COPY app.py /app

ENTRYPOINT ["python"]
CMD ["app.py", "--log-file", "-"]
