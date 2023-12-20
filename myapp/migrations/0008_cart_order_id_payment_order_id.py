# Generated by Django 4.2.2 on 2023-11-03 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_contact_message_message_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order'),
        ),
        migrations.AddField(
            model_name='payment',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order'),
        ),
    ]