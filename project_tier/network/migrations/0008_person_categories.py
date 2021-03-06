# Generated by Django 2.1.8 on 2019-05-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_personcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='categories',
            field=models.ManyToManyField(blank=True, to='network.PersonCategory'),
        ),
        migrations.AddField(
            model_name='personcategory',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
