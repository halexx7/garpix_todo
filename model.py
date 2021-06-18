from peewee import CharField, Model, SqliteDatabase, TextField, BooleanField, DateTimeField
from datetime import datetime


db = SqliteDatabase('todo.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    text = TextField()
    done = BooleanField()

    dateAdded = DateTimeField(default=datetime.now)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'text': str(self.text).strip(),
            'done': str(self.done).strip(),
            'dateAdded': self.dateAdded,
        }
        return data

    def __repr__(self):
        return f'{self.id}, {self.text}, {self.done}, {self.dateAdded}'

db.connect()
db.create_tables(Note, safe=True)