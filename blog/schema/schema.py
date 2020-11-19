import graphene
from blog.schema.blog_schema import BlogModel,Blog,CreateBlog

class Query(graphene.ObjectType):

    blogs = graphene.List(Blog)
    blog = graphene.Field(Blog,id=graphene.Int(required=True))

    def resolve_blogs(self,info):
        return BlogModel.objects.all()

    def resolve_blog(self,info):
        return BlogModel.objects.all()

class Mutations(graphene.ObjectType):
    create_blog = CreateBlog.Field()
