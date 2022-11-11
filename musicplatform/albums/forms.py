from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
import os


class SongValidation(BaseInlineFormSet):
    def clean(self):
        super(SongValidation, self).clean()
        AUDIO_EXTENSIONS = [".mp3", ".wav"]
        non_empty_forms = 0
        for form in self:
            if form.cleaned_data:
                non_empty_forms += 1
                split = os.path.splitext(str(form.cleaned_data["audio"]))
                if split[1] not in AUDIO_EXTENSIONS:
                    raise ValidationError("Audio file must be .mp3 or .wav")
        if non_empty_forms - len(self.deleted_forms) < 1:
            raise ValidationError("Album must contain at least one song")
