# Generated by Django 3.1.5 on 2021-02-10 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendpost',
            name='header',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='extendpost',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='post.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='post_category', to='category.categorypost'),
        ),
    ]