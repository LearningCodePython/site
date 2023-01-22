# Generated by Django 4.1.5 on 2023-01-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vpn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('uso', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('nombre_vpn1', models.CharField(max_length=50)),
                ('pass1', models.CharField(max_length=50)),
                ('ip_gestion', models.CharField(max_length=15)),
                ('red', models.CharField(max_length=15)),
                ('ip_vpn_local', models.CharField(max_length=15)),
                ('ip_vpn_remoto', models.CharField(max_length=15)),
                ('ip_wan1', models.CharField(max_length=15)),
                ('proveedor', models.CharField(max_length=50)),
                ('nombre_vpn2', models.CharField(max_length=50)),
                ('pass2', models.CharField(max_length=50)),
                ('red_vpn_bk', models.CharField(max_length=15)),
                ('ip_vpn_bk_local', models.CharField(max_length=15)),
                ('ip_vpn_bk_remoto', models.CharField(max_length=15)),
                ('ip_wan2', models.CharField(max_length=15)),
                ('proveedor_bk', models.CharField(max_length=50)),
                ('columna6', models.CharField(max_length=50)),
                ('pass_ipsec', models.CharField(max_length=50)),
                ('area_ospf', models.CharField(max_length=3)),
                ('loopbak_local', models.CharField(max_length=15)),
                ('loopbak_remoto', models.CharField(max_length=15)),
            ],
        ),
    ]
