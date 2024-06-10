### Conversor de Moedas

#### Descrição do Projeto

O Conversor de Moedas é uma aplicação desenvolvida para facilitar a conversão de valores entre diferentes moedas. Ao fornecer um valor em uma determinada moeda, a API retorna o valor convertido para outras moedas especificadas.

#### Exemplos de Moedas Suportadas:
- USD (Dólar Americano)
- BRL (Real Brasileiro)
- EUR (Euro)
- GBP (Libra Esterlina)
- JPY (Iene Japonês)

#### Funcionamento

O usuário insere um valor e a moeda de origem, e a API converte esse valor para as moedas de destino desejadas. Por exemplo:

- **Produto custa 80,00 BRL**
- **Convertido para USD: 15,69 USD**

#### Tecnologias Utilizadas

- **Docker**: Para a criação e gerenciamento de contêineres, garantindo um ambiente isolado e consistente para a aplicação.
- **FastAPI**: Framework web utilizado para construir a API, proporcionando alta performance e facilidade no desenvolvimento de aplicações web e serviços de backend.

#### Funcionalidades Principais

- Conversão de valores entre múltiplas moedas.
- Suporte para diversas moedas internacionais.
- Atualização automática das taxas de câmbio.
- Interface de fácil utilização para requisições de conversão.

#### Como Utilizar

1. **Configuração do Ambiente**:
   - Certifique-se de ter o Docker instalado e configurado em sua máquina.
   - Clone o repositório do projeto.
   - Utilize os comandos Docker para construir e iniciar os contêineres da aplicação.

2. **Fazendo uma Requisição**:
   - Envie uma requisição HTTP para a API com o valor e a moeda de origem.
   - A API retornará o valor convertido para as moedas de destino especificadas.

Com essas funcionalidades, o Conversor de Moedas proporciona uma solução eficiente e prática para necessidades de conversão de valores entre diferentes moedas.