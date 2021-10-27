FROM python

COPY . .
RUN pip install .
ENTRYPOINT [ "htm-bot" ]
