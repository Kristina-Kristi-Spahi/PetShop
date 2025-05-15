from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Product
from django.shortcuts import render
from bson import ObjectId


from django.http import JsonResponse

def get_products(request):
    try:
        products = Product.objects.all()
        response_data = {
            'dog': [],
            'cat': []
        }

        for product in products:
            product_data = {
                'id': str(product.id),  # ✅ Convert ObjectId to string
                'name': product.name,
                'description': product.description,
                'image': product.image,
                'price': product.price
            }
            response_data[product.category].append(product_data)

        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def index(request):
    return render(request, 'index.html')

def login_view(request):
    return render(request, "login.html")

def add_products(request):
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            description = request.POST.get('description')
            image = request.POST.get('image')
            price = request.POST.get('price')
            category = request.POST.get('category')

            if not (name and description and image and price and category):
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # Get the highest existing product_id and increment
            last_product = Product.objects.order_by('-product_id').first()
            new_id = (last_product.product_id + 1) if last_product else 1

            # Create and save the new product
            product = Product(
                product_id=new_id,
                name=name,
                description=description,
                image=image,
                price=float(price),
                category=category
            )
            product.save()

            return JsonResponse({'message': 'Product added successfully'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return render(request, "form.html")

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)  # Fetch the product by ID
        product.delete()  # Delete the product
        return JsonResponse({"status": "success", "message": "Product deleted successfully"})
    except Product.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Product not found"}, status=404)
