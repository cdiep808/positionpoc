from django.db import models
from django.conf import settings

# SA Model
class Sa(models.Model):
    sa_number = models.TextField()
    sa_position = models.TextField()

    #def __str__(self):
        #return self.sa_number

    def __str__(self):
        return self.sa_position
