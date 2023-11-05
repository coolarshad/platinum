# Generated by Django 4.2.6 on 2023-10-31 19:01

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_teampage_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teampage',
            name='images',
        ),
        migrations.AddField(
            model_name='teampage',
            name='team_members',
            field=wagtail.fields.StreamField([('team_member', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(required=True)), ('designation', wagtail.blocks.CharBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))], blank=True, null=True, use_json_field=True),
        ),
    ]