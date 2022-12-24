# Generated by Django 4.0.7 on 2022-11-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnerabilities', '0035_add_package_url_to_packages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='package_url',
            field=models.CharField(db_index=True, help_text='The Package URL for this package.', max_length=1000),
        ),
        migrations.AlterField(
            model_name='package',
            name='plain_package_url',
            field=models.CharField(db_index=True, help_text='The Package URL for this package without qualifiers and subpath.', max_length=1000),
        ),
    ]