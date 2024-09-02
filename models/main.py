from dotenv import load_dotenv
from inference.flux1 import Flux1Inference
from inference.stable_diffusion3 import StableDiffusionInference

load_dotenv()

# FLUX1 INFERENCE
flux1_inference = Flux1Inference("/home/samuel/models_hf/text-to-image/black-forest-labs-FLUX.1-dev", gpu_index=1, steps=10)
flux1_image = flux1_inference.run_inference()
flux1_inference.save_image(flux1_image, "flux1")

del flux1_inference

# STABLE DIFFUSION INFERENCE
stable_diffusion_inference = StableDiffusionInference("/home/samuel/projects/stable-diffusion-poc/models/stable-diffusion-3", gpu_index=1)
stable_image = stable_diffusion_inference.run_inference(negative_prompt='')
stable_diffusion_inference.save_image(stable_image, "stable_diffusion")