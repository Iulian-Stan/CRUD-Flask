from init import db

class BaseModel(db.Model):
    __abstract__ = True


    def __init__(self, data):
        """
        Class constructor
        """
        for key, item in data.items():
            if hasattr(self, key):
                setattr(self, key, item)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        self.__init__(data)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_one(cls, id):
        return cls.query.get(id)