# Generated by Django 4.2.4 on 2023-08-17 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextSnippet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('secret_key', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
