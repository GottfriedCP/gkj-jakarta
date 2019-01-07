from django.db import models
from django.core.validators import FileExtensionValidator

class Warta(models.Model):
    date_uploaded = models.DateTimeField(auto_now_add=True, editable=False)
    warta = models.FileField('File Warta (PDF)', upload_to='wg/%Y/%m/%d/', help_text='Mohon pastikan format file adalah PDF.', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])

    class Meta:
        ordering = ['-date_uploaded']

    def __str__(self):
        return 'Warta Gereja {}-{}-{}'.format(self.date_uploaded.day, self.date_uploaded.month, self.date_uploaded.year)
    