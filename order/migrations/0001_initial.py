# Generated by Django 3.2.6 on 2024-01-23 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('dish_marathi_name', models.CharField(default=True, max_length=100)),
                ('price', models.FloatField(default=0)),
                ('hotel_id', models.CharField(blank=True, max_length=100, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Dish_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('hotel_id', models.CharField(blank=True, max_length=100, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.CharField(blank=True, max_length=100, null=True)),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_mobile', models.IntegerField(default=True, unique=True)),
                ('pin', models.IntegerField()),
                ('department', models.CharField(default=True, max_length=50)),
                ('added_by', models.CharField(default=True, max_length=50)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('hotel_address', models.CharField(max_length=100)),
                ('mobile', models.IntegerField(unique=True)),
                ('pin', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
                ('marketing_admin_status', models.IntegerField(default=1)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marketing_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_address', models.CharField(max_length=100)),
                ('employee_mobile', models.IntegerField(default=True, unique=True)),
                ('pin', models.IntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('hotel', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_filter', models.IntegerField(default=True)),
                ('hotel', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.hotel')),
                ('table', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.table')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(default=True)),
                ('dish_marathi_name', models.CharField(default=True, max_length=100)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('ordered_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_filter', models.IntegerField(default=True)),
                ('hotel', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='NewCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_marathi_name', models.CharField(default=True, max_length=100)),
                ('table_number', models.CharField(blank=True, max_length=100, null=True)),
                ('chef_id', models.CharField(blank=True, max_length=100, null=True)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('note', models.CharField(max_length=100, null=True)),
                ('cook_status', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='pending', max_length=50)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('dish', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.dish')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.employee')),
                ('hotel', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.hotel')),
                ('table', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.table')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='marketing_employee',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.marketing_employee'),
        ),
        migrations.AddField(
            model_name='dish',
            name='dish_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.dish_category'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_marathi_name', models.CharField(default=True, max_length=100)),
                ('table_number', models.CharField(blank=True, max_length=100, null=True)),
                ('chef_id', models.CharField(blank=True, max_length=100, null=True)),
                ('qty', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0, null=True)),
                ('total_price', models.FloatField(default=0, null=True)),
                ('note', models.CharField(max_length=100, null=True)),
                ('cook_status', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Packed'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('dish', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.dish')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='order.employee')),
                ('hotel', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.hotel')),
                ('table', models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='order.table')),
            ],
        ),
    ]
