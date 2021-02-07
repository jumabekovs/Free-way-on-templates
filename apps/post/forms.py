from captcha import widgets
from django import forms
from captcha.fields import ReCaptchaField


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(public_key='6LeH70oaAAAAANYOL4iJMLHsO8DPDfLxTRtvX23q',
                             private_key='6LeH70oaAAAAAK9Xtu9GrUkKKoA8jZt-S49MaZ4H',)


class FormWithCaptcha(forms.Form):
    captcha = ReCaptchaField(
        widget=widgets.ReCaptchaV2Checkbox(
        attrs={
            'data-theme': 'dark',
            'data-size': 'compact',
        }
    )
)

