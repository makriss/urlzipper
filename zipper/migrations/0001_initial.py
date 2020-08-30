# Generated by Django 3.1 on 2020-08-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlMapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashcode', models.CharField(max_length=10, unique=True)),
                ('url', models.TextField(unique=True)),
                ('clicks', models.IntegerField(default=0)),
                ('url_shorten_count', models.IntegerField(default=1)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
