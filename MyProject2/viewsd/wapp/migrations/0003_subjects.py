# Generated by Django 4.0.4 on 2022-05-26 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wapp', '0002_rename_wapp_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('subject_name', models.CharField(max_length=100)),
                ('paper_code', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=100)),
            ],
        ),
    ]
