class RefineToggle:
    RETURN_TYPES = ['IMAGE', 'FLOAT']
    FUNCTION = 'do_toggle'
    CATEGORY = 'utils'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'primary_image': ['IMAGE'],
                'primary_denoise_strength': ['FLOAT', {'default': 1/3, 'min': 0.0, 'max': 1.0, 'step': 0.05}],
                'alternate_image': ['IMAGE'],
                'alternate_denoise_strength': ['FLOAT', {'default': 1/2, 'min': 0.0, 'max': 1.0, 'step': 0.05}],
                'use_alternate': ['BOOLEAN', {'default': False}],
            },
        }

    def do_toggle(self, primary_image, primary_denoise_strength, alternate_image, alternate_denoise_strength, use_alternate):
        if use_alternate:
            return (alternate_image, alternate_denoise_strength)
        return (primary_image, primary_denoise_strength)
