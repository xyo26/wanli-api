from models import db
from flask.blueprints import Blueprint
from dataclasses import dataclass
from flask import jsonify
from decimal import Decimal

fabric_bp = Blueprint('fabric', __name__)


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
        return f"<Fabric {self.type} {self.fabric_spec} {self.dye_indicator} {self.color} {self.amount}>"


@fabric_bp.route('/fabrics', methods=['GET'])
def get_fabrics():
    fabrics = FabricModel.query.all()
    return jsonify(fabrics)
