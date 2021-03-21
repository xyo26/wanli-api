from decimal import Decimal
from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask('__main__')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://wanli:wanli@localhost:5432/wanliDB"
db = SQLAlchemy(app)


@dataclass
class FabricModel(db.Model):
    __tablename__ = 'fabric_stock'
    __table_args__ = {'schema': 'wanli_schema'}

    fabric_id: int = db.Column(db.Integer, primary_key=True)
    fabric_type: str = db.Column(db.String)
    fabric_spec: str = db.Column(db.String)
    dye_indicator: bool = db.Column(db.Boolean)
    color: str = db.Column(db.String)
    amount: Decimal = db.Column(db.Numeric)

    def __init__(self, fabric_type, fabric_spec, dye_indicator, color, amount):
        self.fabric_type = fabric_type
        self.fabric_spec = fabric_spec
        self.dye_indicator = dye_indicator
        self.color = color
        self.amount = amount

    def __repr__(self):
        return f"<Fabric {self.fabric_spec}>"


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route('/fabrics', methods=['GET'])
def get_fabrics():
    fabrics = FabricModel.query.all()
    return jsonify(fabrics)


if __name__ == '__main__':
    app.run(debug=True)
