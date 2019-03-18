from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime, uuid

def tomorrow():
    return timezone.now() + datetime.timedelta(days=1)

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField(default=timezone.now, help_text='Tanggal pembuatan pengumuman.')
    date_expired = models.DateTimeField(default=tomorrow, help_text='Tanggal berakhirnya pengumuman.')
    summary = models.TextField(max_length=1000, help_text='(Wajib diisi) Ringkasan isi pengumuman.')
    content = models.TextField()

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('homepage:ann', args=[self.id])

    def get_edit_url(self):
        return reverse('homepage:edit_ann', args=[self.id])
