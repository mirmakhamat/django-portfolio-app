from django.db import models


class Info(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    hero_image = models.FileField(upload_to='images/')
    image = models.FileField(upload_to='images/')
    about = models.TextField()
    happy_clients = models.IntegerField(default=0)
    project_completed = models.IntegerField(default=0)
    awards_won = models.IntegerField(default=0)

    facebook_link = models.CharField(max_length=255, blank=True, null=True)
    twitter_link = models.CharField(max_length=255, blank=True, null=True)
    instagram_link = models.CharField(max_length=255, blank=True, null=True)
    linkedin_link = models.CharField(max_length=255, blank=True, null=True)


class Service(models.Model):
    title = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    content = models.TextField()

    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    likes = models.IntegerField()
    comments = models.IntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class ContactInfo(models.Model):
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class GetInTouch(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self) -> str:
        return self.email
