# Generated by Django 3.1 on 2021-09-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('priceM', models.DecimalField(decimal_places=2, max_digits=8)),
                ('priceL', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bImage', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='pizza',
            name='priceL',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='priceM',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
