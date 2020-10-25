# Generated by Django 3.1.2 on 2020-10-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chef', models.CharField(max_length=50)),
                ('menu', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
