# Generated by Django 3.2.9 on 2022-01-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='userform_filled',
            field=models.BooleanField(default=False),
        ),
    ]