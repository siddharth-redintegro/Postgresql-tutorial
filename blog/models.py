from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.TextField()
    description = models.TextField()
    posted_by = models.TextField()
    posted_on = models.DateTimeField()

class User(models.Model):
    user_name = models.TextField()
    user_desc = models.TextField()
    user_phone = models.TextField()
    user_email = models.TextField()
    user_password = models.TextField()


#create user model name,userid,mobile with crud operations