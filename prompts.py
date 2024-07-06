import re
from pathlib import Path
import numpy.random as npr


class MultilineText:
    RETURN_TYPES = ['STRING']
    FUNCTION = 'get_text_without_comments'
    CATEGORY = 'prompt'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'text': ('STRING', {'default': '', 'multiline': True}),
            },
        }

    def get_text_without_comments(self, text):
        return [re.sub(r'#.*', '', text)]


class TextFlow:
    RETURN_TYPES = ['STRING', 'STRING', 'STRING', 'STRING']
    FUNCTION = 'maybe_concatenate'
    CATEGORY = 'prompt'
    WHITESPACE_REGEX = re.compile(r'\s+')

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'delimiter': ('STRING', {'default': ', '}),
                'collapse_whitespace': ('BOOLEAN', {'default': True}),
                'concatenate': ('BOOLEAN', {'default': False}),
            },
            'optional': {
                'text_a': ('STRING', {'forceInput': True}),
                'text_b': ('STRING', {'forceInput': True}),
                'text_c': ('STRING', {'forceInput': True}),
                'text_d': ('STRING', {'forceInput': True}),
            },
        }

    @staticmethod
    def _collapse_whitespace(text):
        return re.sub(TextFlow.WHITESPACE_REGEX, ' ', text)

    def maybe_concatenate(self, delimiter, collapse_whitespace, concatenate, text_a='', text_b='', text_c='', text_d=''):
        if collapse_whitespace:
            text_a = self._collapse_whitespace(text_a)
            text_b = self._collapse_whitespace(text_b)
            text_c = self._collapse_whitespace(text_c)
            text_d = self._collapse_whitespace(text_d)

        if not concatenate:
            return [text_a, text_b, text_c, text_d]

        full_text = delimiter.join([text_a, text_b, text_c, text_d])
        return [full_text, full_text, full_text, full_text]


class RandomStyle:
    RETURN_TYPES = ['STRING']
    FUNCTION = 'make_random_style'
    CATEGORY = 'prompt'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'style_def_file': [[str(path) for path in Path('models/styles/').glob('*.txt')]],
                'seed': ['INT', {'default': 0, 'min': 0, 'max': 0xffffffffffffffff}],
                'strength': ['FLOAT', {'default': 0.1, 'min': 0.0, 'max': 1.0, 'step': 0.01}],
                'override': ['STRING', {'default': '', 'multiline': True}],
            },
        }

    def make_random_style(self, style_def_file, seed, strength, override):
        if len(override.strip()) > 0:
            return [override]

        rng = npr.default_rng(seed)
        styles = ''

        with open(style_def_file, 'r') as fp:
            for line in fp:
                if rng.random() < strength:
                    styles += f'{line.strip()}, '

        return [styles]
