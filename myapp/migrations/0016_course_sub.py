# Generated by Django 4.2.20 on 2025-04-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_resultmodel_result_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sub',
            field=models.ManyToManyField(related_name='subject', to='myapp.subject'),
        ),
    ]
