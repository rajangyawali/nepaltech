# Generated by Django 2.2 on 2020-04-04 04:03

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
            name='AllNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=500)),
                ('author', models.CharField(default='Nepal Tech', max_length=50)),
                ('posted', models.CharField(default='April 04, 2020', max_length=20)),
                ('scrapped', models.DateTimeField(auto_now_add=True, verbose_name='Scrapped On')),
            ],
            options={
                'verbose_name_plural': 'All News',
                'ordering': ['scrapped'],
            },
        ),
        migrations.CreateModel(
            name='GadgetNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=500)),
                ('author', models.CharField(default='Nepal Tech', max_length=50)),
                ('posted', models.CharField(default='April 04, 2020', max_length=20)),
                ('scrapped', models.DateTimeField(auto_now_add=True, verbose_name='Scrapped On')),
            ],
            options={
                'verbose_name_plural': 'Gadget News',
                'ordering': ['scrapped'],
            },
        ),
        migrations.CreateModel(
            name='GlobalNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=500)),
                ('author', models.CharField(default='Nepal Tech', max_length=50)),
                ('posted', models.CharField(default='April 04, 2020', max_length=20)),
                ('scrapped', models.DateTimeField(auto_now_add=True, verbose_name='Scrapped On')),
            ],
            options={
                'verbose_name_plural': 'Global Tech News',
                'ordering': ['scrapped'],
            },
        ),
        migrations.CreateModel(
            name='TechNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=500)),
                ('author', models.CharField(default='Nepal Tech', max_length=50)),
                ('posted', models.CharField(default='April 04, 2020', max_length=20)),
                ('scrapped', models.DateTimeField(auto_now_add=True, verbose_name='Scrapped On')),
            ],
            options={
                'verbose_name_plural': 'Tech News',
                'ordering': ['scrapped'],
            },
        ),
        migrations.CreateModel(
            name='TelcoNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, unique=True)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=500)),
                ('author', models.CharField(default='Nepal Tech', max_length=50)),
                ('posted', models.CharField(default='April 04, 2020', max_length=20)),
                ('scrapped', models.DateTimeField(auto_now_add=True, verbose_name='Scrapped On')),
            ],
            options={
                'verbose_name_plural': 'Telecom News',
                'ordering': ['scrapped'],
            },
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=256)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Searched on')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, unique=True, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='editor_news/')),
                ('content', models.TextField(verbose_name='Content')),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='Published On')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Posted on')),
                ('slug', models.SlugField(max_length=150)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Editor News',
                'ordering': ['-publish_date', '-updated', '-timestamp'],
            },
        ),
    ]
