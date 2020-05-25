# Generated by Django 3.0.6 on 2020-05-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_company_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='company',
            name='location',
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.ManyToManyField(to='landing_page.Location'),
        ),
    ]
