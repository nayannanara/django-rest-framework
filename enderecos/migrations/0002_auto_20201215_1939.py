# Generated by Django 3.1.4 on 2020-12-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='linha2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='linha1',
            field=models.CharField(max_length=150),
        ),
    ]
