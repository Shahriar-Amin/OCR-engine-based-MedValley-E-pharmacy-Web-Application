# Generated by Django 4.2.2 on 2023-10-22 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, null=True)),
                ('blog_title', models.CharField(max_length=200, null=True)),
                ('user_image', models.ImageField(default=None, null=True, upload_to='uploads/blogs')),
                ('date', models.DateField(null=True)),
                ('writing', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('item_price', models.CharField(max_length=100, null=True)),
                ('total', models.FloatField(null=True)),
                ('cart_session', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(null=True)),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('total', models.FloatField(null=True)),
                ('gateway', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_number', models.CharField(max_length=255, null=True)),
                ('phone_number', models.CharField(max_length=255, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField(null=True)),
                ('customer_name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gateway', models.CharField(max_length=100, null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.order')),
            ],
        ),
        migrations.CreateModel(
            name='Blog_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('user_name', models.CharField(max_length=100, null=True)),
                ('comment', models.TextField(null=True)),
                ('comment_date', models.DateField(null=True)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.blogpost')),
            ],
        ),
    ]
