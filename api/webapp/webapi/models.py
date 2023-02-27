from django.db import models

# Create your models here.

class sitios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='nombre',null=True)
    host = models.CharField(max_length=50, verbose_name='host', null=False)
    api_password = models.CharField(max_length=50, verbose_name="api_password", null=False)
    api_user = models.CharField(max_length=50, verbose_name='api_user', null=False)

    def __str__(self):
    	fila = "Nombre: " + self.nombre
    	return fila

class vpn_data(models.Model):
    cliente = models.CharField(max_length=50, null=False)
    uso = models.CharField(max_length=50, null=True)
    modelo = models.CharField (max_length=50, null=True)
    tipo = models.CharField (max_length=50, null=True)
    nombre_vpn1 = models.CharField (max_length=50, null=False)
    pass1 = models.CharField (max_length=50, null=False)
    ip_gestion = models.CharField (max_length=15, null=False)
    red = models.CharField (max_length=15, null=True)
    ip_vpn_local = models.CharField (max_length=15, null=True)
    ip_vpn_remoto = models.CharField (max_length=15, null=True)
    ip_wan1 = models.CharField (max_length=15, null=True)
    proveedor = models.CharField (max_length=50, null=True)
    nombre_vpn2 = models.CharField (max_length=50, null=True)
    pass2 = models.CharField (max_length=50, null=True)
    red_vpn_bk = models.CharField (max_length=15, null=True)
    ip_vpn_bk_local = models.CharField (max_length=15, null=True)
    ip_vpn_bk_remoto = models.CharField (max_length=15, null=True)
    ip_wan2 = models.CharField (max_length=15, null=True)
    proveedor_bk = models.CharField (max_length=50, null=True)
    columna6 = models.CharField (max_length=50, null=True)
    pass_ipsec = models.CharField (max_length=50, null=True)
    area_ospf = models.IntegerField (null=True)
    loopbak_local = models.CharField (max_length=15, null=True)
    loopbak_remoto = models.CharField (max_length=15, null=True)

    def __str__(self):
        fila = "Cliente: " + self.cliente + "; " + "Uso: " + self.uso
        return fila