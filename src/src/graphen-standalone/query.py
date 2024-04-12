import pdb
import graphene
from graphene import ObjectType, Schema, String


class Query(ObjectType):
    name = String(name=String(default_value="Stranger"))
    goodbye = String()

    def resolve_name(root, info, name):
        return f"welcome {name}!"

    def resolve_goodbye(root, info):
        return "Good Bye!"


schema = Schema(query=Query)

pdb.set_trace()
