from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wanli:wanli@localhost:5432/wanliDB"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class FabricModel(db.Model):
    __table_args__ = {'schema': 'wanli_mgr'}
    __tablename__ = 'FABRIC_STOCK'

    FABRIC_ID = db.Column(db.Integer, primary_key=True)
    TYPE = db.Column(db.String)
    SPECIFICATION = db.Column(db.String)
    DYE_INDICATOR = db.Column(db.String)
    COLOR = db.Column(db.Boolean)
    AMOUNT = db.Column(db.Integer)

    def __init__(self, type, specification, dye_indicator, color, amount):
        self.TYPE = type
        self.SPECIFICATION = specification
        self.DYE_INDICATOR = dye_indicator
        self.COLOR = color
        self.AMOUNT = amount

    def __repr__(self):
        return f"<Fabric {self.SPECIFICATION}>"


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route("/<your_name>")
def hello(your_name):
    return 'hello ' + your_name


@app.route('/fabrics', methods=['GET'])
def get_fabrics():
    # return {"msg": "looks good"}
    if request.method == 'POST':
        return {"error": "Invalid request method"}

    elif request.method == 'GET':
        fabrics = FabricModel.query.all()
        results = [
            {
                "specification": fabric.SPECIFICATION,
                "type": fabric.TYPE
            } for fabric in fabrics]

        return {"count": len(results), "fabrics": results}


if __name__ == '__main__':
    app.run(debug=True)
