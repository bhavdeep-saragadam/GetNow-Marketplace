# Generated by Django 4.0.6 on 2024-02-04 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_customuser_alter_comment_user_alter_product_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.customuser'),
        ),
    ]
