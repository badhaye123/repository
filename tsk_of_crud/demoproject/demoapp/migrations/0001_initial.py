# Generated by Django 3.2.6 on 2021-09-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laptopmodelname', models.CharField(choices=[('Asus', 'Asus'), ('Hp', 'HP'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')], max_length=30)),
                ('laptopcompanyname', models.CharField(max_length=30)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('weight', models.FloatField()),
                ('processor', models.CharField(max_length=30)),
            ],
        ),
    ]
