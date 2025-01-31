import asyncio

import aiohttp
from passlib.context import CryptContext

from app.core.security import get_password_hash
from app.db.session import SessionLocal
from app.models.user import User
from app.schemas.product import ProductCreate
from app.services.product_service import ProductService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def fetch_and_seed_products():
    db = SessionLocal()
    product_service = ProductService(db)

    try:
        # Check if products exist
        paginated_products = product_service.get_all_products()
        if paginated_products.total > 0:
            print("Products already exist in database, skipping seed")
            return
        products = []
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://dummyjson.com/products?limit=200"
            ) as response:
                data = await response.json()
                products = data["products"]

        for product_data in products:
            product_create = ProductCreate(
                title=product_data["title"],
                price=float(product_data["price"]),
                description=product_data["description"],
                category=product_data["category"],
                image=product_data["images"][0],
                stock=product_data["stock"],
                is_active=True,
            )
            product_service.create_product(product_create)
        print(f"Successfully seeded {len(products)} products")
    except Exception as e:
        print(f"Error seeding products: {e}")
    finally:
        db.close()


async def create_admin_user():
    db = SessionLocal()

    try:
        # Check if admin exists directly using the User model
        admin = (
            db.query(User).filter(User.email == "admin@example.com").first()
        )

        if not admin:
            # Create admin user directly
            admin = User(
                username="admin",
                email="admin@example.com",
                hashed_password=get_password_hash("test123"),
                is_active=True,
                is_superuser=True,
            )
            db.add(admin)
            db.commit()
            print("Admin user created successfully")
        else:
            print("Admin user already exists")
    except Exception as e:
        print(f"Error creating admin user: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(fetch_and_seed_products())
    asyncio.run(create_admin_user())
