from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Author(models.Model):
	'''
		Author name
		2.Author email
		3.author bio 
	'''
	name= models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	bio = models.TextField()

	def __str__(self): 
		return self.name

class Category(models.Model):
	cat_name = models.CharField('category name',max_length=50)
	cat_description = models.CharField('category description',max_length=255)

	class Meta: 
		verbose_name_plural = 'Categories'

	def __str__(self): 
		return self.cat_name



class Tag (models.Model): 
	tag_name = models.CharField(max_length=50)
	tag_description = models.CharField(max_length=255)


	def __str__(self): 
		return self.tag_name


class Post (models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	create_date = models.DateTimeField(auto_now_add=True, auto_now = False)
	updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
	author = models.ForeignKey(Author)
	categories = models.ManyToManyField(Category)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title




	