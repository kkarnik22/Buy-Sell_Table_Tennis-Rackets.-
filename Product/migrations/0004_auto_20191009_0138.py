# Generated by Django 2.2.5 on 2019-10-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0003_racket_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racket',
            name='model_no',
            field=models.TextField(),
        ),
    ]
