# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='income',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'a', b'$0-$35,000'), (b'b', b'$35,001-$50,000'), (b'c', b'$50,001-$100,000'), (b'd', b'$100,001+')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='orientation',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'Men', b'Men'), (b'Women', b'Women'), (b'Everyone', b'Everyone'), (b'Neither', b'Neither'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='race',
            field=models.CharField(blank=True, max_length=15, null=True, choices=[(b'Asian', b'Asian'), (b'Middle Eastern', b'Middle Eastern'), (b'Black', b'Black'), (b'Native American', b'Native American'), (b'Hispanic/Latin', b'Hispanic/Latin'), (b'Pacific Islander', b'Pacific Islander'), (b'White', b'White'), (b'Mixed', b'Mixed'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
    ]
