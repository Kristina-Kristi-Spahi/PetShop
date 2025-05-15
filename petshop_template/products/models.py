from mongoengine import Document, fields

class Product(Document):
    product_id = fields.IntField(unique=True, required=True)
    name = fields.StringField(required=True, max_length=100)
    description = fields.StringField()
    image = fields.StringField()
    price = fields.FloatField()
    category = fields.StringField(choices=('dog', 'cat'))