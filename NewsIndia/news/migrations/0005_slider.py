# Generated by Django 4.1.5 on 2023-04-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shead', models.CharField(max_length=300)),
                ('ssubject', models.CharField(max_length=300)),
                ('sdes', models.TextField()),
                ('spic', models.ImageField(default='', upload_to='static/slider/')),
            ],
        ),
    ]
