# Generated by Django 5.0.3 on 2024-04-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='bcontent',
            field=models.CharField(max_length=2500, null=True),
        ),
    ]
