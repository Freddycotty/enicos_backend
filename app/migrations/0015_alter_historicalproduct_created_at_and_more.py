# Generated by Django 5.1.6 on 2025-02-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_historicalinventory_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='created_at',
            field=models.DateTimeField(blank=True, editable=False, help_text='Fecha de creación del objeto', null=True),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='updated_at',
            field=models.DateTimeField(blank=True, editable=False, help_text='Fecha de actualización del objeto', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, help_text='Fecha de creación del objeto', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, help_text='Fecha de actualización del objeto', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('name', 'subcategory')},
        ),
    ]
