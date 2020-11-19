import graphene
from graphene_django.types import DjangoObjectType
from blog.models import User as User_Model


class User(DjangoObjectType):
    class Meta:
        model = User_Model


class CreateUser(graphene.Mutation):
    class Arguments:
        user_name = graphene.String(required=True)
        user_desc = graphene.String(required=True)
        user_phone = graphene.String(required=True)
        user_email = graphene.String(required=True)
        user_password = graphene.String(required=True)

    user = graphene.Field(User)

    def mutate(self, info, user_name, user_desc, user_phone, user_email, user_password):
        new_user = User_Model(
            user_name=user_name,
            user_desc=user_desc,
            user_phone=user_phone,
            user_email=user_email,
            user_password=user_password
        )
        new_user.save()
        return CreateUser(user=new_user)

class UpdateUser(graphene.Mutation):
    class Arguments:
        user_email = graphene.String(required=True)
        id = graphene.Int()
    
    message = graphene.String()

    def mutate(self,info,user_email,id):
        old_user = User_Model.objects.get(pk=id)
        old_email = old_user.user_email
        old_user.user_email = user_email
        old_user.save()
        return UpdateUser(message=f'New Email:{user_email} Old Email:{old_email} Id:{id}')


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    message = graphene.String()

    def mutate(self,info,id):
        old_user = User_Model.objects.get(pk=id)
        old_user.delete()
        return DeleteUser(message=f'Deleted User Id:{id}')