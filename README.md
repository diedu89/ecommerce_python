# FastAPI e-commerce GraphQL API

e-commerce API built with FastAPI, GraphQL, SQLAlchemy, and Pydantic.

## Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

## Project structure

```
fastapi_ecommerce/
├── app/
│   ├── main.py          # FastAPI application
│   ├── core/            # Core settings
│   ├── db/              # Database setup
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   └── graphql/         # GraphQL resolvers
├── alembic/             # Database migrations
└── tests/              # Test suite
```
