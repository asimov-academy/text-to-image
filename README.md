# Documentação do Projeto Text-to-Image

## Sumário

1. [Introdução](#introdução)
2. [Como Clonar o Projeto e Configurar o Ambiente](#como-clonar-o-projeto-e-configurar-o-ambiente)
3. [Instalação de Dependências com Poetry](#instalação-de-dependências-com-poetry)
4. [Executando o Script de Teste](#executando-o-script-de-teste)
5. [Documentação de Inferência](#documentação-de-inferência)
6. [FLUX.1 Arquitetura](#flux1-arquitetura)
7. [FLUX.1 vs Stable Diffusion](#flux1-vs-stable-diffusion)

---

## Introdução

O projeto **Text-to-Image** é uma aplicação que utiliza modelos de difusão para gerar imagens a partir de prompts textuais. Ele suporta dois modelos principais: **FLUX.1** e **Stable Diffusion**, permitindo uma personalização detalhada do processo de inferência, incluindo o uso de prompts positivos e negativos.

### Documentação de Inferência

Para detalhes sobre como usar os modelos de inferência e os parâmetros disponíveis, consulte a [Documentação de Inferência](./docs/inference.md).

## Como Clonar o Projeto e Configurar o Ambiente

### Passo 1: Clonar o Repositório do GitHub

Primeiro, clone o repositório do projeto do GitHub para o seu ambiente local. Use o comando abaixo no terminal:

```bash
git clone https://github.com/asimov-academy/text-to-image.git
```

### Passo 2: Navegar até o Diretório do Projeto

Depois de clonar o repositório, navegue até o diretório do projeto:

```bash
cd text-to-image
```

## Configuração do Ambiente com .env

O projeto **Text-to-Image** requer um arquivo `.env` para configurar variáveis de ambiente específicas que otimizam o uso da GPU pelo PyTorch.

### Passo 3: Criar o Arquivo `.env`

Há duas formas de configurar o arquivo `.env` para o projeto:

1. **Criar manualmente o arquivo `.env`**:

   Crie um arquivo chamado `.env` na raiz do projeto e adicione a seguinte configuração:

   ```bash
   PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"
   ```

   Esta configuração otimiza a alocação de memória CUDA para melhorar a eficiência e estabilidade durante a inferência.

2. **Usar o arquivo `.env-example` fornecido**:

   O projeto vem com um arquivo de exemplo chamado `.env-example`. Você pode renomeá-lo para `.env` para configurar automaticamente o ambiente:

   ```bash
   mv .env-example .env
   ```

### Importância da Configuração do `.env`

A configuração `PYTORCH_CUDA_ALLOC_CONF="expandable_segments:True"` permite ao PyTorch gerenciar melhor a memória da GPU, evitando problemas de fragmentação e garantindo que o modelo utilize eficientemente os recursos disponíveis durante a inferência.

---

## Instalação de Dependências com Poetry

O projeto utiliza **Poetry** para gerenciamento de dependências e ambiente. Poetry facilita a instalação de pacotes e a criação de um ambiente virtual isolado para o projeto.

### Passo 4: Instalar Poetry

Se você ainda não tiver o **Poetry** instalado, você pode instalá-lo seguindo as instruções do site oficial: [Instalação do Poetry](https://python-poetry.org/docs/#installation).

### Passo 5: Instalar Dependências

Com o Poetry instalado, você pode instalar todas as dependências do projeto executando o seguinte comando no diretório raiz do projeto:

```bash
poetry install
```

Este comando irá:

- Criar um ambiente virtual isolado para o projeto.
- Instalar todas as dependências listadas no arquivo `pyproject.toml`.

## Executando o Script de Teste

Após instalar as dependências, você pode testar a configuração executando o script principal do projeto.

### Passo 6: Ativar o Ambiente Virtual

Antes de executar qualquer script, ative o ambiente virtual criado pelo Poetry:

```bash
poetry shell
```

### Passo 7: Executar o Script Principal

Para executar um teste de inferência de imagem, execute o script `main.py` localizado no diretório `models`:

```bash
python ./models/main.py
```

Este script de teste carregará os modelos, executará inferências baseadas em prompts textuais e salvará as imagens geradas no diretório especificado.

### Observações

- **Configuração de GPU**: Certifique-se de que sua configuração de GPU está correta e que os drivers necessários estão instalados.
- **Prompt Textual**: O script `main.py` utilizará um prompt padrão ou pode ser configurado para aceitar um prompt específico durante a execução.

## Documentação de Inferência

Para obter detalhes sobre como personalizar inferências e utilizar os diferentes parâmetros dos modelos, consulte a [Documentação de Inferência](./docs/inference.md).

## FLUX.1 Arquitetura

Para obter detalhes sobre a arquitetura do modelo Flux.1 da black forest labs, consulte a [FLUX.1 Arquitetura(./docs/flux1_architecture.md).

## FLUX.1 vs Stable Diffusion

Para saber pontos fortes e fracos dos modelos em um comparativo, consulte a [FLUX.1 vs Stable Diffusion](./docs/flux_vs_sd.md).
