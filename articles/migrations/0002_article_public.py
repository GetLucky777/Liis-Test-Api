# Generated by Django 2.2.16 on 2022-04-23 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=False, verbose_name='Область доступа к статье'),
        ),
    ]
