Using uWSGI server

* `$ docker build -t identidock .`
* `$ docker run -d -p 9090:9090 -p 9191:9191 identidock`
* `$ curl localhost:9090`

Replacing with this command `docker run -d -P --name port-test identidock`, Docker automatically map a random high- numbered port on the host to each “exposed” port on the container.

To view the ports exposed from the container, run `docker port port-test`

__Downside__ with this approach is that we’ve lost access to the development tools such as debugging output and live code-reloading provided by the default Python web server.