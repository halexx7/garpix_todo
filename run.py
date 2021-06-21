from todo import create_app
from todo.models.task_model import drop_tables

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
