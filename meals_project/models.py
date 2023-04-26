from django.db import models
from django.contrib.auth.models import User


class PersonalInfo(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    # name = models.CharField(max_length=100, verbose_name='نام')
    age = models.SmallIntegerField(default=0, null=False, blank=False, verbose_name='سن')
    gender = models.CharField(max_length=20, null=False, blank=False, verbose_name='جنسیت')
    wrist = models.FloatField(default=0, null=False, blank=False, verbose_name='دور مچ')
    height = models.FloatField(default=0, null=False, blank=False, verbose_name='قد')
    weight = models.FloatField(default=0, null=False, blank=False, verbose_name='وزن')
    waist = models.FloatField(default=0, null=False, blank=False, verbose_name='دور کمر')
    hips = models.FloatField(default=0, null=False, blank=False, verbose_name='دور باسن')
    child = models.BooleanField(default=False)
    child_head = models.FloatField(default=0, null=False, blank=False, verbose_name='دور سر بچه')
    PHYSICAL_ACTIVITY = (
        ('low', 'خیلی کم'),
        ('2days', 'دو روز در هفته'),
        ('3days', 'سه روز در هفته'),
        ('4days', 'چهار روز در هفته'),
        ('5days', 'پنج روز در هفته یا بیشتر'),
        ('pro', 'ورزش کار حرفه ای'),
    )
    lowest_weight = models.FloatField(default=0, null=False, blank=False, verbose_name='کمترین وزن در 2 یا 3 سال اخیر')
    have_kids = models.BooleanField(default=False)
    Hereditary_diseases = models.CharField(max_length=200, null=True, blank=True, default=None)
    physical_activity = models.CharField(max_length=40, choices=PHYSICAL_ACTIVITY, null=False, blank=False)
    fasting_blood_sugar = models.FloatField(default=0, null=False, blank=False, verbose_name='قند خون ناشتا')
    blood_sugar = models.FloatField(default=0, null=False, blank=False, verbose_name='قند خون')
    HBA1C = models.FloatField(default=0, null=False, blank=False)
    triglyceride = models.FloatField(default=0, null=False, blank=False)
    Cholesterol = models.FloatField(default=0, null=False, blank=False)
    LDL = models.FloatField(default=0, null=False, blank=False)
    HDL = models.FloatField(default=0, null=False, blank=False)
    SGPT = models.FloatField(default=0, null=False, blank=False)
    SGOT = models.FloatField(default=0, null=False, blank=False)
    BUN = models.FloatField(default=0, null=False, blank=False)
    Creatinine = models.FloatField(default=0, null=False, blank=False)
    calcium_phosphorus = models.FloatField(default=0, null=False, blank=False)
    Sodium_potassium = models.FloatField(default=0, null=False, blank=False)
    D_3 = models.FloatField(default=0, null=False, blank=False)
    iron = models.FloatField(default=0, null=False, blank=False)
    ferritin = models.FloatField(default=0, null=False, blank=False)
    TIBC = models.FloatField(default=0, null=False, blank=False)
    EATING_HABITS = (
        ('low', 'خیلی کم'),
        ('mid', 'متوسط'),
        ('Relatively much', 'به نسبت زیاد'),
        ('too much', 'پر خور'),
    )
    total_cal = models.FloatField(default=0, null=False, blank=False)
    total_protein = models.FloatField(default=0, null=False, blank=False)
    total_carbohydrate = models.FloatField(default=0, null=False, blank=False)
    total_fat = models.FloatField(default=0, null=False, blank=False)
    eating_habits = models.CharField(max_length=100, choices=EATING_HABITS, null=False, blank=False,
                                     verbose_name='عادت های غذایی')
    allergy = models.CharField(max_length=100, null=True, blank=True, verbose_name='آلرژی های غذایی')
    Special_drugs = models.CharField(max_length=100, null=True, blank=True, verbose_name='دارو های خاص')

    class Meta:
        verbose_name = 'اطلاعات رژیم گیرنده'
        verbose_name_plural = 'اطلاعات رژیم گیرنده'

    # def __str__(self):
    #     return f"{self.user.first_name} {self.user.last_name}"
    # def __str__(self):
    #     full_name = self.user.get_full_name()
    # def __str__(self):
    #     return self.name
    # def head(self):
    #     if self.child:

# class BIOCHEMISTRY(models.Model):
#     #user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
#     fasting_blood_sugar = models.FloatField(default=0, null=False, blank=False, verbose_name='قند خون ناشتا')
#     blood_sugar = models.FloatField(default=0, null=False, blank=False, verbose_name='قند خون')
#     HBA1C = models.FloatField(default=0, null=False, blank=False)
#     triglyceride = models.FloatField(default=0, null=False, blank=False)
#     Cholesterol = models.FloatField(default=0, null=False, blank=False)
#     LDL = models.FloatField(default=0, null=False, blank=False)
#     HDL = models.FloatField(default=0, null=False, blank=False)
#     SGPT = models.FloatField(default=0, null=False, blank=False)
#     SGOT = models.FloatField(default=0, null=False, blank=False)
#     BUN = models.FloatField(default=0, null=False, blank=False)
#     Creatinine = models.FloatField(default=0, null=False, blank=False)
#     calcium_phosphorus = models.FloatField(default=0, null=False, blank=False)
#     Sodium_potassium = models.FloatField(default=0, null=False, blank=False)
#     D_3 = models.FloatField(default=0, null=False, blank=False)
#     iron = models.FloatField(default=0, null=False, blank=False)
#     ferritin = models.FloatField(default=0, null=False, blank=False)
#     TIBC = models.FloatField(default=0, null=False, blank=False)
#
#
# class DietMeals(models.Model):
#     #user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
#     EATING_HABITS = (
#         ('low', 'خیلی کم'),
#         ('mid', 'متوسط'),
#         ('Relatively much', 'به نسبت زیاد'),
#         ('too much', 'پر خور'),
#     )
#     total_cal = models.FloatField(default=0, null=False, blank=False)
#     total_protein = models.FloatField(default=0, null=False, blank=False)
#     total_carbohydrate = models.FloatField(default=0, null=False, blank=False)
#     total_fat = models.FloatField(default=0, null=False, blank=False)
#     eating_habits = models.CharField(max_length=100, choices=EATING_HABITS, null=False, blank=False,
#                                      verbose_name='عادت های غذایی')
#     allergy = models.CharField(max_length=100, null=True, blank=True, verbose_name='آلرژی های غذایی')
#     Special_drugs = models.CharField(max_length=100, null=True, blank=True, verbose_name='دارو های خاص')
