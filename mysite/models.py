#import datetime
from django.db                              import models
from django.utils                           import timezone

class Site(models.Model):
  private_site            = models.BooleanField       (default=True)
  notice                  = models.TextField          (blank=True, null=True)
  announcement            = models.TextField          (blank=True, null=True)
  contact_info            = models.CharField          (max_length=200, blank=True, null=True)
  note                    = models.TextField          (blank=True, null=True)
  def __str__(self):
    return str(self.contact_info)

class Photo(models.Model):
  author                  = models.ForeignKey         ('users.Person', related_name="authorp", on_delete=models.CASCADE, null=True)
  priority                = models.IntegerField       ('Priority of photo', default=100)
  is_live                 = models.BooleanField       (default=True)
  already_liked           = models.BooleanField       (default=False)
  upticks                 = models.IntegerField       (default=0)
  title                   = models.TextField          ('Title of photo', blank=True, null=True)
  cover                   = models.ImageField         (upload_to='images/')
  created_date            = models.DateTimeField      (default=timezone.now)
  def __str__(self):
    return self.title

class Bookmark(models.Model):
  author                  = models.ForeignKey         ('users.Person', related_name="authorb", on_delete=models.CASCADE, null=True)
  priority                = models.IntegerField       ('Priority of bookmark', default=100)
  is_live                 = models.BooleanField       (default=True)
  already_liked           = models.BooleanField       (default=False)
  upticks                 = models.IntegerField       (default=0)
  title                   = models.TextField          ('Title of bookmark')
  address                 = models.URLField           ('Address of bookmark',default='http://')
  created_date            = models.DateTimeField      (default=timezone.now)
  def __str__(self):
    return self.title

class EnquiryB(models.Model):
  #author                  = models.ForeignKey         ('users.Person', related_name="authory", on_delete=models.CASCADE, null=True)
  priority                = models.IntegerField       ('Priority of enquiry', default=100)
  is_live                 = models.BooleanField       (default=True)
  content                 = models.TextField          (blank=True, null=True)
  created_date            = models.DateTimeField      (blank=True, null=True, default=timezone.now)
  def __str__(self):
    return self.content


"""
class Response(models.Model):
  priority                = models.IntegerField       (default=100)
  is_live               = models.BooleanField       (default=True)
  content               = models.TextField          (null=True)
  #author                = models.ForeignKey         ('users.Person', related_name="authorq", on_delete=models.CASCADE, null=True)
  created_date            = models.DateTimeField      (blank=True, null=True, default=timezone.now)
  def __str__(self):
    return self.content
"""
