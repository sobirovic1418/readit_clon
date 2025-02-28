from django.db import models

class Team(models.Model):
    body=models.TextField()
    image=models.FileField(upload_to='team/')
    full_name=models.CharField(max_length=202)
    work=models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

class Home(models.Model):
    image=models.FileField(upload_to='home/')
    title=models.CharField(max_length=202)
    body=models.TextField()

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



