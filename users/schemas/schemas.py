from models.model import Voter, db
from graphene import String, Field, Boolean
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class VoterObject(SQLAlchemyObjectType):
    class Meta:
        model = Voter
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_voters = SQLAlchemyConnectionField(VoterObject)
    
class CreateVoter(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        name = graphene.String(required=True)
        position_name = graphene.String(required=True)
    
    voter = graphene.Field(lambda: VoterObject)

    def mutate(self, info, username, name, email, position_name):
        voter = Voter.query.filter_by(username=username).first()
        use = Voter(username=username, email=email, name=name, position_name=position_name)
        db.session.add(use)
        db.session.commit()
        return CreateVoter(voter=use)

class Mutation(graphene.ObjectType):
    create_voter = CreateVoter.Field()

our_schema = graphene.Schema(query=Query, mutation=Mutation)