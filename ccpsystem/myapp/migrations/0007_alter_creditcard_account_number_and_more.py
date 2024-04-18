# Generated by Django 4.2.4 on 2024-04-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_creditcard_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='account_number',
            field=models.CharField(max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='expiration_date',
            field=models.CharField(max_length=10),
        ),
    ]
