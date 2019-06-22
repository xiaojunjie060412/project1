from django.db import models

# Create your models here.


class Photographer(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    info = models.CharField(max_length=200, default=None)
    headimage = models.ImageField(upload_to='headimage')

    def __str__(self):
        return self.name


class Classify(models.Model):
    title = models.CharField(max_length=20)
    photographer = models.ManyToManyField(Photographer)

    def __str__(self):
        return self.title


class MyPicture(models.Model):
    pic = models.ImageField(upload_to='picture')
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE)
    belong = models.ForeignKey(Photographer, on_delete=models.CASCADE)
    intro = models.CharField(max_length=200)

    def __str__(self):
        return self.intro


class Celebrity(models.Model):
    name = models.CharField(max_length=20)
    headimage = models.ImageField(upload_to='headimage')
    dictum = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    content = models.TextField()

    def __str__(self):
        return self.name
