# Generated by Django 4.0 on 2021-12-25 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tshirtapp', '0003_alter_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='tshirt',
            name='tshirtid',
            field=models.CharField(default='T1', max_length=64),
        ),
    ]