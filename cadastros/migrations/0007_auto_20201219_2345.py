# Generated by Django 3.1.4 on 2020-12-20 02:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_pcvaga_data_criacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='pccandidato',
            name='data_criacao',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='pccandidatura',
            name='data_criacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
