from init import db, ma
from model.base_model import BaseModel

class User(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User 