from .conditional_lora_loader import ConditionalLoraLoader
from .prompts import MultilineText, TextFlow
from .resolution import ResolutionSDXL

NODE_CLASS_MAPPINGS = {
    'WF_ConditionalLoraLoader': ConditionalLoraLoader,
    'WF_MultilineText': MultilineText,
    'WF_TextFlow': TextFlow,
    'WF_ResolutionSDXL': ResolutionSDXL,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'WF_ConditionalLoraLoader': 'Conditional LoRA Loader',
    'WF_MultilineText': 'Multiline Text',
    'WF_TextFlow': 'Text Flow Controller',
    'WF_ResolutionSDXL': 'Select SDXL Resolution',
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
