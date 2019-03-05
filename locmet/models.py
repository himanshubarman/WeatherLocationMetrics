from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class BaseMetrics(models.Model):


    MONTH_LIST = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sept'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec')
        )

    def year_validation(value):
        error_flag = False
        if (len(str(value)) == 4) or (value in range(1600,2021)):
            raise ValidationError(('%(value)s is not a valid year'),
            params={'value': value},
        )


    bid = models.AutoField(primary_key = True)
    value = models.IntegerField()
    year = models.IntegerField(validators = [year_validation])
    month = models.IntegerField(choices = MONTH_LIST)
    location = models.CharField(max_length = 1000)

    class Meta:
        abstract = True
        unique_together = (('location','year','month'),)


class Tmax(BaseMetrics):
    pass

class Tmin(BaseMetrics):
    pass

class Rainfall(BaseMetrics):
    pass







