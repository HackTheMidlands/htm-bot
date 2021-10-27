FROM python

RUN pip install -U pip
COPY . .
RUN pip install .
ENTRYPOINT [ "htm-bot" ]
