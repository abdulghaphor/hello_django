# Generated by Django 2.2.5 on 2019-09-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20190921_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('P', 'Payment Successful'), ('S', 'Shipped'), ('Z', 'Complete'), ('0', 'Inactive'), ('F', 'Payment Failed')], default='A', max_length=1),
        ),
    ]
