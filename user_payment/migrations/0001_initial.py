# Generated by Django 4.2.2 on 2023-08-19 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0002_alter_customer_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_bool', models.BooleanField(default=False)),
                ('stripe_checkout_id', models.CharField(max_length=500)),
                ('Customer_ID', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
