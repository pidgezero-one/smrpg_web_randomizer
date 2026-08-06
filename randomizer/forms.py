from django import forms

MODES = (
    ('open', 'Open'),
    ('linear', 'Linear'))


class GenerateForm(forms.Form):
    seed = forms.Field(required=False)
    mode = forms.ChoiceField(required=False, choices=MODES, initial='open')
    flags = forms.Field(required=False, initial='')
    cosmetics = forms.Field(required=False, initial='')
    debug_mode = forms.BooleanField(required=False, initial=False)
    debug_bps_patches = forms.BooleanField(required=False, initial=False)
    race_mode = forms.BooleanField(required=False, initial=False)
    prize_offset = forms.IntegerField(required=False, initial=None, min_value=0, max_value=46)
    mimic_offset = forms.IntegerField(required=False, initial=None, min_value=0, max_value=511)
    offset_slots = forms.BooleanField(required=False, initial=True)
    offset_mimics = forms.BooleanField(required=False, initial=True)
    offset_coins = forms.BooleanField(required=False, initial=True)
    offset_star_pieces = forms.BooleanField(required=False, initial=True)
    offset_invisible_flags = forms.BooleanField(required=False, initial=True)
