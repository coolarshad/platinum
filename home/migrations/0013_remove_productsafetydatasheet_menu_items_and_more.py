# Generated by Django 4.2.6 on 2023-11-01 19:23

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homepage_address_homepage_email_homepage_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsafetydatasheet',
            name='menu_items',
        ),
        migrations.AddField(
            model_name='productsafetydatasheet',
            name='custom_field',
            field=wagtail.fields.StreamField([('checkbox', wagtail.blocks.BooleanBlock(help_text='Check to enable feature', required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(required=False))], blank=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='productsafetydatasheet',
            name='parent',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='home.productsafetydatasheet'),
        ),
    ]
