# Generated by Django 4.0.2 on 2022-04-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assesment', '0007_remove_quesmodel_ans_quesmodel_para_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesmodel',
            name='ans',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]