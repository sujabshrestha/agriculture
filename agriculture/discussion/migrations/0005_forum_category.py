# Generated by Django 3.0.8 on 2020-09-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion', '0004_discussion_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='category',
            field=models.CharField(choices=[('vegetable seeds', 'vegetable seeds'), ('fertilizers', 'fertilizers')], default='', max_length=255),
        ),
    ]
