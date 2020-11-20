# Generated by Django 3.0.8 on 2020-10-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20201003_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='benifits',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='climate',
            field=models.CharField(blank=True, default='', max_length=900),
        ),
        migrations.AlterField(
            model_name='product',
            name='growingperiod',
            field=models.CharField(blank=True, default='', max_length=900),
        ),
        migrations.AlterField(
            model_name='product',
            name='healthbenifits',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='product',
            name='p_area',
            field=models.CharField(blank=True, default='', max_length=900),
        ),
        migrations.AlterField(
            model_name='product',
            name='soilfertility',
            field=models.CharField(blank=True, default='', max_length=900),
        ),
    ]