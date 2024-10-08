# Generated by Django 5.1.1 on 2024-09-21 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LigneTrajet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='stops.stop')),
            ],
        ),
    ]
