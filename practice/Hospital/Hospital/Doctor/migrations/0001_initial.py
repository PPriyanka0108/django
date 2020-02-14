# Generated by Django 2.2.3 on 2019-08-28 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=50)),
                ('doc_specialization', models.CharField(max_length=50)),
                ('doc_qualification', models.CharField(max_length=20)),
            ],
        ),
    ]