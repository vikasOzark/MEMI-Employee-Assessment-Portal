# Generated by Django 4.0.2 on 2022-04-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_customuser_assesment_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='time_taken',
            field=models.TimeField(null=True),
        ),
    ]