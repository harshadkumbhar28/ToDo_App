# Generated by Django 5.0 on 2024-03-02 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description', models.TextField(max_length=100)),
                ('Date', models.CharField(max_length=20)),
                ('Status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20)),
            ],
        ),
    ]
