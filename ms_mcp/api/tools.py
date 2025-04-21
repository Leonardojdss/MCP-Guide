from fastapi import APIRouter
from infra.postgresql_connection import get_connection_uri
import psycopg
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

conn_string = get_connection_uri()
conn = psycopg.connect(conn_string)
cursor = conn.cursor()

# Model for customer data
class Customer(BaseModel):
    name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

# Model for customer to update
class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

# Create new customer
@router.post("/customers", operation_id="create_customer")
async def create_customer(customer: Customer):
    """
    Create a new customer in the database.
    """
    cursor.execute(
        """
        INSERT INTO customer (name, email, phone, address)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """,
        (customer.name, customer.email, customer.phone, customer.address),
    )
    customer_id = cursor.fetchone()[0]
    conn.commit()
    return {"id": customer_id, "message": "Customer created successfully"}

# Get customer by ID
@router.get("/customers/{customer_id}", operation_id="get_customer")
async def get_customer(customer_id: int):
    """
    Get customer details by ID.
    """
    cursor.execute(
        """
        SELECT id, name, email, phone, address, created_at, updated_at
        FROM customer
        WHERE id = %s
        """,
        (customer_id,),
    )
    
    result = cursor.fetchone()
    if not result:
        return {"message": "Customer not found"}
    
    customer = {
        "id": result[0],
        "name": result[1],
        "email": result[2],
        "phone": result[3],
        "address": result[4],
        "created_at": result[5],
        "updated_at": result[6]
    }
    
    return customer

# Update customer
@router.put("/customers/{customer_id}", operation_id="update_customer")
async def update_customer(customer_id: int, customer: CustomerUpdate):
    """
    Update customer information.
    """
    # Converter o modelo para um dicionário e filtrar campos None
    update_data = {k: v for k, v in customer.dict().items() if v is not None}
    
    if not update_data:
        return {"message": "No fields to update provided"}
    
    # Construir dinamicamente a consulta SQL
    set_clause = ", ".join([f"{field} = %s" for field in update_data.keys()])
    set_clause += ", updated_at = CURRENT_TIMESTAMP"
    
    query = f"""
        UPDATE customer
        SET {set_clause}
        WHERE id = %s
        RETURNING id
    """
    
    # Criar lista de valores para os parâmetros da consulta
    params = list(update_data.values())
    params.append(customer_id)
    
    cursor.execute(query, params)
    
    result = cursor.fetchone()
    conn.commit()
    
    if not result:
        return {"message": "Customer not found"}
    
    return {"message": "Customer updated successfully"}

# Delete customer
@router.delete("/customers/{customer_id}", operation_id="delete_customer")
async def delete_customer(customer_id: int):
    """
    Delete a customer by ID.
    """
    cursor.execute(
        """
        DELETE FROM customer
        WHERE id = %s
        RETURNING id
        """,
        (customer_id,),
    )
    
    result = cursor.fetchone()
    conn.commit()
    
    if not result:
        return {"message": "Customer not found"}
    
    return {"message": "Customer deleted successfully"}

# List all customers
@router.get("/customers", operation_id="list_customers")
async def list_customers():
    """
    Get a list of all customers.
    """
    cursor.execute(
        """
        SELECT id, name, email, phone
        FROM customer
        ORDER BY name
        """
    )
    
    customers = []
    for row in cursor.fetchall():
        customers.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "phone": row[3]
        })
    
    return customers
