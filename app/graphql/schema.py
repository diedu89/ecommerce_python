import strawberry
from .queries.user import UserQueries
from .queries.product import ProductQueries
from .mutations.user import UserMutations
from .mutations.product import ProductMutations


@strawberry.type
class Query(UserQueries, ProductQueries):
    pass


@strawberry.type
class Mutation(UserMutations, ProductMutations):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
