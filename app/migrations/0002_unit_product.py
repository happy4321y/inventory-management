# Generated by Django 4.0.6 on 2022-08-03 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('short_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('photo', models.ImageField(upload_to='product/')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.unit')),
            ],
        ),
    ]
