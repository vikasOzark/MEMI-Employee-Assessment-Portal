# Generated by Django 4.0.2 on 2022-02-17 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customuser_graduation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='comment',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
