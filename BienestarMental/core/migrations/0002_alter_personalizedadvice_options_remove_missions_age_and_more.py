# Generated by Django 4.2.5 on 2023-09-14 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalizedadvice',
            options={'ordering': ['id'], 'verbose_name': 'Asesoria', 'verbose_name_plural': 'Asesorias'},
        ),
        migrations.RemoveField(
            model_name='missions',
            name='age',
        ),
        migrations.AlterField(
            model_name='missions',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Nombre Mision'),
        ),
        migrations.AlterField(
            model_name='missions',
            name='numberMission',
            field=models.PositiveIntegerField(verbose_name='Numero Misiones'),
        ),
        migrations.AlterField(
            model_name='missions',
            name='objetive',
            field=models.CharField(max_length=250, verbose_name='Objetivo Mision'),
        ),
        migrations.AlterField(
            model_name='missions',
            name='result',
            field=models.CharField(max_length=250, verbose_name='Resultado Mision'),
        ),
        migrations.AlterField(
            model_name='missions',
            name='typeMission',
            field=models.CharField(max_length=250, verbose_name='Tipo Mision'),
        ),
        migrations.AlterField(
            model_name='personalizedadvice',
            name='historialAdvice',
            field=models.CharField(max_length=250, verbose_name='Historial Asesorias'),
        ),
        migrations.AlterField(
            model_name='personalizedadvice',
            name='missions',
            field=models.ManyToManyField(to='core.missions', verbose_name='Asesoramiento Misión'),
        ),
        migrations.AlterField(
            model_name='personalizedadvice',
            name='topic',
            field=models.CharField(max_length=250, verbose_name='Tema Asesoria'),
        ),
        migrations.AlterField(
            model_name='personalizedadvice',
            name='typeAdvice',
            field=models.CharField(max_length=250, verbose_name='Tipo Asesoria'),
        ),
    ]
