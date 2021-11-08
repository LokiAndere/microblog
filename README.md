# microblog
 python flask tutorial

# dependences
pip install flask
export FLASK_APP=microblog.py
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate

## db migration
flask db init
flask db migrate -m "users table"
flask db upgrade

## db manipulation
flask shell

### shell example 1
```
users = User.query.all()
for u in users:
    print(u.id, u.username)
```

>>> u = User.query.get(1)
>>> posts = u.posts.all()

>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)

>>> User.query.order_by(User.username.desc()).all()

>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> posts = Post.query.all()
>>> for p in posts:
...     db.session.delete(p)
...
>>> db.session.commit()

## continue installation
pip install flask-login

### shell example 2
>>> u = User(username='susan', email='susan@example.com')
>>> u.set_password('cat')
>>> db.session.add(u)
>>> db.session.commit()

## continue installation
pip install email-validator
