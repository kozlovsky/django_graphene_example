import graphene

import estore.schema

class Query(estore.schema.Query):
    pass

schema = graphene.Schema(name='E-store Schema')
schema.query = Query
