# Generated by Django 4.2.5 on 2023-09-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_articles_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='publishedAt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='source',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='articles',
            name='urlToImage',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
