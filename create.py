from application import db
from application.models import Posts, Users

db.drop_all()
db.create_all()
