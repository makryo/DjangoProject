# Generated by Django 2.1.1 on 2018-11-24 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', default='DEFAULT VALUE')),
                ('Codigo', models.CharField(max_length=45)),
                ('Nombre1', models.CharField(max_length=45)),
                ('Nombre2', models.CharField(max_length=45)),
                ('ApellidoP', models.CharField(max_length=45)),
                ('ApellidoM', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID', default='DEFAULT VALUE')),
                ('Nombre', models.CharField(max_length=45)),
                ('Creditos', models.PositiveIntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('FechaMatricula', models.DateTimeField(auto_now_add=True)),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Montessori.Alumno')),
                ('Curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Montessori.Curso', default='DEFAULT VALUE')),
            ],
        ),
    ]