# Generated by Django 5.0.2 on 2024-02-18 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_snippet_options_snippet_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
