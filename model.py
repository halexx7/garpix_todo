from peewee import CharField, Model, SqliteDatabase, TextField, BooleanField, DateTimeField
from datetime import datetime


db = SqliteDatabase('todo.sqlite')
class BaseModel(Model):
    class Meta:
        database = db

class Task(BaseModel):

    title = CharField(max_length=150)
    content = TextField()
    done = BooleanField()

    create_at = DateTimeField(default=datetime.now)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'title': str(self.title).strip(),
            'content': str(self.content).strip(),
            'done': self.done,
            'create_at': self.create_at,
        }
        return data

    def __repr__(self):
        return f'{self.id}, {self.title}, {self.content}, {self.create_at}'
        

def create_tables():
    print('done')
    with db:
        db.create_tables([Task,])