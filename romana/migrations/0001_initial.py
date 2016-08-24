# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chofer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ci', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('placa_vehiculo', models.CharField(max_length=20)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(max_length=200, blank=True)),
                ('activo', models.BooleanField(default=b'true')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rif', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(max_length=200, blank=True)),
                ('activo', models.BooleanField(default=b'true')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='romana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hora_entrada', models.DateTimeField(null=True)),
                ('hora_salida', models.DateTimeField(null=True)),
                ('guia', models.CharField(max_length=50)),
                ('peso_tara', models.FloatField(default=0)),
                ('peso_neto', models.FloatField(default=0)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('observacion', models.TextField(max_length=200, blank=True)),
                ('activo', models.BooleanField(default=b'true')),
                ('chofer', models.ForeignKey(to='romana.chofer')),
                ('empresa', models.ForeignKey(to='romana.empresa')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
