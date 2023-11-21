FROM postgres:14.4-alpine

COPY init.sql /docker-entrypoint-initdb.d/
RUN chmod +r /docker-entrypoint-initdb.d/init.sql

COPY populate.sql /docker-entrypoint-initdb.d/
RUN chmod +r /docker-entrypoint-initdb.d/populate.sql

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["postgres"]
