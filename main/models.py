from django.db import models

# Create your models here.
class CCCD(models.Model):
    cccd=models.CharField(max_length=12, unique=True)

    def __str__(self):
	    return self.cccd

class GetInfor(models.Model):
    cccd = models.ForeignKey(CCCD, on_delete=models.CASCADE) # <--- added
    name = models.CharField(max_length=200)
    birth = models.DateField()
    gender = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=12)
    location = models.CharField(max_length=300)
    guardian = models.CharField(max_length=200)
    queuenumber = models.CharField(max_length=6)
    #img_port = models.ImageField(null=True, upload_to='images/')
    #img_tokhaimau = models.ImageField(null=True, upload_to='images/')
    #img_nguoidaidien = models.ImageField(null=True, upload_to='images/')
    #img_hochieu = models.ImageField(null=True, upload_to='images/')

    def __str__(self):
	    return self.name

class Queue(models.Model):
    day=models.IntegerField(unique=True)
    month=models.IntegerField(unique=True)
    stt= models.IntegerField(unique=True)

    def __str__(self):
        if self.stt<10:
            stt='0'+str(self.stt)
        else:
            stt=str(self.stt)
        if self.month<10:
            month='0'+str(self.month)
        else:
            month=str(self.month)
        if self.day<10:
            day='0'+str(self.day)
        else:
            day=str(self.day)
        return month+day+stt