# Generated by Django 4.2.4 on 2024-04-02 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_creditcard_cvv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
