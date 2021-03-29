from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# @dataclass
# class DyeFactoryModel(db.Model):
#     __tablename__ = 'dye_factory'
#     __table_args__ = {'schema': 'wanli_schema'}
#
#     factory_id: int = db.Column(db.Integer, primary_key=True)
#     name: str = db.Column(db.String)
#     address: str = db.Column(db.String)
#     phone_number: str = db.Column(db.String)
#
#     def __init__(self, name, address, phone_number):
#         self.name = name
#         self.address = address
#         self.phone_number = phone_number
#
#     def __repr__(self):
#         return f"<Dye Factory {self.name} {self.address} {self.phone_number}>"
#
#
# @dataclass
# class CustomerModel(db.Model):
#     __tablename__ = 'customer'
#     __table_args__ = {'schema': 'wanli_schema'}
#
#     customer_id: int = db.Column(db.Integer, primary_key=True)
#     name: str = db.Column(db.String)
#     phone_number: str = db.Column(db.String)
#
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number
#
#     def __repr__(self):
#         return f"<Customer {self.name} {self.phone_number}>"
