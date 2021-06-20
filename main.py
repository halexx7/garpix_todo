from flask import Flask, jsonify
from flask_restx import Api, Resource, fields
import requests
from werkzeug.middleware.proxy_fix import ProxyFix
from model import db
from datetime import datetime
from peewee import CharField, Model, SqliteDatabase, TextField, BooleanField, DateTimeField

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='TodoMVC API',
    description='A simple TodoMVC API',
)

ns = api.namespace('api/task/', description='TODO operations')

task_list = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The title task'),
    'content': fields.String(required=True, description='The content task'),
    'done': fields.Boolean(requests=True, description='Task completion mark')

})

task = api.model('Task_detail', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'title': fields.String(required=True, description='The title task'),
    'content': fields.String(required=True, description='The title task'),
})

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

create_tables()


class TaskDAO(object):

    def get_all(self):
        tasks = Task.select()
        tasks_json = []
        for task in tasks:
            tasks_json.append({
                "id": task.id,
                "title": task.title,
                "create_at": task.create_at
            })
        return tasks_json

    def get(self, id):
        print(id)
        task = Task.select().where(Task.id == id).get()
        if task:
            return task
        api.abort(404, f"Todo {id} doesn't exist")

    def create(self, data):
        note = Task(title=data['title'], content=data['content'], done=False)
        note.save()
        return note

    def update(self, id, data):
        task = Task.select().where(Task.id == id).get()
        if not task:
            api.abort(404)
        if not 'title' in data:
            api.abort(400)
        if not 'content' in data:
            api.abort(400)
        if not 'done' in data is not bool:
            api.abort(400)
        print('2')
        task.title = data['title']
        task.content = data['content']
        task.done = True if data['done'] == 'True' else False
        task.save()
        return task

    def delete(self, id):
        try:
            Task.get(Task.id == id).delete_instance()
        except:
            api.abort(404, f"Todo {id} doesn't exist.")


DAO = TaskDAO()
# DAO.create({'title': 'Buy milk', 'content': 'Buy the most delicious milk'})
# DAO.create({'title': 'Buy bread', 'content': 'Buy the most delicious bread'})
# DAO.create({'title': 'Buy butter', 'content': 'Buy the most delicious butter'})


@ns.route('/')
class TodoList(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    @ns.doc('list_todos')
    @ns.marshal_list_with(task_list)
    def get(self):
        '''List all tasks'''
        return DAO.get_all()

    @ns.doc('create_todo')
    @ns.expect(task_list)
    @ns.marshal_with(task_list, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@ns.route('/<int:id>')
@ns.response(404, 'Todo not found')
@ns.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @ns.doc('get_todo')
    @ns.marshal_with(task_list)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @ns.doc('delete_todo')
    @ns.response(204, 'Todo deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @ns.expect(task_list)
    @ns.marshal_with(task_list)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)


if __name__ == '__main__':
    app.run(debug=True)