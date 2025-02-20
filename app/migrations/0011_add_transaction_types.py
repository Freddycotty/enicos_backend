from django.db import migrations

def add_transaction_types(apps, schema_editor):
    TransactionTypeInventory = apps.get_model('app', 'TransactionTypeInventory')
    
    transaction_types = [
        {'name': 'Entrada', 'is_active': True},
        {'name': 'Salida', 'is_active': True},
        {'name': 'Ajuste', 'is_active': True},
    ]
    
    for type_data in transaction_types:
        TransactionTypeInventory.objects.create(**type_data)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_product_id_historicalproductvalue_product_and_more'),
    ]

    operations = [
        migrations.RunPython(add_transaction_types),
    ]
