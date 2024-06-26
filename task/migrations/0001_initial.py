# Generated by Django 5.0.6 on 2024-06-27 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_created', models.DateTimeField(auto_created=True)),
                ('Title', models.CharField(default='', max_length=100)),
                ('Description', models.TextField()),
                ('Completed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
