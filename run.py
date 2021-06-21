from todo import create_app, create_and_filling_db

app = create_app()
create_and_filling_db()


if __name__ == "__main__":
    app.run(debug=True)

