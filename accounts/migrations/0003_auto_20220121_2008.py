# Generated by Django 3.2.9 on 2022-01-21 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220121_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='currrent_ctc',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='currrent_employer',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='currrent_loc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='expected_ctc',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='graduation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='notice_per',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='other_qual',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='pos_applied_for',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='post_graduation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Assesment/static/media'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reson_for_leaving',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tenth_percent',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='twelfth_percent',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='assesment_taken',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
