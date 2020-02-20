from init import db
from model.user import User

db.create_all()
db.session.commit()