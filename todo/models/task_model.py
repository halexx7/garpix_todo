from datetime import datetime

from flask import abort
from peewee import CharField, DateTimeField, Model, SqliteDatabase, TextField

db = SqliteDatabase("todo.sqlite")


class BaseModel(Model):
    class Meta:
        database = db


class Task(BaseModel):
    title = CharField(max_length=150)
    content = TextField()
    create_at = DateTimeField(default=datetime.now)

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.content}, {self.create_at}"

    def get_all_task(self):
        tasks = Task.select()
        tasks_json = []
        for task in tasks:
            tasks_json.append(
                {"id": task.id, "title": task.title, "content": task.content, "create_at": task.create_at}
            )
        return tasks_json

    def get_task(self, id):
        task = Task.select().where(Task.id == id).get()
        if task:
            return task
        abort(404, f"Todo {id} doesn't exist")

    def create_task(self, data):
        note = Task(title=data["title"], content=data["content"], done=False)
        note.save()
        return note

    def update_task(self, id, data):
        task = Task.select().where(Task.id == id).get()
        if not task:
            abort(404)
        if not "title" in data:
            abort(400)
        if not "content" in data:
            abort(400)
        task.title = data["title"]
        task.content = data["content"]
        task.save()
        return task

    def delete_task(self, id):
        try:
            Task.get(Task.id == id).delete_instance()
        except:
            abort(404, f"Todo {id} doesn't exist.")


MODELS = [
    Task,
]


def create_tables():
    with db:
        db.create_tables(MODELS)


def drop_tables():
    with db:
        db.drop_tables(MODELS)


def filling_db():
    DAO = Task()
    DAO.create_task({"title": "Buy milk", "content": "Buy the most delicious milk"})
    DAO.create_task({"title": "Buy bread", "content": "Buy the most delicious bread"})
    DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
    DAO.create_task({"title": "Buy milk", "content": "Buy the most delicious milk"})
    DAO.create_task({"title": "Buy bread", "content": "Buy the most delicious bread"})
    DAO.create_task({"title": "Buy butter", "content": "Buy the most delicious butter"})
