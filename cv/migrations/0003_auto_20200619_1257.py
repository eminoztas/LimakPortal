# Generated by Django 3.0.7 on 2020-06-19 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20200618_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='personeImage',
            new_name='personelImage',
        ),
        migrations.RemoveField(
            model_name='cv',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='personnel',
            name='cv',
        ),
        migrations.AddField(
            model_name='cv',
            name='personnel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cv.Personnel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personnel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='cv.Personnel'),
        ),
    ]