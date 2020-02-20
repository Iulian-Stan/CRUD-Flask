from init import app

if __name__ == '__main__':
	app.add_api('openapi.yaml')
	app.run(port=9090, debug=True)