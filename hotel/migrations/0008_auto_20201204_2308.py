# Generated by Django 3.1.3 on 2020-12-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='num_person',
            field=models.CharField(choices=[('1', 'single'), ('2', 'double'), ('family', 'family')], max_length=50),
        ),
    ]
