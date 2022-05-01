FROM python:3.10-buster
WORKDIR /src
COPY ./requirements.txt /src
RUN pip3 install -r requirements.txt
COPY ./convert_csv_to_parquet.py /src
ENTRYPOINT python3 convert_csv_to_parquet.py
