# Generated by Django 3.1.5 on 2021-02-10 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubimage',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='club.club'),
        ),
    ]
