# Generated by Django 3.0.2 on 2020-02-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_auto_20200210_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='emailId',
            field=models.EmailField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='name',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='subject',
            field=models.CharField(max_length=5000),
        ),
    ]
