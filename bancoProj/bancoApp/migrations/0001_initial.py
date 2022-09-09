# Generated by Django 4.1.1 on 2022-09-08 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lastChangeDate', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='bancoApp.customer')),
            ],
        ),
    ]