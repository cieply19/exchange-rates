from django.db import models


class Rate(models.Model):
    crypto_name = models.CharField('Name', max_length=32, editable=False)
    usd_rate = models.DecimalField(max_digits=16, decimal_places=4, editable=False)
    pln_rate = models.DecimalField(max_digits=16, decimal_places=4, editable=False)
    date = models.DateTimeField('Update date', editable=False)

    def __str__(self):
        return f'{self.crypto_name} {self.usd_rate} {self.date} {self.date}'
