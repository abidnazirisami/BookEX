# Generated by Django 2.0.3 on 2018-04-08 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boiii',
            name='book_id',
            field=models.AutoField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
