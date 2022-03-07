# Generated by Django 4.0.3 on 2022-03-06 20:13

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='key_issue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comic',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='comic',
            name='own',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comic',
            name='own_slabbed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comic',
            name='slab_grade',
            field=models.DecimalField(choices=[(Decimal('0.5'), '0.5'), (Decimal('1.0'), '1.0'), (Decimal('1.5'), '1.5'), (Decimal('1.8'), '1.8'), (Decimal('2.0'), '2.0'), (Decimal('2.5'), '2.5'), (Decimal('3.0'), '3.0'), (Decimal('3.5'), '3.5'), (Decimal('4.0'), '4.0'), (Decimal('4.5'), '4.5'), (Decimal('5.0'), '5.0'), (Decimal('5.5'), '5.5'), (Decimal('6.0'), '6.0'), (Decimal('6.5'), '6.5'), (Decimal('7.0'), '7.0'), (Decimal('7.5'), '7.5'), (Decimal('8.0'), '8.0'), (Decimal('8.5'), '8.5'), (Decimal('9.0'), '9.0'), (Decimal('9.2'), '9.2'), (Decimal('9.4'), '9.4'), (Decimal('9.6'), '9.6'), (Decimal('9.8'), '9.8'), (Decimal('9.9'), '9.9'), (Decimal('10'), '10')], decimal_places=1, max_digits=2, null=True),
        ),
    ]
