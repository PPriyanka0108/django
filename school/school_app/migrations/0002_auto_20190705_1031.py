# Generated by Django 2.2.3 on 2019-07-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='roll_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='sub',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]