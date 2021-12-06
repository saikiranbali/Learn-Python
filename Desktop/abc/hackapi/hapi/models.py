from django.db import models


class HackApi(models.Model):
    name = models.CharField(max_length=60)
    var_a = models.IntegerField(default=0)
    var_b = models.IntegerField(default=0)
    addd = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.addd = (self.var_a + self.var_b)
        super(HackApi, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
