# Generated by Django 3.2.3 on 2021-06-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spinner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.TextField()),
                ('stop_words', models.CharField(max_length=50)),
            ],
        ),
    ]
