# Generated by Django 3.2.3 on 2021-06-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spinner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StopWords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_words', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Spinner',
        ),
    ]
