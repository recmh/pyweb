from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    mobile = models.CharField(max_length=11,null=True)
    email = models.EmailField(null=True)
    ip = models.GenericIPAddressField(null=True)
    nickname = models.CharField(max_length=50,null=True)
    signup_at = models.DateTimeField(null=True,auto_now_add=True)
    lastlogin = models.DateTimeField(null=True)
    
    def __str__(self):
        return '{name:%s,password:%s,mobile:%s,email:%s,ip:%s,nickname:%s,signup_at:%s,lastlogin:%s}' % (self.name,self.password,self.mobile,self.email,self.ip,self.nickname,self.signup_at,self.lastlogin)
