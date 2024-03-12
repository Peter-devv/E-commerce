from fastapi import APIRouter, HTTPException, status

from schema.product import Product, ProductCreate, ProductUpdate, products

product_router = APIRouter()

# create product
# list all products

@product_router.post('/', status_code=201)
def create_product(payload: ProductCreate):
    # get the product id
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {'message': 'Product created successfully', 'data': new_product}

@product_router.get('/', status_code=200)
def list_products():
    return {'message': 'success', 'data': products}

@product_router.put("/{product_id}")
def edit_product(product_id: int, payload: ProductUpdate):
    product = None
    for key in products:
        _key = int(key)
        if _key == product_id:
            product = products.get(_key)
            break
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")

    product.name = payload.name 
    product.quantity_available = payload.quantity_available 
    product.price = payload.price 
    return {'message': 'product edited successfully', 'data': product}
