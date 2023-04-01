# Generated by Django 4.1.7 on 2023-03-31 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieSearch', '0002_city_dayweek_genre_state_rating_neighborhood_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genre', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='genre', to='movieSearch.genre')),
            ],
        ),
    ]