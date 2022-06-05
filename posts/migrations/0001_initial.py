# Generated by Django 4.0.4 on 2022-06-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('post_id', models.IntegerField()),
                ('categoriya', models.TextField(choices=[('Dj', 'Django'), ('Py', 'Python')], max_length=255)),
                ('start_sanasi', models.DateTimeField(auto_now_add=True)),
                ('ozgartirilgan_sanasi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
