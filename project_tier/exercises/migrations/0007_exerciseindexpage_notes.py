# Generated by Django 2.0.4 on 2018-08-20 23:05

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20180424_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseindexpage',
            name='notes',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='A brief note to help the readers'),
        ),
    ]