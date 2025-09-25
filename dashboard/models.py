from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.SmallAutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.BinaryField()  # karena di DB: bytea
    token = models.CharField(max_length=40, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    last_password_change = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    secret_key = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'admin'
        managed = False  # penting agar Django tidak migrasi tabel ini

    def __str__(self):
        return self.username
    
class Company_group(models.Model):
    id = models.SmallAutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    phone = models.CharField(max_length=20,blank=True, null=True)
    code = models.CharField(max_length=8,blank=True,null=True)

    class Meta:
        db_table = 'account_group'
        managed = False  # ⬅️ penting!

    def __str__(self):
        return self.username
