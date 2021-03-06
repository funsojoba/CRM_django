# Generated by Django 3.2.3 on 2021-05-14 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_app', '0004_auto_20210514_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
