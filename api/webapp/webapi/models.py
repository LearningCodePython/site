from django.db import models

# Create your models here.

class sitios(models.Model):
    nombre = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    api_password = models.CharField(max_length=50)
    api_user = models.CharField(max_length=50)

    def __str__(self):
    	fila = self.nombre
    	return fila

class vpn_data(models.Model):
    cliente = models.CharField(max_length=50)
    uso = models.CharField(max_length=50)
    modelo = models.CharField (max_length=50)
    tipo = models.CharField (max_length=50)
    nombre_vpn1 = models.CharField (max_length=50)
    pass1 = models.CharField (max_length=50)
    ip_gestion = models.CharField (max_length=15)
    red = models.CharField (max_length=15)
    ip_vpn_local = models.CharField (max_length=15)
    ip_vpn_remoto = models.CharField (max_length=15)
    ip_wan1 = models.CharField (max_length=15)
    proveedor = models.CharField (max_length=50)
    nombre_vpn2 = models.CharField (max_length=50)
    pass2 = models.CharField (max_length=50)
    red_vpn_bk = models.CharField (max_length=15)
    ip_vpn_bk_local = models.CharField (max_length=15)
    ip_vpn_bk_remoto = models.CharField (max_length=15)
    ip_wan2 = models.CharField (max_length=15)
    proveedor_bk = models.CharField (max_length=50)
    columna6 = models.CharField (max_length=50)
    pass_ipsec = models.CharField (max_length=50)
    area_ospf = models.IntegerField (max_length=3)
    loopbak_local = models.CharField (max_length=15)
    loopbak_remoto = models.CharField (max_length=15)