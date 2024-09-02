import torch

from diffusers import StableDiffusion3Pipeline
from inference.base_inference import BaseInference


class StableDiffusionInference(BaseInference):
    def load_model(self, model_path):
        return StableDiffusion3Pipeline.from_pretrained(model_path, torch_dtype=torch.float16)

    def prepare_pipeline(self):
        self.pipe.to(self.GPU)

    def run_inference(self, positive_prompt=None, negative_prompt=None):
        image = self.pipe(
            self.PROMPT if not positive_prompt else positive_prompt,
            negative_prompt=negative_prompt if negative_prompt else '',
            num_inference_steps=self.STEPS,
            guidance_scale=self.GUIDANCE,
            height=self.HEIGHT,
            width=self.WIDTH,
            max_sequence_length=512,
        ).images[0]
        return image
