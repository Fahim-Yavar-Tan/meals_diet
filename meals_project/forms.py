from django import forms
from .models import PersonalInfo


class Info(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ('age', 'gender', 'wrist', 'height', 'weight', 'waist', 'hips', 'child', 'child_head', 'lowest_weight',
                  'have_kids', 'Hereditary_diseases', 'physical_activity', 'fasting_blood_sugar', 'blood_sugar', 'HBA1C',
                  'triglyceride', 'Cholesterol', 'LDL', 'HDL',
                  'SGPT', 'SGOT', 'BUN', 'Creatinine', 'calcium_phosphorus', 'Sodium_potassium', 'D_3',
                  'iron', 'ferritin', 'TIBC', 'total_cal', 'total_protein', 'total_carbohydrate',
                  'total_fat', 'eating_habits', 'allergy', 'Special_drugs',)
    # age = forms.IntegerField()
    # gender = forms.CharField()
    # wrist = forms.FloatField()
    # height = forms.FloatField()
    # weight = forms.FloatField()
    # waist = forms.FloatField()
    # hips = forms.FloatField()
    # child = forms.BooleanField()
    # child_head = forms.FloatField()
    # PHYSICAL_ACTIVITY = (
    #     ('low', 'خیلی کم'),
    #     ('2days', 'دو روز در هفته'),
    #     ('3days', 'سه روز در هفته'),
    #     ('4days', 'چهار روز در هفته'),
    #     ('5days', 'پنج روز در هفته یا بیشتر'),
    #     ('pro', 'ورزش کار حرفه ای'),
    # )
    # lowest_weight = forms.FloatField()
    # have_kids = forms.BooleanField()
    # Hereditary_diseases = forms.CharField(max_length=200)
    # physical_activity = forms.ChoiceField(choices=PHYSICAL_ACTIVITY)
    # fasting_blood_sugar = forms.FloatField()
    # blood_sugar = forms.FloatField()
    # HBA1C = forms.FloatField()
    # triglyceride = forms.FloatField()
    # Cholesterol = forms.FloatField()
    # LDL = forms.FloatField()
    # HDL = forms.FloatField()
    # SGPT = forms.FloatField()
    # SGOT = forms.FloatField()
    # BUN = forms.FloatField()
    # Creatinine = forms.FloatField()
    # calcium_phosphorus = forms.FloatField()
    # Sodium_potassium = forms.FloatField()
    # D_3 = forms.FloatField()
    # iron = forms.FloatField()
    # ferritin = forms.FloatField()
    # TIBC = forms.FloatField()
    # EATING_HABITS = (
    #     ('low', 'خیلی کم'),
    #     ('mid', 'متوسط'),
    #     ('Relatively much', 'به نسبت زیاد'),
    #     ('too much', 'پر خور'),
    # )
    # total_cal = forms.FloatField()
    # total_protein = forms.FloatField()
    # total_carbohydrate = forms.FloatField()
    # total_fat = forms.FloatField()
    # eating_habits = forms.ChoiceField(choices=EATING_HABITS)
    # allergy = forms.CharField(max_length=100)
    # Special_drugs = forms.CharField(max_length=100)
