# Generated by Django 2.1 on 2018-12-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default=' ', max_length=1000),
            preserve_default=False,
        ),
    ]
