# Generated by Django 3.1.7 on 2021-03-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(
                    auto_now_add=True, null=True)),
            ],
        ),
    ]
