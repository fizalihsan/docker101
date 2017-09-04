FROM debian:wheezy
MAINTAINER Fizal
RUN apt-get update && apt-get install -y cowsay fortune

# The COPY instruction simply copies a file from the host into the image’s filesystem to destination path
COPY entrypoint.sh /

# ENTRYPOINT ["/usr/games/cowsay"]
# ENTRYPOINT scripts will swallow any commands given to `docker run`.
ENTRYPOINT ["/entrypoint.sh"]