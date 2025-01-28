from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.api.v1 import auth
from app.graphql.schema import schema
from app.graphql.context import get_context

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI E-commerce API"}


graphql_app = GraphQLRouter(schema, context_getter=get_context)

app.include_router(graphql_app, prefix="/graphql")
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
