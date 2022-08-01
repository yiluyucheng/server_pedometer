from django.db import models

# Create your models here.

class Session(models.Model):
    ids = models.CharField(max_length=50, verbose_name='Unique_ID')
    step = models.IntegerField(verbose_name='Step')
    pain = models.IntegerField(verbose_name='Pain')
    date = models.CharField(max_length=20, verbose_name='Date')
    distance = models.FloatField(verbose_name='Distance')
    start = models.CharField(verbose_name='Start', max_length=30)
    end = models.CharField(verbose_name='End', max_length=30)
    height = models.IntegerField(verbose_name='Height')
    weight = models.FloatField(verbose_name='Weight')
    sex = models.CharField(max_length=10, verbose_name='Sex')
    age = models.FloatField(verbose_name='Age')

    def __str__(self):
        return "{}-{}-{}".format(self.ids, self.step, self.pain)

    class Meta:
        verbose_name = 'Session'
