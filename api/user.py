from model.user import User, UserSchema

user_schema = UserSchema()

def get_users() -> list:
    users = User.get_all()
    data = user_schema.dump(users, many=True)
    return data

def post_user(user):
    new_user = User(user)
    new_user.save()

    return '', 201

def get_user(id):
    user = User.get_one(id)
    if user is not None:
        return user_schema.dump(user)
    else:
        return '', 404

def delete_user(id):
    user = User.get_one(id)
    if user is not None:
        user.delete()
        return '', 204
    else:
        return '', 404

def put_user(id, user):
    old_user = User.get_one(id)
    print(user)
    if old_user is not None:
        old_user.first_name = user['first_name']
        old_user.last_name = user['last_name']
        old_user.save()
    else:
        new_user = User(user)
        new_user.save()
    return '', (200 if old_user is not None else 201)