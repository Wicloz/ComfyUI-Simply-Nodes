from .conditional_lora_loader import ConditionalLoraLoader
from .prompts import MultilineText, TextFlow, RandomStyle
from .resolution import ResolutionSDXL
from .pixelart import FixupPixelArt

NODE_CLASS_MAPPINGS = {
    'WF_ConditionalLoraLoader': ConditionalLoraLoader,
    'WF_MultilineText': MultilineText,
    'WF_TextFlow': TextFlow,
    'WF_ResolutionSDXL': ResolutionSDXL,
    'WF_RandomStyle': RandomStyle,
    'WF_FixupPixelArt': FixupPixelArt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    'WF_ConditionalLoraLoader': 'Conditional LoRA Loader',
    'WF_MultilineText': 'Multiline Text',
    'WF_TextFlow': 'Text Flow Controller',
    'WF_ResolutionSDXL': 'Select SDXL Resolution',
    'WF_RandomStyle': 'Random Style Prompt',
    'WF_FixupPixelArt': 'Fix Pixel Art',
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
