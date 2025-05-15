import os
import django
from mongoengine import connect
from products.models import Product

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'petstore.settings')
django.setup()

# MongoDB Configuration
MONGODB_DATABASE = 'petstore'
MONGODB_HOST = 'mongodb://localhost:27017/'

# Connect to MongoDB
connect(
    db=MONGODB_DATABASE,
    host=MONGODB_HOST,
    alias='default'
)

initial_products = [
    {
        "name": "Premium Dog Food",
        "description": "High-protein, grain-free formula for adult dogs",
        "image": "static/assets/images/dog_food.jpeg",
        "price": 49.99,
        "category": "dog"
    },
    {
        "name": "Durable Chew Toy",
        "description": "Tough rubber toy designed for heavy chewers",
        "image": "static/assets/images/dog_toy.jpg",
        "price": 14.99,
        "category": "dog"
    },
    {
        "name": "Orthopedic Dog Bed",
        "description": "Memory foam bed for joint support and comfort",
        "image": "static/assets/images/dog_bed.jpeg",
        "price": 79.99,
        "category": "dog"
    },
    {
        "name": "Organic Cat Food",
        "description": "Grain-free recipe with real chicken",
        "image": "static/assets/images/cat_food.jpeg",
        "price": 39.99,
        "category": "cat"
    },
    {
        "name": "Cat Tree",
        "description": "Multi-level cat tree with scratching posts",
        "image": "static/assets/images/cat_tree.jpeg",
        "price": 89.99,
        "category": "cat"
    },
    {
        "name": "Interactive Laser Toy",
        "description": "Automatic laser toy for engaging playtime",
        "image": "static/assets/images/cat_laser.jpeg",
        "price": 24.99,
        "category": "cat"
    }
]

def run():
    Product.objects.all().delete()

    last_product = Product.objects.order_by('-product_id').first()
    new_id = (last_product.product_id + 1) if last_product else 1

    for product in initial_products:
        product["product_id"] = new_id
        Product(**product).save()
        new_id += 1

    print("Successfully loaded initial products!")

if __name__ == "__main__":
    run()
