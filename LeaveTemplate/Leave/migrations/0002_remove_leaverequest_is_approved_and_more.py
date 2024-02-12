# Generated by Django 4.2.10 on 2024-02-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leave', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='leaverequest',
            name='approval_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('declined', 'Declined')], default='pending', max_length=20),
        ),
    ]
