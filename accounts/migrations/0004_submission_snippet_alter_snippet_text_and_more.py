# Generated by Django 5.0.2 on 2024-02-18 14:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_snippet_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='snippet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.snippet'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]