from flask import request
from flask_restx import Namespace, Resource, fields

from ..models.task_model import Task

ns = Namespace("api/task/", description="TODO operations")

task = ns.model(
    "Task",
    {
        "id": fields.Integer(readonly=True, description="The task unique identifier"),
        "title": fields.String(required=True, description="The title task"),
        "content": fields.String(required=True, description="The content task"),
        "create_at": fields.DateTime(required=True, description="Create date"),
    },
)

task_create = ns.model(
    "Task_create",
    {
        "title": fields.String(required=True, description="The title task"),
        "content": fields.String(required=True, description="Create date"),
    },
)

task_list = ns.model(
    "Task_list",
    {
        "title": fields.String(required=True, description="The title task"),
        "create_at": fields.DateTime(required=True, description="Create date"),
    },
)

task_detail = ns.model(
    "Task_detail",
    {
        "title": fields.String(required=True, description="The title task"),
        "content": fields.String(required=True, description="Create date"),
        "create_at": fields.DateTime(required=True, description="Create date"),
    },
)

DAO = Task()


@ns.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @ns.doc("list_todos")
    @ns.marshal_list_with(task_list)
    def get(self):
        """List all tasks"""
        return DAO.get_all()

    @ns.doc("create_todo")
    @ns.expect(task_create)
    @ns.marshal_with(task, code=201)
    def post(self):
        """Create a new task"""
        return DAO.create(request.json), 201


@ns.route("/<int:id>")
@ns.response(404, "Todo not found")
@ns.param("id", "The task identifier")
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @ns.doc("get_todo")
    @ns.marshal_with(task_detail)
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @ns.doc("delete_todo")
    @ns.response(204, "Todo deleted")
    def delete(self, id):
        """Delete a task given its identifier"""
        DAO.delete(id)
        return "", 204

    @ns.expect(task_create)
    @ns.marshal_with(task)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update_task(id, request.json)
