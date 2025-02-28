from django.db import models

class Contact(models.Model):
    location=models.TextField()
    number=models.CharField(max_length=202)
    email=models.EmailField()
    web_site=models.CharField(max_length=202)
    full_name=models.CharField(max_length=202)
    message=models.TextField()
    subject=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
