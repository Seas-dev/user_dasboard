from django.db import models
import re
import bcrypt

# TODO: add validator statement for passwords

# Create Validators here.
class UserValidator(models.Manager):
    def loginValidator(self, postData):
        errors = {}
        # make sure email is in the database
        email_ck = User.objects.filter(email=postData['email'])
        # if not, return an error
        if len(email_ck) != 1:
            errors['email_missing'] = "The email you entered isn't in the database"

        # if so, make sure the PW they enterd matches the one in the DB

        return errors

    def regValidator(self, postData):
        errors = {}
        # make sure the email entered is in the correct format
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = ("Invalid email address format!")
            return errors

        # make sure the email is unique and isn't in the database
        email_ck = User.objects.filter(email=postData['email'])
        if len(email_ck) > 0:
            errors['email_exist'] = "Sorry, the email you entered is already taken. Have you tried logging in?"

        # make sure first and last name are longer than 2 characters
        if len(postData['first_name']) < 2:
            errors['fname_short'] = "Your first name needs to be at least 2 characters"

        if len(postData['last_name']) < 2:
            errors['lname_short'] = "Your last name needs to be at least 2 characters"

        # make sure password is at least 8 characters and matches password confirm
        if len(postData['password']) < 8:
            errors['pw_short'] = "Your password needs to be at least 8 characters"

        if postData['password'] != postData['pw_confirm']:
            errors['pw_mismatch'] = "Your password doesn't match the confirmation password"

        return errors

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_level = models.IntegerField()
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserValidator()