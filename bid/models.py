from sys import modules
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False) #type: ignore
    project_owner = models.BooleanField(default=False) #type: ignore


class Project(models.Model):
    name = models.CharField(max_length=255)
    save_url = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    video_url = models.TextField()
    version = models.PositiveSmallIntegerField(default=1) #type: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name= "owned_projects")
    admin_approved = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name='approved_projects')


class Comment(models.Model):
    comment = models.CharField(255)
    score = models.PositiveSmallIntegerField(
        validators= [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    project = models.ForeignKey(Project , on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)


# this model needs to check as well
class ChatHistory(models.Model):
    # TODO: check on delete on here, if its ok
    first_user = models.ForeignKey(User , null = True, on_delete= models.SET_NULL , related_name= 'chat_for_first_user')
    second_user = models.ForeignKey(User , null = True, on_delete= models.SET_NULL , related_name= 'chat_for_second_user')
    message = models.TextField()
    time = models.DateTimeField(auto_now_add = True)
    is_seen = models.BooleanField(default= False) # type: ignore


class Tags(models.Model):
    tag = models.CharField(55)


class Notification(models.Model):
    title = models.CharField(255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    is_read = models.BooleanField(default= False) # type: ignore


class Transaction(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add = True)
    project = models.ForeignKey(Project , on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)


class Score(models.Model):

    @staticmethod
    def get_score_with_validation():
        return models.PositiveSmallIntegerField(
            validators= [
                MaxValueValidator(5),
                MinValueValidator(1)
            ]
        )

    score_giver = models.ForeignKey(User, on_delete= models.CASCADE)
    project = models.ForeignKey(Project , on_delete= models.CASCADE)
    clean = get_score_with_validation() # type: ignore
    easy_run = get_score_with_validation()
    complexity = get_score_with_validation()
    document = get_score_with_validation()
    test = get_score_with_validation()
    eror = get_score_with_validation()
    bugs = get_score_with_validation()

class BugReport(models.Model):
    title = models.CharField(255)
    description = models.TextField()
    project = models.ForeignKey(Project , on_delete= models.CASCADE)
    ticket_sender = models.ForeignKey(User , on_delete= models.CASCADE)
    resource_url1 = models.TextField()
    resource_url2 = models.TextField()
    resource_url3 = models.TextField()
    resource_url4 = models.TextField()
