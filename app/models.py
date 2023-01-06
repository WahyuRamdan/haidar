from django.db import models

class Maps(models.Model):
    club = models.CharField(max_length=200, null=True, blank=True)
    lokasi = models.CharField(max_length=200, null=True, blank=True)

class Crud(models.Model):
    club = models.CharField(max_length=200, null=True, blank=True)
    nama_pemain = models.CharField(max_length=200, null=True, blank=True)
    tahun_join = models.CharField(max_length=200, null=True, blank=True)
