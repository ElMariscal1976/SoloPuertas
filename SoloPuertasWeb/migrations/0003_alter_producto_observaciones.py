# Generated by Django 5.1 on 2024-08-27 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SoloPuertasWeb', '0002_alter_producto_clasificacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='observaciones',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
