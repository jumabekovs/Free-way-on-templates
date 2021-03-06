# Generated by Django 3.1.5 on 2021-02-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('gender_segregation', models.CharField(choices=[('men', 'Only for Men '), ('women', 'Only for Women'), ('both', 'Open')], max_length=25)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, help_text='Contact phone number', max_length=14)),
                ('area', models.IntegerField()),
                ('address', models.CharField(max_length=400, unique=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='club_types', to='category.categoryclub')),
            ],
        ),
        migrations.CreateModel(
            name='ClubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, default='default_club_logo.jpg', null=True, upload_to='club_images')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club', to='club.club')),
            ],
        ),
    ]
