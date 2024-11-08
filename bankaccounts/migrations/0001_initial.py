# Generated by Django 5.1.3 on 2024-11-06 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=30)),
                ('balance', models.FloatField(default=500)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
