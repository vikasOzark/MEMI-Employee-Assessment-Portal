# Generated by Django 4.0.2 on 2022-03-17 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assesment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quesmodel',
            name='sel_ans',
        ),
        migrations.AddField(
            model_name='quesmodel',
            name='saved_answer',
            field=models.JSONField(null=True),
        ),
    ]