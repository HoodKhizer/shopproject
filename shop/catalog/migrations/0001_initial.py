# Generated by Django 3.1 on 2021-03-09 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LU_Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.lu_status')),
            ],
        ),
    ]
