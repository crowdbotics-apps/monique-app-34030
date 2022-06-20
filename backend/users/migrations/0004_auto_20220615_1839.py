# Generated by Django 2.2.26 on 2022-06-15 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_datalist'),
    ]

    operations = [
        migrations.AddField(
            model_name='datalist',
            name='date_end',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Date End'),
        ),
        migrations.AddField(
            model_name='datalist',
            name='date_start',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Date Start'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='subject_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Subject ID'),
        ),
    ]
