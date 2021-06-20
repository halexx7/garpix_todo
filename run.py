from model import create_tables
from main import app

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)