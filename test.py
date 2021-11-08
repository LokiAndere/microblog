from microblog import app
print(app.config['SECRET_KEY'])

from hashlib import md5
email = 'dyudok@gmail.com'
bemail = email.lower().encode('utf-8')
print(bemail)
mdemail = md5(bemail)
print(mdemail)
digest = mdemail.hexdigest()
print(digest)