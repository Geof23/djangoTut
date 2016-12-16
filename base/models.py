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

class Feedb(models.Model):
    auth = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
    )
    Feedback_and_comments = models.TextField()

class Regs(models.Model):
    auth = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
    )
    fname = models.CharField('first name', max_length=20)
    lname = models.CharField('last name', max_length=20)
    institution = models.CharField(max_length=200)
    Poster_URL = models.CharField(max_length=200, blank=True)
    #email = models.CharField(max_length=200) #taking this from auth_user
    Phone = models.CharField('Phone number', max_length=15)
    program = models.CharField('Primary Funding Program', max_length=6, choices=PROGRAM,
                               default='si2')
    ptitle = models.CharField('NSF Award Title', max_length=100)
    nsfnum = models.CharField('NSF Award Number', max_length=20)
    Arrival_date = models.DateField('arrival date', blank=True)
    Departure_date = models.DateField('departure date', blank=True)
    airport = models.CharField('Airport (if known/applicable)', max_length=3, blank=True)
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
                '<td>' + self.ptitle + '</td>' +
                '<td><a href="' + self.Poster_URL + '">Poster</a></td>')
    def dump_header(self):
        return('fname,' +
               'lname,' +
               'institution,' +
               'Poster_URL,' +
               'Phone,' +
               'program,' +
               'ptitle,' +
               'nsfnum,' +
               'Arrival_date,' +
               'Departure_date,' +
               'airport,' +
               'parkathotel,' +
               'vegan,' +
               'vegetarian,' +
               'glutenfree,' +
               'glutenallergy,' +
               'kosher,' +
               'halal,' +
               'allergy,' +
               'other.verbose_name')
        
    # def dump_header(self):
    #     return(self.fname.verbose_name + ',' +
    #            self.lname.verbose_name + ',' +
    #            self.institution.verbose_name + ',' +
    #            self.Poster_URL.verbose_name + ',' +
    #            self.Phone.verbose_name + ',' +
    #            self.program.verbose_name + ',' +
    #            self.ptitle.verbose_name + ',' +
    #            self.nsfnum.verbose_name + ',' +
    #            self.Arrival_date.verbose_name + ',' +
    #            self.Departure_date.verbose_name + ',' +
    #            self.airport.verbose_name + ',' +
    #            self.parkathotel.verbose_name + ',' +
    #            self.vegan.verbose_name + ',' +
    #            self.vegetarian.verbose_name + ',' +
    #            self.glutenfree.verbose_name + ',' +
    #            self.glutenallergy.verbose_name + ',' +
    #            self.kosher.verbose_name + ',' +
    #            self.halal.verbose_name + ',' +
    #            self.allergy.verbose_name + ',' +
    #            self.other.verbose_name)
        
    def dump_string(self):
        return(self.fname + ',' +
               self.lname + ',' +
               self.institution + ',' +
               self.Poster_URL + ',' +
               self.Phone + ',' +
               self.program + ',' +
               self.ptitle + ',' +
               self.nsfnum + ',' +
               str(self.Arrival_date) + ',' +
               str(self.Departure_date) + ',' +
               self.airport + ',' +
               str(self.parkathotel) + ',' +
               str(self.vegan) + ',' +
               str(self.vegetarian) + ',' +
               str(self.glutenfree) + ',' +
               str(self.glutenallergy) + ',' +
               str(self.kosher) + ',' +
               str(self.halal) + ',' +
               str(self.allergy) + ',' +
               self.other)
