from django.db import models

# Create your models here.
class contactus(models.Model):
    status=False
    Name=models.CharField(max_length=50)
    Mobile=models.CharField(max_length=25)
    Email=models.CharField(max_length=50)
    Message=models.TextField()
    #def __str__(self):
        #return self.Name
class city(models.Model):
    city=models.CharField(max_length=100)
    cpic=models.ImageField(upload_to='static/city/',default="")
    def __str__(self):
      return self.city

class category(models.Model):
    cname=models.CharField(max_length=200)
    def __str__(self):
       return self.cname
class news(models.Model):
    headline=models.CharField(max_length=500)
    newspic=models.ImageField(upload_to='static/news/', default="")
    ndes=models.TextField()
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    cdate=models.DateField()
    def __str__(self):
        return self.headline
class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=300)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',null=True)
    def __str__(self):
        return self.shead
class videos(models.Model):
    vhead=models.CharField(max_length=100)
    vdes=models.CharField(max_length=300)
    vlink=models.CharField(max_length=500)
    vpic=models.ImageField(upload_to='static/videos/', default="")
    def __str__(self):
        return self.vhead
class bnews(models.Model):
    bhead=models.CharField(max_length=300)
    bdate=models.DateField()
    bdes=models.TextField()
    bpic=models.ImageField(upload_to='static/bnews/',default="")
    def __str__(self):
        return self.bhead
