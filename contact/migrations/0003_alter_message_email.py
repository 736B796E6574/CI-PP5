# Generated by Django 4.1.1 on 2022-12-01 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_message_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.CharField(max_length=254),
        ),
    ]
