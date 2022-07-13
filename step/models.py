from django.db import models

# Create your models here.

class Session(models.Model):
    ids = models.CharField(max_length=50, verbose_name='Unique_ID')
    step = models.IntegerField(verbose_name='Step')
    pain = models.IntegerField(verbose_name='Pain')

    def __str__(self):
        return "{}-{}-{}".format(self.ids, self.step, self.pain)

    class Meta:
        verbose_name = 'Session'
