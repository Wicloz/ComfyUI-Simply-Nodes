from math import gcd


class ResolutionSDXL:
    RETURN_TYPES = ['INT', 'INT']
    FUNCTION = 'convert_resolution'
    CATEGORY = 'prompt'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'resolution': [['1080x1080', '720x1280', '1280x720', '600x1920']],
                'multiplier': ['FLOAT', {'default': 1}],
            },
        }

    def convert_resolution(self, resolution, multiplier):
        width, height = resolution.split('x')
        width = int(width) // 8
        height = int(height) // 8

        denominator = gcd(width, height)
        base = round(denominator * multiplier)

        return [
            base * 8 * (width // denominator),
            base * 8 * (height // denominator),
        ]
