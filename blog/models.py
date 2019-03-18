from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
import uuid

# Create your models here.
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('Judul:', max_length=500, unique=True)
    slug = models.SlugField(max_length=100, editable=False)
    published = models.BooleanField('Rilis artikel?', default=True)
    comment_allowed = models.BooleanField('Izinkan komentar pembaca?', default=True)
    summary = models.TextField('Ringkasan (opsional, sebaiknya diisi):', max_length=1000, blank=True, null=True)
    content = models.TextField('Isi artikel:')
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    author = models.CharField('Penulis:', max_length=100, blank=True, null=True, help_text='Identitas pembuat artikel asli')

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return str(self.title)

    def save(self):
        self.slug = slugify(str(self.title))
        super().save()

    def get_absolute_url(self):
        return reverse('blog:article', args=[self.date_created.year, self.slug])

    def get_edit_url(self):
        return reverse('blog:edit', args=[self.date_created.year, self.slug])
