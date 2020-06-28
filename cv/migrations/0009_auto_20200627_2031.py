# Generated by Django 3.0.7 on 2020-06-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_auto_20200621_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='status',
            new_name='EducationalLevel',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='name',
            new_name='FirstName',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='surname',
            new_name='LastName',
        ),
        migrations.RenameField(
            model_name='cv',
            old_name='description',
            new_name='Summary',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='ozet',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='telefon',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='title',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='update_time',
        ),
        migrations.AddField(
            model_name='cv',
            name='Adress',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='cv',
            name='DateOfBirth',
            field=models.DateField(blank=True, default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='Tel',
            field=models.TextField(blank=True, max_length=16),
        ),
    ]