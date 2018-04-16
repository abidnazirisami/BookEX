# Generated by Django 2.0.3 on 2018-04-16 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('author_name', models.CharField(default='Not available', max_length=100)),
                ('wiki_link', models.CharField(default='Not available', max_length=500)),
                ('rating', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Boiii',
            fields=[
                ('book_id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('condition', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(default='Not available', max_length=50, primary_key=True, serialize=False)),
                ('topic_name', models.CharField(default='Not available', max_length=100)),
                ('publish_year', models.IntegerField(default=1996)),
                ('publisher', models.CharField(default='Not available', max_length=100)),
                ('amazon_link', models.CharField(default='Not available', max_length=500)),
                ('edition', models.IntegerField(default=1)),
                ('pages', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('book_name', models.CharField(default='Not available', max_length=100)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Author')),
            ],
        ),
        migrations.CreateModel(
            name='OurUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='Not available', max_length=100)),
                ('batch', models.IntegerField(default=21)),
                ('roll', models.IntegerField(default=26)),
                ('mail_id', models.CharField(default='Not available', max_length=100)),
                ('donate_count', models.IntegerField(default=0)),
                ('phone', models.CharField(default='Not available', max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='boiii',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.OurUser'),
        ),
        migrations.AddField(
            model_name='boiii',
            name='isbn',
            field=models.ForeignKey(default='Not available', on_delete=django.db.models.deletion.CASCADE, to='pages.Book'),
        ),
    ]
