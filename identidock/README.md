
* `$ docker build -t identidock .`
* `$ docker run -d -p 5000:5000 identidock`
* `$ curl localhost:5000`

__Downside__ of this approach is that every little change to the code means we need to rebuild the image and restart the container.

To avoid the above downside, we can _bind mount_ the source code folder on the host inside the container. This overwrites the `/app` folder inside the container and makes the volume writeable from inside.

`docker run -d -p 5000:5000 -v "$(pwd)"/app:/app identidock`

__Downside__ of this approach are that 

* all our dependencies —the Python compiler and libraries— are encapsulated inside a Docker container.
* it is running the default Flask webserver, which is only intended for development and too inefficient and insecure for production use.

