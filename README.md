# Introdução ao LangChain

Este projeto contém exemplos práticos e exercícios para aprender os fundamentos do LangChain, um framework poderoso para desenvolvimento de aplicações com IA generativa.

## 📋 Sobre o Projeto

O LangChain é uma biblioteca Python que simplifica o desenvolvimento de aplicações que utilizam modelos de linguagem grandes (LLMs). Este repositório apresenta uma introdução progressiva aos conceitos fundamentais, desde configurações básicas até pipelines complexos de processamento.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+**
- **LangChain** - Framework principal para aplicações de IA
- **OpenAI GPT** - Modelo de linguagem da OpenAI
- **Google Gemini** - Modelo de linguagem do Google
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📦 Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Conta na OpenAI (para usar GPT)
- Conta no Google AI (para usar Gemini)

### Configuração do Ambiente

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd Introducao-ao-LangChain
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**
Crie um arquivo `.env` na raiz do projeto com suas chaves de API:

```env
OPENAI_API_KEY=sua_chave_openai_aqui
GOOGLE_API_KEY=sua_chave_google_aqui
```

## 📚 Estrutura do Projeto

```
Introducao-ao-LangChain/
├── 01-fundamentos/
│   ├── 1-hello-world.py          # Primeiro contato com LangChain
│   ├── 2-init-chat-model.py      # Inicialização de modelos de chat
│   ├── 3-prompt-templates.py     # Templates de prompt básicos
│   └── 4-chat-prompt-template.py # Templates de chat avançados
├── 02-chains-e-processamento/
│   ├── 1-iniciando-com-chains.py # Introdução às chains
│   ├── 2-chains-com-decorator.py # Chains com decoradores
│   ├── 3-runnable-lambda.py      # Funções lambda executáveis
│   └── 4-pipeline-de-processamento.py # Pipelines complexos
├── requirements.txt              # Dependências do projeto
└── README.md                    # Este arquivo
```

## 🎯 Conteúdo dos Módulos

### 01 - Fundamentos

#### 1. Hello World (`1-hello-world.py`)
- Configuração básica do LangChain
- Primeira interação com um modelo de IA
- Uso do ChatOpenAI

#### 2. Inicialização de Chat Model (`2-init-chat-model.py`)
- Como inicializar diferentes modelos de chat
- Integração com Google Gemini
- Configuração de provedores de modelo

#### 3. Prompt Templates (`3-prompt-templates.py`)
- Criação de templates reutilizáveis
- Interpolação de variáveis em prompts
- Formatação de mensagens

#### 4. Chat Prompt Template (`4-chat-prompt-template.py`)
- Templates para conversas estruturadas
- Separação de mensagens do sistema e usuário
- Configuração de estilos de resposta

### 02 - Chains e Processamento

#### 1. Iniciando com Chains (`1-iniciando-com-chains.py`)
- Conceito de chains no LangChain
- Composição de prompts e modelos
- Execução sequencial de operações

#### 2. Chains com Decorator (`2-chains-com-decorator.py`)
- Uso de decoradores para criar chains
- Processamento de dados em etapas
- Combinação de múltiplas chains

#### 3. Runnable Lambda (`3-runnable-lambda.py`)
- Funções personalizadas como runnables
- Processamento de dados customizado
- Integração com o ecossistema LangChain

#### 4. Pipeline de Processamento (`4-pipeline-de-processamento.py`)
- Pipelines complexos de processamento
- Tradução e sumarização de texto
- Parsers de saída estruturados

## 🏃‍♂️ Como Executar

### Executando Exemplos Individuais

```bash
# Exemplo básico
python 01-fundamentos/1-hello-world.py

# Exemplo com chains
python 02-chains-e-processamento/1-iniciando-com-chains.py

# Pipeline completo
python 02-chains-e-processamento/4-pipeline-de-processamento.py
```

### Executando Todos os Exemplos

```bash
# Execute todos os exemplos de fundamentos
for file in 01-fundamentos/*.py; do
    echo "Executando: $file"
    python "$file"
    echo "---"
done

# Execute todos os exemplos de chains
for file in 02-chains-e-processamento/*.py; do
    echo "Executando: $file"
    python "$file"
    echo "---"
done
```

## 🔧 Configurações Importantes

### Modelos Utilizados

- **GPT-5-nano/mini**: Modelos da OpenAI (requer chave de API)
- **Gemini-2.5-flash**: Modelo do Google (requer chave de API)

### Parâmetros de Configuração

- **Temperature**: Controla a criatividade das respostas (0.0 - 1.0)
- **Model Provider**: Especifica o provedor do modelo
- **Output Parsers**: Formatam a saída dos modelos

## 📖 Conceitos Aprendidos

Após completar este projeto, você terá aprendido:

1. **Configuração básica** do LangChain
2. **Inicialização de modelos** de diferentes provedores
3. **Criação de templates** de prompt reutilizáveis
4. **Composição de chains** para processamento sequencial
5. **Uso de decoradores** para criar funções executáveis
6. **Construção de pipelines** complexos de processamento
7. **Integração com APIs** de IA (OpenAI, Google)

## 🛠️ Próximos Passos

Para continuar aprendendo LangChain, considere explorar:

- **Agents**: Para automação de tarefas complexas
- **Memory**: Para manter contexto em conversas
- **Vector Stores**: Para busca semântica em documentos
- **Document Loaders**: Para processamento de diferentes tipos de arquivo
- **Retrieval Augmented Generation (RAG)**: Para aplicações com conhecimento específico

## 🤝 Contribuições

Contribuições são bem-vindas! Se você encontrar bugs ou tiver sugestões de melhorias:

1. Abra uma issue descrevendo o problema
2. Faça um fork do projeto
3. Crie uma branch para sua feature
4. Submeta um pull request

## 📄 Licença

Este projeto é destinado a fins educacionais. Certifique-se de respeitar os termos de uso das APIs utilizadas (OpenAI, Google AI).

## 📞 Suporte

Se você tiver dúvidas ou precisar de ajuda:

- Consulte a [documentação oficial do LangChain](https://python.langchain.com/)
- Verifique as [issues do projeto](https://github.com/seu-usuario/Introducao-ao-LangChain/issues)
- Entre em contato através dos canais de comunicação do projeto

---

**Desenvolvido com ❤️ para a comunidade de desenvolvedores interessados em IA**
