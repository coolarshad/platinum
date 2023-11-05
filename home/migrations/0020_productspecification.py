# Generated by Django 4.2.6 on 2023-11-01 20:00

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0019_remove_safetydatasheet_parent_safetydatasheet_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('menu_items', wagtail.fields.StreamField([('page', wagtail.blocks.PageChooserBlock(required=False)), ('file', wagtail.documents.blocks.DocumentChooserBlock(required=False))], blank=True, use_json_field=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]