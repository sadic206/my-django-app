# Generated by Django 3.1.1 on 2020-10-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=20)),
                ('msg', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to=None)),
            ],
            options={
                'db_table': 'mail',
            },
        ),
    ]
