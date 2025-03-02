from django.db import models

class Hello(models.Model):
    image = models.FileField(upload_to='about/')
    title=models.CharField(max_length=202)
    body=models.TextField()

    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Articles(models.Model):
    image=models.FileField(upload_to='article/')
    data=models.TextField()
    title=models.CharField(max_length=202)
    description=models.TextField()
    read=models.CharField(max_length=202)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


