FROM alpine:latest

RUN apk add --no-cache bash postgresql-client

WORKDIR /scripts
COPY backup.sh .

RUN chmod +x backup.sh

CMD ["./backup.sh"]