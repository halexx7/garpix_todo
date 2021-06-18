from flask import Flask, request, render_template, redirect
from peewee import Model, SqliteDatabase, TextField, BooleanField, DateTimeField
from datetime import datetime
from datetime import datetime
import os

app = Flask(__name__)

db = SqliteDatabase('todo.db')

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = db


class Note(BaseModel):
    text = TextField()
    done = BooleanField()

    dateAdded = DateTimeField(default=datetime.now)

db.connect()
db.create_tables([Note,])


def create_note(text):
    note = Note(text=text, done=False)
    note.save()


def read_notes():
    return Note.select()


def update_note(note_id, text, done):
	note = Note.select().where(Note.id == note_id).get()
	note.text = text
	note.done = True if done == "on" else False
	note.save()
	

def delete_note(note_id):
    Note.get(Note.id == note_id).delete_instance()


@app.route("/", methods=["POST", "GET"])
def view_index():
    if request.method == "POST":
        create_note(request.form['text'])
    return render_template("index.html", notes=read_notes())


@app.route("/edit/<note_id>", methods=["POST", "GET"])
def edit_note(note_id):
    if request.method == "POST":
        update_note(note_id, text=request.form['text'], done=request.form['done'])
    elif request.method == "GET":
        delete_note(note_id)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)