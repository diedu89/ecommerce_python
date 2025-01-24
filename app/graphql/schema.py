import strawberry
from .queries.user import UserQueries
from .mutations.user import UserMutations


@strawberry.type
class Query(UserQueries):
    pass


@strawberry.type
class Mutation(UserMutations):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
