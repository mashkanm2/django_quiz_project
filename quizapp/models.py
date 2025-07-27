# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from .managers import PublishedPostManager

class AuthUser(models.Model):
    username = models.CharField(unique=True)
    email = models.CharField()
    password = models.CharField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Author(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    title = models.CharField()
    author = models.ForeignKey(Author, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'book'


class Company(models.Model):
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'company'


class DjangoContentType(models.Model):
    app_label = models.CharField()
    model = models.CharField()

    class Meta:
        managed = False
        db_table = 'django_content_type'


class Employee(models.Model):
    name = models.CharField()
    company = models.ForeignKey(Company, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee'


class Photo(models.Model):
    file_path = models.CharField()

    class Meta:
        managed = False
        db_table = 'photo'


class Post(models.Model):
    title = models.CharField()
    is_published = models.BooleanField()

    published=PublishedPostManager()

    objects = models.Manager() 

    class Meta:
        managed = False
        db_table = 'post'
    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    bio = models.TextField()

    class Meta:
        managed = False
        db_table = 'profile'
    
    def __str__(self):
        return self.user.username


class Survey(models.Model):
    questions_json = models.TextField()

    class Meta:
        managed = False
        db_table = 'survey'


class Tag(models.Model):
    name = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'tag'


class Taggeditem(models.Model):
    tag = models.ForeignKey(Tag, models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    object_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taggeditem'


class Tenant(models.Model):
    schema_name = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'tenant'
