# Generated by Django 4.1.5 on 2023-01-15 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_user_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='url',
        ),
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='uploads/%Y/%M/%D/'),
        ),
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='document',
            name='pre_processing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.CharField(max_length=200)),
                ('is_tokenized', models.BooleanField(default=False)),
                ('content_tokenized', models.CharField(max_length=200)),
                ('is_encode', models.BooleanField(default=False)),
                ('encode', models.BinaryField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
