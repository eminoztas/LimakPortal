# Generated by Django 3.0.7 on 2020-06-27 19:29

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_remove_cv_deneme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='Tel',
            field=phone_field.models.PhoneField(blank=True, max_length=16),
        ),
    ]
