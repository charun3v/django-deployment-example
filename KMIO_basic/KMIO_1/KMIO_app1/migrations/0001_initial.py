# Generated by Django 3.0.5 on 2020-04-21 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mr_No', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='KMIO_app1.PatientID')),
            ],
        ),
        migrations.CreateModel(
            name='PatientAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='KMIO_app1.PatientID')),
            ],
        ),
    ]