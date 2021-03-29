from flask import Flask
from flask_cors import CORS
from models import db
from supplier import supplier_bp
from fabric import fabric_bp

# from supplier import bp

app = Flask('__main__')
CORS(app)
# TODO: db user, pass, host, name to be extracted in environment variables
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wanli:wanli@localhost:5432/wanliDB"
db.init_app(app)
app.register_blueprint(supplier_bp)
app.register_blueprint(fabric_bp)


@app.route('/healthcheck')
def health_check():
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
