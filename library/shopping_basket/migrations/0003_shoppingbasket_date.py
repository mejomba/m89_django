# Generated by Django 4.2 on 2023-04-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingbasket',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]