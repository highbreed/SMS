# Generated by Django 2.2.5 on 2020-01-09 04:54

import DB.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DB', '0003_auto_20200108_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarryOverStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three')], max_length=10, null=True)),
                ('academic_year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.AcademicYear')),
                ('class_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.ClassRoom')),
                ('stream', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.Stream')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.Student')),
            ],
        ),
        migrations.CreateModel(
            name='RepeatingStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three')], max_length=10, null=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.AcademicYear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpa', models.FloatField(null=True)),
                ('cat_gpa', models.FloatField(null=True)),
                ('term', models.CharField(blank=True, choices=[('ONE', 'One'), ('TWO', 'Two'), ('THREE', 'Three')], max_length=10, null=True)),
                ('academic_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.AcademicYear')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.Student')),
            ],
        ),
        migrations.CreateModel(
            name='SubjectAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.ManyToManyField(related_name='allocated_subjects', to='DB.Subject')),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DB.Teacher')),
                ('term', models.ForeignKey(blank=DB.models.Term, null=True, on_delete=django.db.models.deletion.CASCADE, to='DB.Term')),
            ],
        ),
        migrations.AddField(
            model_name='studentclass',
            name='main_class',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='DB.ClassRoom'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TeacherSubject',
        ),
    ]
