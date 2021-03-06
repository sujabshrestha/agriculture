# Generated by Django 3.0.8 on 2020-09-20 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20200920_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancellation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.IntegerField()),
                ('product_quantity', models.CharField(max_length=255)),
            ],
        ),
    ]
