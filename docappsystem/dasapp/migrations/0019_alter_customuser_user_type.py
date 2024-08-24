# Generated by Django 5.0.7 on 2024-07-25 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0018_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'admin'), (2, 'doc')], default=2, max_length=50),
        ),
    ]