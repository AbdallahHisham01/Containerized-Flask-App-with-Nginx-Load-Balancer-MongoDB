FROM python

WORKDIR /app

COPY . .

RUN mkdir /mnt_mongodb
RUN mkdir /mnt_nfs


ENTRYPOINT ["python", "collector.py"]
