from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    desc=models.TextField(max_length=100)
    def __str__(self):
        return self.name
class team(models.Model):
    id_name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pic')
    descrip=models.TextField(max_length=100)

    def __str__(self):
        return self.id_name