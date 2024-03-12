from fastapi import HTTPException

from schema.product import Product, products
from schema.order import OrderCreate, orders

class OrderService:

    @staticmethod
    def order_parser(orders):

        for order in orders:
            order_items = order.items
            new_order = []
            for product_id in order_items:
                product = products.get(product_id)
                new_order.append(product)
            order.items = new_order
        return orders
    
    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                raise HTTPException(status_code=400, detail='Product is unavailable')
            product.quantity_available -= 1
        return payload
    
    @staticmethod 
    def check_order_availability(order_id: int):
        order_set = set()
        for order in orders:
            order_set.add(order.id)
        if order_id not in order_set:
            raise HTTPException(status_code=404, detail="order does not exist")
        return order_id
    
order_service = OrderService()

