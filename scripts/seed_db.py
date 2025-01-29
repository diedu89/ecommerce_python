import aiohttp
import asyncio
from app.db.session import SessionLocal
from app.services.product_service import ProductService
from app.services.user_service import UserService
from app.schemas.product import ProductCreate
from app.schemas.user import UserCreate


async def fetch_and_seed_products():
    db = SessionLocal()
    product_service = ProductService(db)

    try:
        # Check if products exist
        products = product_service.get_all_products()
        if len(products) > 0:
            print("Products already exist in database, skipping seed")
            return

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
    user_service = UserService(db)

    try:
        if not user_service.get_user_by_email("admin@example.com"):
            admin_data = UserCreate(
                username="admin",
                email="admin@example.com",
                password="test123",
                is_superuser=True,
            )
            user_service.create_user(admin_data)
            print("Admin user created successfully")
        else:
            print("Admin user already exists")
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(fetch_and_seed_products())
    asyncio.run(create_admin_user())
