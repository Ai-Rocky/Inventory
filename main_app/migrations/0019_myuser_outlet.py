# Generated by Django 3.0.4 on 2020-07-06 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='Outlet',
            field=models.ForeignKey(default=45, on_delete=django.db.models.deletion.CASCADE, to='main_app.Outlet'),
        ),
    ]