# Generated by Django 4.2.6 on 2023-11-01 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_teampage_images_teampage_team_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
