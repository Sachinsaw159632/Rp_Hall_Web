# Generated by Django 2.1.2 on 2018-10-31 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]
