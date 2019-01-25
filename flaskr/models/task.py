# 日本語

# coding: utf-8
#
from flaskr import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.String(255) )

#    def __repr__(self):
#        return '<Entry id={id} title={title!r}>'.format(
#                id=self.id, title=self.title)

def init():
    db.create_all()
