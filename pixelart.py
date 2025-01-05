from PIL.Image import Dither, Quantize
from PIL import Image
import numpy as np
import torch


class FixupPixelArt:
    RETURN_TYPES = ['IMAGE']
    FUNCTION = 'fixup'

    @classmethod
    def INPUT_TYPES(cls):
        return {
            'required': {
                'images': ['IMAGE'],
                'pixel_size': ['INT', {'default': 1, 'min': 1}],
                'palette_colors': ['INT', {'default': 12, 'min': 1, 'max': 256}],
            },
        }

    @staticmethod
    def pil2tensor(image):
        return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

    @staticmethod
    def tensor2pil(tensor):
        i = 255. * tensor.cpu().numpy()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        return img

    def fixup(self, images, pixel_size, palette_colors):
        images = [image for image in images]

        for idx in range(len(images)):
            images[idx] = self.tensor2pil(images[idx])

            images[idx] = images[idx].resize((int(round(images[idx].width / pixel_size)), int(round(images[idx].height / pixel_size))), resample=Image.NEAREST)
            images[idx] = images[idx].quantize(colors=palette_colors, method=Quantize.MAXCOVERAGE, dither=Dither.NONE)

            images[idx] = images[idx].resize((images[idx].width * pixel_size, images[idx].height * pixel_size), resample=Image.NEAREST)
            images[idx] = images[idx].convert('RGB')

            images[idx] = self.pil2tensor(images[idx])

        return images
