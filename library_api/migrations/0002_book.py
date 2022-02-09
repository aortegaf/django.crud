# Generated by Django 4.0.2 on 2022-02-09 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('edition', models.PositiveIntegerField()),
                ('pages', models.PositiveIntegerField()),
                ('idiom', models.CharField(max_length=20)),
                ('editorial', models.CharField(max_length=100)),
                ('author', models.ManyToManyField(to='library_api.Author')),
            ],
        ),
    ]
