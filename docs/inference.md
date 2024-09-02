# Documentação para Inferências com Modelos FLUX.1 e Stable Diffusion

## Visão Geral

Este guia fornece instruções detalhadas sobre como usar as classes **`Flux1Inference`** e **`StableDiffusionInference`** para realizar inferências de imagens. Ambas as classes suportam a inserção de prompts positivos e negativos durante a inferência, permitindo controle flexível sobre o conteúdo gerado. A principal diferença entre os modelos está no comportamento do parâmetro de orientação (`guidance`).

## Uso Comum das Classes de Inferência

Tanto o **FLUX.1** quanto o **Stable Diffusion** permitem gerar imagens a partir de descrições textuais, ajustando parâmetros como resolução, passos de inferência, e orientação de prompt.

### Atributos Comuns

- **`model_path` (str)**: Caminho para o modelo pré-treinado. Deve apontar para o diretório onde o modelo está salvo.
- **`gpu_index` (int)**: Índice da GPU a ser utilizada para a inferência (por exemplo, `1` para a primeira GPU, `2` para a segunda, etc.).
- **`height` (int)**: Altura da imagem gerada em pixels. O padrão é `1088`.
- **`width` (int)**: Largura da imagem gerada em pixels. O padrão é `1088`.
- **`steps` (int)**: Número de passos de difusão a serem realizados. Mais passos geralmente resultam em imagens de melhor qualidade, mas aumentam o tempo de processamento.
- **`guidance` (float)**: Escala de orientação para guiar a geração da imagem conforme o prompt. **O comportamento varia entre os modelos**:
  - **FLUX.1**: Um valor mais alto significa maior aderência ao prompt.
  - **Stable Diffusion**: Um valor mais alto permite mais criatividade e menos aderência ao prompt.
- **`positive_prompt` (str, opcional)**: Um prompt textual positivo para guiar a geração da imagem. Se não for fornecido, o modelo usará o prompt padrão configurado.
- **`negative_prompt` (str, opcional)**: Um prompt textual negativo para evitar certos elementos ou estilos na imagem gerada. Suportado apenas pelo **Stable Diffusion**.

### Métodos Comuns

- **`run_inference(self, positive_prompt=None, negative_prompt=None)`**: Executa a inferência com os prompts fornecidos.
  - **`positive_prompt`**: Prompt positivo para a geração de imagem.
  - **`negative_prompt`**: Prompt negativo para evitar elementos indesejados (apenas para **Stable Diffusion**).

- **`save_image(self, image, directory)`**: Salva a imagem gerada no diretório especificado.

### Exemplo de Uso Comum

```python
# Importação das classes
from models.inference.flux1 import Flux1Inference
from models.inference.stable_diffusion3 import StableDiffusionInference

# Configuração do modelo FLUX.1
flux1_inference = Flux1Inference(
    model_path="/caminho/para/modelo/flux1",
    gpu_index=1,
    height=1088,
    width=1088,
    steps=15,
    guidance=3.5
)

# Configuração do modelo Stable Diffusion
stable_diffusion_inference = StableDiffusionInference(
    model_path="/caminho/para/modelo/stable-diffusion",
    gpu_index=2,
    height=1088,
    width=1088,
    steps=35,
    guidance=7.5  # Note que um valor mais alto permite mais criatividade
)

# Inferência com FLUX.1
flux1_image = flux1_inference.run_inference(
    positive_prompt="Uma paisagem de montanha ao pôr do sol"
)

# Inferência com Stable Diffusion
stable_image = stable_diffusion_inference.run_inference(
    positive_prompt="Uma cidade futurista durante a noite",
    negative_prompt="sem carros voadores"
)

# Salvando as imagens
flux1_inference.save_image(flux1_image, "flux1")
stable_diffusion_inference.save_image(stable_image, "stable_diffusion")

# Liberando recursos da GPU
del flux1_inference
del stable_diffusion_inference
```

## Diferenças Específicas dos Modelos

### FLUX.1 (`Flux1Inference`)

- **Orientação (`guidance`)**: Um valor mais alto de `guidance` força o modelo a seguir mais rigorosamente o prompt textual fornecido. Ideal para quando você deseja que a imagem gerada corresponda de perto à descrição textual.
- **Prompt Negativo**: Não é utilizado pelo modelo FLUX.1. Qualquer valor fornecido para `negative_prompt` será ignorado.

### Stable Diffusion (`StableDiffusionInference`)

- **Orientação (`guidance`)**: Um valor mais alto de `guidance` permite mais criatividade e menos aderência ao prompt textual. Isso é útil para quando você deseja resultados mais variados e menos previsíveis.
- **Prompt Negativo**: Suportado. Pode ser usado para evitar certos elementos na imagem gerada. Por exemplo, `negative_prompt="sem carros voadores"` instruirá o modelo a evitar incluir carros voadores na imagem.

## Detalhes dos Parâmetros de Inferência

- **`model_path`**: Certifique-se de que este caminho é válido e aponta para o modelo correto. A falta do modelo correto resultará em erros de carregamento.
- **`gpu_index`**: Escolha a GPU correta para evitar conflitos, especialmente em sistemas com múltiplas GPUs.
- **`height` e `width`**: Ajuste de acordo com a resolução desejada. Resoluções mais altas exigem mais memória de GPU.
- **`steps`**: Aumente para melhorar a qualidade da imagem, mas esteja ciente de que isso também aumentará o tempo de inferência.
- **`guidance`**: Ajuste de acordo com o comportamento desejado do modelo:
  - **FLUX.1**: Mais alto para maior aderência ao prompt.
  - **Stable Diffusion**: Mais alto para permitir mais criatividade e menos aderência.
- **`positive_prompt`**: Use para orientar o modelo a gerar uma imagem específica.
- **`negative_prompt`**: Use apenas com **Stable Diffusion** para evitar elementos específicos.

## Considerações Finais

- **Liberação de Memória**: Utilize `del` após a inferência para liberar a memória da GPU.
- **Ajuste de Parâmetros**: Os parâmetros podem ser ajustados para melhor atender às suas necessidades de geração de imagem.

Com essa documentação, você deve ser capaz de configurar e utilizar os modelos **FLUX.1** e **Stable Diffusion** para gerar imagens conforme suas especificações. Lembre-se de ajustar os parâmetros conforme necessário para obter os melhores resultados.