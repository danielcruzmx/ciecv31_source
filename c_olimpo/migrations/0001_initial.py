# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-18 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('debe', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('haber', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('a_favor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_auxiliar_proveedor_id', to='main.Proveedore')),
            ],
            options={
                'ordering': ['fecha'],
                'managed': True,
                'db_table': 'olimpo_asiento',
            },
        ),
        migrations.CreateModel(
            name='Condomino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depto', models.CharField(blank=True, max_length=15, null=True)),
                ('propietario', models.CharField(blank=True, max_length=60, null=True)),
                ('poseedor', models.CharField(blank=True, max_length=60, null=True)),
                ('ubicacion', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=25, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_escrituracion', models.DateField(blank=True, null=True)),
                ('referencia', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_condomino_condominio_id', to='main.Condominio')),
            ],
            options={
                'ordering': ['depto'],
                'managed': True,
                'db_table': 'olimpo_condomino',
            },
        ),
        migrations.CreateModel(
            name='CuentaBanco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.CharField(max_length=20)),
                ('clabe', models.CharField(max_length=18)),
                ('apoderado', models.CharField(max_length=60)),
                ('saldo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_saldo', models.DateField(blank=True, null=True)),
                ('situacion', models.IntegerField(blank=True, null=True)),
                ('tipo_cuenta', models.CharField(max_length=20)),
                ('banco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Banco')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Condominio')),
            ],
            options={
                'db_table': 'olimpo_cuenta_banco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleMovimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, default='.', max_length=250, null=True)),
                ('monto', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('cuenta_contable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CuentaContable', verbose_name='Cuenta Contable Ingreso/Egreso')),
            ],
            options={
                'ordering': ['movimiento'],
                'managed': True,
                'db_table': 'olimpo_detalle_movimiento',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.IntegerField()),
                ('fecha_expedicion', models.DateField()),
                ('monto_total', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('notas', models.CharField(blank=True, max_length=45, null=True)),
                ('situacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_recibo_situacion_id', to='main.Situacion')),
                ('tipo_documento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_recibo_tipodoc_id', to='main.TipoDocumento')),
            ],
            options={
                'db_table': 'olimpo_documento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'olimpo_estacionamiento',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('retiro', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('deposito', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True)),
                ('condomino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_movimiento_condomino_id', to='c_olimpo.Condomino')),
                ('cuenta_banco', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_movimiento_cuenta_id', to='c_olimpo.CuentaBanco')),
                ('documento', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_movimiento_documento_id', to='c_olimpo.Documento')),
                ('tipo_movimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_movimiento_tipo_movimiento_id', to='main.TipoMovimiento')),
            ],
            options={
                'ordering': ['fecha'],
                'managed': True,
                'db_table': 'olimpo_movimiento',
            },
        ),
        migrations.AddField(
            model_name='detallemovimiento',
            name='movimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='c_olimpo.Movimiento', verbose_name='Movto'),
        ),
        migrations.AddField(
            model_name='detallemovimiento',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Proveedore', verbose_name='Proveedor'),
        ),
        migrations.AddField(
            model_name='condomino',
            name='estacionamiento',
            field=models.ManyToManyField(related_name='olimpo_condomino_estacionamiento_id', to='c_olimpo.Estacionamiento'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='condomino',
            field=models.ForeignKey(default=67, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_auxiliar_condomino_id', to='c_olimpo.Condomino'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='cuenta_contable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.CuentaContable', verbose_name='Cuenta Contable'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='tipo_movimiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='olimpo_auxiliar_tipo_movimiento_id', to='main.TipoMovimiento'),
        ),
    ]