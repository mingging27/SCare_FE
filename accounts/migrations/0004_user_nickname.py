# Generated by Django 5.0.7 on 2024-07-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_is_child_remove_user_is_parent_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]