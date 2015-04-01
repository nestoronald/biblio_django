from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    username = models.OneToOneField(User, unique=True)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    last_login = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    def __unicode__(self):
        tag = "%s %s"%(self.name, self.surname)
        return tag
class ItemType(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
class Language(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=200)
    typ = models.ForeignKey(ItemType)
    fx_register = models.DateTimeField(blank=True, null=True)
    isbn = models.CharField(max_length=70, blank=True)
    language = models.ForeignKey(Language)
    lc = models.CharField(max_length=70, blank=True)
    dewey = models.CharField(max_length=70, blank=True)
    code_igp = models.CharField(max_length=70, blank=True)
    number_edition = models.CharField(max_length=70, blank=True)
    des_pagination = models.CharField(max_length=70, blank=True)
    des_ilustration = models.CharField(max_length=70, blank=True)
    des_dimension = models.CharField(max_length=70, blank=True)
    note_thesis = models.TextField(blank=True)
    note_bibliographic = models.TextField(blank=True)
    note_content = models.TextField(blank=True)
    note_content = models.TextField(blank=True)
    summary = models.TextField(blank=True)
    title_secundary = models.TextField(blank=True)
    fx_entry = models.DateTimeField(blank=True, null=True)
    mode_acquisition = models.CharField(max_length=70, blank=True)
    cataloger = models.CharField(max_length=70, blank=True)
    location_physical = models.CharField(max_length=70, blank=True)
    location_electronic = models.CharField(max_length=70, blank=True)
    image = models.ImageField(upload_to='static/img', blank=True)
    def __unicode__(self):
        return self.title
class Examplary(object):
    item = models.ForeignKey(Item)
    state = models.CharField(max_length=70)
    def __unicode__(self):
        return self.item.title

class ItemDetails(models.Model):
    item = models.ForeignKey(Item)
    pub_country = models.CharField(max_length=70)
    pub_editorial = models.CharField(max_length=70)
    pub_year = models.CharField(max_length=70)
    serie = models.CharField(max_length=70)
    note_general = models.TextField()
    number_entry = models.CharField(max_length=70)
    def __unicode__(self):
        return self.item.title

class ItemTheme(models.Model):
    item = models.ForeignKey(Item)
    main = models.CharField(max_length=70)
    secundary = models.CharField(max_length=70)
    def __unicode__(self):
        tag = "%s %s"%(self.item.title,self.main)
        return tag
class ItemThemeSecundary(models.Model):
    secundary = models.CharField(max_length=70)
    itemtheme = models.ForeignKey(ItemTheme)
    def __unicode__(self):
        tag = "%s %s"%(self.itemtheme.main, self.secundary)
        return tag


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    def __unicode__(self):
        tag = "%s %s"%(self.name, self.surname)
        return tag

class AuthorType(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class ItemAuthor(models.Model):
    item = models.ForeignKey(Item)
    author = models.ForeignKey(Author)
    typ = models.ForeignKey(AuthorType)
    def __unicode__(self):
        tag = "%s %s"%(self.item.title, self.author.name)
        return tag
