from models import db
from flask.blueprints import Blueprint
from dataclasses import dataclass
from flask import jsonify

supplier_bp = Blueprint('supplier', __name__)


@dataclass
class SupplierModel(db.Model):
    __tablename__ = 'supplier'
    __table_args__ = {'schema': 'wanli_schema'}

    supplier_id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String)
    address: str = db.Column(db.String)
    phone_number: str = db.Column(db.String)

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __repr__(self):
        return f"<Supplier {self.name} {self.address} {self.phone_number}>"


@supplier_bp.route('/suppliers', methods=['GET'])
def get_suppliers():
    fabrics = SupplierModel.query.all()
    return jsonify(fabrics)
