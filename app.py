from flask_openapi3 import OpenAPI
from flask_sqlalchemy import SQLAlchemy


app = OpenAPI(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:root@localhost/testdb"


@app.route('/')
def hello_world():
    return 'Hello World!'


db = SQLAlchemy(app)


from audit import audit_bp

app.register_api(audit_bp)

if __name__ == '__main__':
    app.run()
    db.create_all()
