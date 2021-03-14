# Generated by Django 3.1.7 on 2021-03-13 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210314_0127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), (
                    'Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=50, null=True)),
                ('date_created', models.DateTimeField(
                    auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[
                 ('Indoor', 'Indoor'), ('Outdoor', 'Outdoor')], max_length=100, null=True)),
                ('description', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(
                    auto_now_add=True, null=True)),
            ],
        ),
    ]