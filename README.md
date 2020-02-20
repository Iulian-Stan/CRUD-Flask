# Flask
Simple CRUD application implemented using Flask framework
Additional dependencies
* [connexion](https://github.com/zalando/connexion) - OpenAPI documentation generation
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com)- ORM (DB interaction)
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io) - Data serialization/deserialization

## Installation
Create a python virtual environment (optional)
```bash
python -m venv .env
.env\Scripts\activate
```
Install of the dependencies from *requirements.txt*
```bash
pip install -r requirements.txt
```

## Usage
Start the application by running *main.py*
```bash
python main.py
```
Navigate to the following URL in your web browser - [http://127.0.0.1:9090/v1.0/ui/](http://127.0.0.1:9090/v1.0/ui/). It will open the OpenAPI generate API documentation based on *openapi.yaml*. The application will create an initially empty DB (see *init.py*). Use the POST or PUT methods to populate the DB with some sample data in order to be able to test other HTTP methods.