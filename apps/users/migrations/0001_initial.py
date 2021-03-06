# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 11:07
from __future__ import unicode_literals

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='', max_length=6)),
                ('birday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('height', models.CharField(blank=True, max_length=8, null=True, verbose_name='身高')),
                ('weight', models.CharField(blank=True, max_length=8, null=True, verbose_name='体重')),
                ('city', models.CharField(blank=True, max_length=8, null=True, verbose_name='城市')),
                ('spfamily', models.CharField(choices=[('1', '单亲家庭'), ('2', '非单亲')], default='2', max_length=6)),
                ('education', models.CharField(blank=True, default='本科', max_length=6, null=True)),
                ('one_child', models.CharField(choices=[('1', '独生子女'), ('2', '非独生子女')], default='1', max_length=6)),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('mstatus', models.CharField(choices=[('never_married', '从未结婚'), ('ivorce', '离异'), ('widowed', '丧偶')], default='never_married', max_length=30)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('work', models.CharField(blank=True, default='白领', max_length=6, null=True)),
                ('salary', models.CharField(blank=True, default='10w', max_length=6, null=True)),
                ('car', models.CharField(choices=[('1', '有车'), ('2', '没有')], default='2', max_length=6)),
                ('home', models.CharField(choices=[('1', '有房'), ('2', '没有')], default='2', max_length=6)),
                ('image', models.ImageField(default='', upload_to='head/%Y/%m', verbose_name='headImg')),
                ('addtime', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_type', models.CharField(blank=True, choices=[('register', '注册'), ('forgetpw', '忘记密码')], max_length=20, null=True, verbose_name='验证码类别')),
                ('phone', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('code', models.CharField(default='', max_length=20, verbose_name='验证码')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '手机验证码',
                'verbose_name_plural': '手机验证码',
            },
        ),
    ]
