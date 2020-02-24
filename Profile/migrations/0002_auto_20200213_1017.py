# Generated by Django 2.2.1 on 2020-02-13 16:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='modeloCiudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='modeloEstado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='modeloEstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'EstadoCivil',
            },
        ),
        migrations.CreateModel(
            name='modeloGenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Genero',
            },
        ),
        migrations.CreateModel(
            name='modeloOcupacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=254)),
                ('delete', models.BooleanField(default=False)),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Ocupacion',
            },
        ),
        migrations.AlterField(
            model_name='modeloprofile',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.modeloCiudad'),
        ),
        migrations.AlterField(
            model_name='modeloprofile',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.modeloEstado'),
        ),
        migrations.AlterField(
            model_name='modeloprofile',
            name='estadoCivil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.modeloEstadoCivil'),
        ),
        migrations.AlterField(
            model_name='modeloprofile',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.modeloGenero'),
        ),
        migrations.AlterField(
            model_name='modeloprofile',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.modeloOcupacion'),
        ),
    ]
