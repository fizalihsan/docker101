FROM python:3.4

# Creates the uwsgi user and group
# users and groups created inside containers do not propogate to the host.
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi 

RUN pip install Flask==0.10.1 uWSGI==2.0.8 
WORKDIR /app
COPY app /app

# exposes these ports to the host and other containers
EXPOSE 9090 9191 

# sets the user for all the following lines
USER uwsgi
CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", "--callable", "app", "--stats", "0.0.0.0:9191"]