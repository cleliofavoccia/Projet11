# Generated by Django 3.1.5 on 2021-02-12 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_product', to='products.product')),
                ('substitute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites_as_substitute', to='products.product')),
            ],
        ),
    ]