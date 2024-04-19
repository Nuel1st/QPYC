from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    file_type = models.CharField(max_length=10, choices=[('audio', 'Audio'), ('docx', 'Document')])
    file = models.FileField(upload_to='songs/', null=True, blank=True)

    def __str__(self):
        return self.title