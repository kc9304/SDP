from django.db import models


# Create your models here.
class Login(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table = 'login_table'

    def __str__(self):
        return self.username


class Signup1(models.Model):
    name = models.CharField(max_length=150, blank=False, unique=True)
    psw = models.CharField(max_length=100, blank=False)
    class Meta:
        db_table = 'Signup1_table'

class Comic(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)

    class Meta:
        db_table = 'Comic_table'

    def __str__(self):
        return self.name


from django.db import models

class Personal(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=False)
    alternative_number = models.CharField(max_length=15, blank=True, null=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=50, blank=False)
    town = models.CharField(max_length=50, blank=False)


    class Meta:
        db_table = 'Personal_table'
