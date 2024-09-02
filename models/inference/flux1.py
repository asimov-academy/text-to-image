import torch

from diffusers import FluxPipeline
from inference.base_inference import BaseInference

class Flux1Inference(BaseInference):
    def load_model(self, model_path):
        return FluxPipeline.from_pretrained(model_path, torch_dtype=torch.bfloat16)

    def prepare_pipeline(self):
        self.pipe.enable_model_cpu_offload(device=self.GPU)

    def run_inference(self, positive_prompt=None, negative_prompt=None):
        image = self.pipe(
            self.PROMPT if not positive_prompt else positive_prompt,
            height=self.HEIGHT,
            width=self.WIDTH,
            guidance_scale=self.GUIDANCE,
            output_type="pil",
            num_inference_steps=self.STEPS,
            max_sequence_length=512,
            generator=torch.Generator("cpu").manual_seed(0)
        ).images[0]
        return image
