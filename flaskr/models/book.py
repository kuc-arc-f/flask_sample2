# 日本語

# coding: utf-8
#
from flaskr import db

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    body  = db.Column(db.String(255) )

#    def __repr__(self):
#        return '<Entry id={id} title={title!r}>'.format(
#                id=self.id, title=self.title)

def init():
    db.create_all()
