from django.db import models

class Warta(models.Model):
    date_uploaded = models.DateTimeField(auto_now_add=True, editable=False)
    warta = models.FileField(upload_to='wg/%Y/%m/%d/', help_text='Pastikan format PDF.')

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return 'Warta Gereja {}-{}-{}'.format(self.date_uploaded.day, self.date_uploaded.month, self.date_uploaded.year)
    