# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-18 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=3)),
                ('descripcion', models.CharField(blank=True, max_length=25, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'banco',
            },
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('calle', models.CharField(blank=True, max_length=45, null=True)),
                ('colonia', models.CharField(blank=True, max_length=45, null=True)),
                ('delegacion', models.CharField(blank=True, max_length=45, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=45, null=True)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
                ('cp', models.CharField(blank=True, max_length=5, null=True)),
                ('regimen', models.CharField(blank=True, max_length=45, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('fecha_constitucion', models.DateField(blank=True, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'condominio',
            },
        ),
        migrations.CreateModel(
            name='CuentaContable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cuenta', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('clave_mayor', models.CharField(max_length=4)),
            ],
            options={
                'managed': True,
                'db_table': 'cuenta_contable',
                'ordering': ['num_cuenta'],
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicial', models.DateField(blank=True, null=True)),
                ('fecha_final', models.DateField(blank=True, null=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Condominio')),
            ],
            options={
                'managed': True,
                'db_table': 'periodo',
            },
        ),
        migrations.CreateModel(
            name='Proveedore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=60)),
                ('domicilio', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=30, null=True)),
                ('rfc', models.CharField(blank=True, max_length=13, null=True)),
                ('clabe', models.CharField(default='0', max_length=18, null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'proveedore',
            },
        ),
        migrations.CreateModel(
            name='Situacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacion', models.CharField(max_length=25)),
            ],
            options={
                'managed': True,
                'db_table': 'situacion',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
            ],
            options={
                'managed': True,
                'db_table': 'tipo_documento',
            },
        ),
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=25)),
            ],
            options={
                'managed': True,
                'db_table': 'tipo_movimiento',
            },
        ),
    ]
