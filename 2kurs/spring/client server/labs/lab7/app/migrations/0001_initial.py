# Generated by Django 5.0.3 on 2024-03-10 04:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('wname', models.CharField(max_length=50)),

                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.branch')),
            ],
        ),
    ]
