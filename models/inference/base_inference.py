import uuid, torch, gc
from abc import ABC, abstractmethod
from utils.helpers import get_gpu, get_prompt, create_and_get_path


class BaseInference(ABC):
    def __init__(self, model_path, gpu_index=1, height=1088, width=1088, steps=15, guidance=3.5):
        self.GPU = get_gpu(gpu_index)
        self.PROMPT = get_prompt()
        self.HEIGHT = height
        self.WIDTH = width
        self.STEPS = steps
        self.GUIDANCE = guidance
        self.pipe = self.load_model(model_path)
        self.prepare_pipeline()

    @abstractmethod
    def load_model(self, model_path):
        pass

    @abstractmethod
    def prepare_pipeline(self):
        pass

    @abstractmethod
    def run_inference(self, positive_prompt=None, negative_prompt=None):
        pass

    def save_image(self, image, directory):
        path = create_and_get_path(f'./images/{directory}')
        image.save(f"{path}/{str(uuid.uuid1())}.png")
    
    def __del__(self):
        if hasattr(self, 'pipe'):
            # Libera o modelo da memória
            del self.pipe
            torch.cuda.empty_cache()
        
        # Coleta de lixo manual para garantir que tudo seja liberado
        gc.collect()

        # Se a GPU ainda tiver memória alocada, desalocar manualmente
        if torch.cuda.is_available():
            device = torch.device(self.GPU)
            with torch.cuda.device(device):
                torch.cuda.empty_cache()
                torch.cuda.ipc_collect() 
