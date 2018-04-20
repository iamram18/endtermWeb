# Generated by Django 2.0.3 on 2018-04-20 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
