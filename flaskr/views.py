# 日本語

# coding: utf-8
#
from flask import request, redirect, url_for, render_template, flash
from flaskr import app, db
from flaskr.models.entry import Entry
from flaskr.models.task import Task
from flaskr.models.book import Book
#
@app.route('/')
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

#
@app.route('/add', methods=['POST'])
def add_entry():
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
#
@app.route('/tasks', methods=['GET'])
def tasks():
    tasks = Task.query.order_by(Task.id.desc()).all()
    for task in tasks:
        print(task.title )
    return ""
#
@app.route('/books', methods=['GET'])
def books():
    books = Book.query.order_by( Book.id.desc()).all()
    for book in books:
        print(  book.title, book.body )
    return ""    




