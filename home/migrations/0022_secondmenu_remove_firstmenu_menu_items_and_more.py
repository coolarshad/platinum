# Generated by Django 4.2.6 on 2023-11-01 20:34

from django.db import migrations, models
import django.db.models.deletion
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0021_firstmenu_delete_safetydatasheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondMenu',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('file_upload', wagtail.fields.StreamField([('file', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a file', required=False))], blank=True, null=True, use_json_field=True)),
                ('enable_feature', models.BooleanField(default=False, help_text='Check to enable the feature')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='firstmenu',
            name='menu_items',
        ),
        migrations.RemoveField(
            model_name='productspecification',
            name='menu_items',
        ),
        migrations.AddField(
            model_name='firstmenu',
            name='enable_feature',
            field=models.BooleanField(default=False, help_text='Check to enable the feature'),
        ),
        migrations.AddField(
            model_name='firstmenu',
            name='file_upload',
            field=wagtail.fields.StreamField([('file', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a file', required=False))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='enable_feature',
            field=models.BooleanField(default=False, help_text='Check to enable the feature'),
        ),
        migrations.AddField(
            model_name='productspecification',
            name='file_upload',
            field=wagtail.fields.StreamField([('file', wagtail.documents.blocks.DocumentChooserBlock(help_text='Upload a file', required=False))], blank=True, null=True, use_json_field=True),
        ),
    ]
