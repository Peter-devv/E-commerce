from fastapi import HTTPException, status

from schema.customer import customers, CustomerCreate

class CustomerService:

    @staticmethod
    def check_existing_user(customer_in: CustomerCreate):
        for customer in customers:
            if customer_in.username == customer.username:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists.") 
        return customer_in
    
customer_service = CustomerService()    