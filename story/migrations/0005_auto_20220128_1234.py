# Generated by Django 3.1.6 on 2022-01-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_alter_comment_id_remove_story_f_story_f_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
