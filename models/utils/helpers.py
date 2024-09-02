import os


def get_prompt(dir = './models/prompt.txt'):
    with open(dir) as prompt:
        return prompt.read()

def get_gpu(gpu_position=1):
    position = max(0, gpu_position - 1)
    return f'cuda:{position}'

def create_and_get_path(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory
