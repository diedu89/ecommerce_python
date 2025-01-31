import strawberry

from .mutations.product import ProductMutations
from .mutations.user import UserMutations
from .queries.product import ProductQueries
from .queries.user import UserQueries


@strawberry.type
class Query(UserQueries, ProductQueries):
    pass


@strawberry.type
class Mutation(UserMutations, ProductMutations):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
