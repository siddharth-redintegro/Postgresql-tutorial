import graphene
from graphene_django.types import DjangoObjectType
from blog.models import Blog as BlogModel
from django.utils import timezone

class Blog(DjangoObjectType):
    class Meta:
        model=BlogModel

class CreateBlog(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description=graphene.String()
        posted_by = graphene.String()
        posted_on = graphene.String()

    blog= graphene.Field(Blog)

    def mutate(self, info, name, description, posted_by):

        new_blog = BlogModel(
            name=name,
            description=description,
            posted_by=posted_by,
            posted_on=timezone.now()

        )

        new_blog.save()
        
        return CreateBlog(blog = new_blog)