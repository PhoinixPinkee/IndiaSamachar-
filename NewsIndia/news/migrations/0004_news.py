# Generated by Django 4.1.5 on 2023-04-25 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=500)),
                ('newspic', models.ImageField(default='', upload_to='static/news/')),
                ('ndes', models.TextField()),
                ('cdate', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.city')),
            ],
        ),
    ]