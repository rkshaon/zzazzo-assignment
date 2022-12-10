# Generated by Django 3.2.16 on 2022-12-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order_custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_custom.purchase')),
            ],
        ),
    ]