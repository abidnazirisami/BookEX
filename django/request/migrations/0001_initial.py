# Generated by Django 2.0.3 on 2018-04-17 16:35

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
            name='Wishlist',
            fields=[
                ('id', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('isbn', models.CharField(default='Not available', max_length=50)),
                ('author_name', models.CharField(default='Not available', max_length=500)),
                ('edition', models.IntegerField(default=1)),
                ('count', models.IntegerField(default=1)),
                ('book_name', models.CharField(default='Not available', max_length=100)),
                ('isAvailable', models.BooleanField(default=False)),
                ('hasReceived', models.BooleanField(default=False)),
                ('isEmergency', models.BooleanField(default=False)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(default='Not available', on_delete=django.db.models.deletion.DO_NOTHING, related_name='request_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
