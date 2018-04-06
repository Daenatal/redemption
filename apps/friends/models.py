# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        #checking everything for emptyness
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ''))
            if field == 'password':
                if not field in errors and len(value) < 8:
                    errors[field] = '{} field must be at least 8 characters'.format(field.replace('_', ''))
            if field == 'username':
                if not field in errors and len(value) < 5:
                    errors[field] = '{} field must be at least 5 characters'.format(field.replace('_', ''))
            if field == 'confirmpass':
                temp = self.get(username=postData['username'])
                if temp.password != postData['confirmpass']:
                    errors[field] = 'incorrect password'
        return errors

#creating users table first
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.CharField(max_length=20)
    buddies = models.ManyToManyField('self', blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.name
