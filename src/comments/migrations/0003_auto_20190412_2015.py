# Generated by Django 2.1.7 on 2019-04-12 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2, null=True),
        ),
    ]
