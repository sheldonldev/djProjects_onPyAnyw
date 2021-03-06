# Generated by Django 3.0.3 on 2020-02-23 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20200223_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.CharField(max_length=10240, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.CharField(max_length=10240, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='iso',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Region'),
        ),
    ]
