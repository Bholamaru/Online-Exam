# Generated by Django 5.1.7 on 2025-03-30 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_papermodel_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='myapp.course'),
            preserve_default=False,
        ),
    ]
