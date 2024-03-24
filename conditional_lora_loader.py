from nodes import LoraLoader


class ConditionalLoraLoader(LoraLoader):
    FUNCTION = 'maybe_load_lora'

    @classmethod
    def INPUT_TYPES(cls):
        composed = super().INPUT_TYPES()
        composed['required']['enabled'] = ('BOOLEAN', {'default': True})
        return composed

    def maybe_load_lora(self, enabled, model, clip, **kwargs):
        if enabled:
            return self.load_lora(model=model, clip=clip, **kwargs)
        else:
            return [model, clip]
