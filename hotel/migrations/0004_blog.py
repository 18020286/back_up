# Generated by Django 3.1.3 on 2020-11-29 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20201122_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=1000)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('picture', models.ImageField(upload_to='other')),
                ('content', models.TextField()),
                ('author', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
