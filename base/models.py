from django.db import models
from django.contrib.auth.models import User

# Create your models here.

PROGRAM = (
    ('si2','SI2'),
    ('eager','EAGER'),
    ('rapid','RAPID'),
    ('voss','VOSS'),
    ('career','CAREER'),
)

class Regs(models.Model):
    auth = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
    )
    fname = models.CharField('first name', max_length=20)
    lname = models.CharField('last name', max_length=20)
    institution = models.CharField(max_length=200)
    #email = models.CharField(max_length=200) #taking this from auth_user
    phone = models.CharField(max_length=20)
    program = models.CharField(max_length=6, choices=PROGRAM,
                               default='si2')
    ptitle = models.CharField('program title', max_length=100)
    nsfnum = models.CharField('nsf number', max_length=20)
    adate = models.DateTimeField('arrival date', blank=True)
    airport = models.CharField(max_length=3, blank=True)
    parkathotel = models.BooleanField('park at the hotel')
    vegan = models.BooleanField()
    vegetarian = models.BooleanField()
    glutenfree = models.BooleanField('gluten free')
    glutenallergy = models.BooleanField('gluten allergy')
    kosher = models.BooleanField()
    halal = models.BooleanField()
    allergy = models.CharField('list allergies', max_length=100, blank=True)
    other = models.CharField('other relevant info', max_length=100, blank=True)

    def pub_string(self):
        return ('<td>' + self.lname + '</td>' +
                '<td>' + self.fname + '</td>' +
                '<td>' + self.institution + '</td>' +
                '<td>' + self.ptitle + '</td>')
    
