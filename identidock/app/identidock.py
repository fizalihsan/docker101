from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello_world():
	return 'Hello World!!!\n' 

if __name__ == '__main__':
	app.run(
		debug=True, 
		# binds to all network interfaces to allow the container to be accessed from the host or other containers.
		host='0.0.0.0'
		)
