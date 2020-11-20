# Generated by Django 3.0.8 on 2020-07-29 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200720_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=255)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('customer_contact', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_id', models.IntegerField()),
                ('product_quantity', models.CharField(max_length=255)),
                ('subtotal', models.IntegerField()),
                ('delivery_charge', models.IntegerField()),
                ('total_amount', models.IntegerField()),
            ],
        ),
    ]