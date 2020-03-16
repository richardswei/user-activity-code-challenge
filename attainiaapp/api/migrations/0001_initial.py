# Generated by Django 3.0.4 on 2020-03-16 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('login_count', models.IntegerField()),
                ('project_count', models.IntegerField()),
                ('last_login', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]