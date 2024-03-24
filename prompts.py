import re


class MultilineText:
    RETURN_TYPES = ['STRING']
    FUNCTION = 'get_text_verbatim'
    CATEGORY = 'prompt'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'text': ('STRING', {'default': '', 'multiline': True}),
            },
        }

    def get_clean_text(self, text):
        cleaned = ''

        for line in text.split('\n'):
            line = line.split('#', 1)[0]
            cleaned += line

        return [cleaned]

    def get_text_verbatim(self, text):
        return [text]


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
