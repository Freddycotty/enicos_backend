# Generated by Django 5.1.6 on 2025-02-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_add_transaction_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiontypeinventory',
            name='name',
            field=models.CharField(help_text='Tipo de transacción', max_length=50, verbose_name='Tipo de transacción'),
        ),
    ]
