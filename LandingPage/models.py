from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
# Article class.

class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    cover = models.ImageField(upload_to='images/', null=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


# registration class.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    E_mail = models.EmailField(max_length=254)
    COUNTRY_CHOICES = [('saudi arabia +966','SAUDI ARABIA +966'),
                       ('oman +968','OMAN +968'),
                       ('kuwait +965','KWUAIT +965'),
                       ('Qatar +948','QATAR +948')]
    country = models.CharField(max_length=250, choices=COUNTRY_CHOICES, null=True)
    phone = models.IntegerField(null=True)
    #phone = PhoneNumberField()
    #phone = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    phone_code = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    NATIONALITY_CHOICES = (('1', 'خليجي'), ('2', 'ليس خليجي'))
    nationality = models.CharField(max_length=250, choices=NATIONALITY_CHOICES, null=True)

    def __str__(self):
        return self.first_name







    #phone = models.CharField(null=True, max_length=10, validators=[RegexValidator(r'^\d{1,15}$')])
    #phone_code = PhoneNumberPrefixWidget(null=True)
    #phone = PhoneNumberField(null=True)
