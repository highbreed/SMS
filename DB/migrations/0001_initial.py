# Generated by Django 2.2.5 on 2020-01-08 12:03

import DB.validators
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=200, unique=True)),
                ('is_current_session', models.BooleanField(blank=True, default=False, null=True)),
                ('next_session_begins', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[DB.validators.class_room_validator])),
                ('capacity', models.IntegerField(blank=True, default=25, help_text='Enter total number of sits defaults is set to 25')),
                ('occupied_sits', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassStream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_stream', to='DB.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('parent_type', models.CharField(choices=[('F', 'Father'), ('M', 'Mother'), ('G', 'Guardian')], max_length=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='DB.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[DB.validators.stream_validator])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('unique_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('date_of_birth', models.DateField(validators=[DB.validators.students_date_of_birth_validator])),
                ('admission_date', models.DateTimeField(auto_now_add=True)),
                ('admission_number', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='StudentsImages')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[DB.validators.subject_validator])),
                ('subject_code', models.CharField(blank=True, max_length=10, null=True)),
                ('is_selectable', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], max_length=1)),
                ('subject_teaching', models.ManyToManyField(blank=True, null=True, to='DB.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_lecturer', models.BooleanField(default=False)),
                ('is_parent', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_pictures/')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three')], max_length=10)),
                ('is_current_term', models.BooleanField(blank=True, default=False, null=True)),
                ('next_term_begins', models.DateField(blank=True, null=True)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.AcademicYear')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.ManyToManyField(to='DB.Subject')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_address', to='DB.Address')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_address', to='DB.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to='DB.Parent')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_parent', to='DB.Student')),
            ],
        ),
        migrations.CreateModel(
            name='StudentClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(auto_now_add=True)),
                ('date_to', models.DateField(blank=True, null=True)),
                ('class_stream', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='DB.ClassStream')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_class', to='DB.Student')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mission', models.TextField(blank=True, null=True)),
                ('vision', models.TextField(blank=True, null=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='DB.Address')),
            ],
        ),
        migrations.CreateModel(
            name='ParentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_address', to='DB.Address')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_address', to='DB.Parent')),
            ],
        ),
        migrations.CreateModel(
            name='ClassTeachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='DB.ClassStream')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_teacher', to='DB.Teacher')),
            ],
        ),
        migrations.AddField(
            model_name='classstream',
            name='stream_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='class_stream', to='DB.Stream'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='subjects',
            field=models.ManyToManyField(to='DB.Subject'),
        ),
    ]
