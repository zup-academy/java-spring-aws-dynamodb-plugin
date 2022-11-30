# **Java Spring AWS DynamoDB Plugin**

Plugin Java Spring AWS DynamoDB é um conjunto de técnologias e metodologia de desenvolvimento que juntos auxiliam no uso do Amazon DynamoDb em Aplicações Java Spring Boot. 

Este Plugin possui suporte para projetos criados junto a Stack Java Spring Boot REST API. E Dado a isso também suporta projetos Java Spring Boot que utilizem **Maven** como gerenciador de dependencias e tenham suas configurações de properties no padrão **YAML**.



Nas proximas sessões você encontrará em detalhes informações sobre como utilizar Plugin Java Spring AWS DynamoDB  para habilitar a capacidade de lidar com  Amazon DynamoDb e todo suporte do Spring Data em seus projetos.

Abaixo esta de forma sumariazada cada sessão desta documentação.

1. [Técnologias base da Plugin](#tecnologias-base-da-plugin)
2. [Capacidades Habilitadas ao uso da Plugin](#quais-são-as-capacidades-habilitadas)
3. [Beneficio de utilizar a Plugin](#quais-os-beneficios-de-utilizar-java-spring-aws-dynamodb-plugin)
4. [Aplicando Java Spring AWS DynamoDB Plugin](#aplicando-java-spring-aws-dynamodb-plugin)


## **Tecnologias base da Plugin**
Objetivo desta sessão é informar quais são as técnologias que fazem parte do Java Spring AWS DynamoDB Plugin.

Ao aplicar este plugin em um projeto Java Spring Boot, sua aplicação poderá se beneficiar de toda infraestrutura da ferramenta Spring Data e AWS DynamoDB.


### **Composição Técnologica**

A definição deste Plugin foi pensada visando as maiores dores no uso do AWS DynamoDB junto a um aplicativo Java.

Entendemos que a qualidade é inegociavel, e olhamos para as técnologias e metodologias como meio para obter a tão desejada qualidade no software. Essa premissa foi o guia para escolha de cada técnologia detalhada abaixo.


- Ambiente de produção
    - Spring Data DynamoDB
        - Amazon DynamoDB
        - Spring Data
- Ambiente de desenvolvimento
    - Docker Compose
        - LocalStack
- Ambiente de testes
    - JUnit
    - TestContainers
        - LocalStack



## **Quais são as capacidades Habilitadas**

Ao aplicar em seu projeto Java Spring Boot, o Java Spring AWS DynamoDB Plugin, seu projeto será capaz:

1. Mapear objetos como entidades dynamo e se beneficiar de toda estrutura do Amazon DynamoDB
2. Criar Repositories da Spring Data e se beneficiar das abstrações
3. Capacidade de criar aplicativos que utilizam DynamoDB sem utilizar AWS
4. Criar uma suite de testes de integração automatizada junto a TestContainers
5. Ambiente de desenvolvimento configurado junto ao Docker com Docker-compose e LocalStack


## **Quais os Beneficios de Utilizar Java Spring AWS DynamoDB Plugin**

1. Facilidade na configuração do DynamoDb e Spring Data em seu projeto através da StackSpot CLI.
2. Codigos de exemplo de Criação de Repositories do DynamoDb baseado em boas praticas.
3. Codigos de exemplo de Criação de Converters para APIs da Java.time junto ao DynamoDb.
4. Codigo de exemplo com Caso de Uso dos repositories do Spring Data DynamoDb
6. Codigos de exemplo de Testes de integração baseado em boas praticas.
7. Configuração do ambiente de testes com JUnit e TestContainers.
8. DockerCompose para uso da LocalStack e DynamoDb em ambiente de desenvolvimento.


[Assita este video para ver os beneficios de utilizar Java Spring AWS DynamoDB Plugin em seu projeto](https://youtu.be/azGk4QYM_iQ)


## **Aplicando Java Spring AWS DynamoDB Plugin**

Para Aplicar o Java Spring AWS DynamoDB Plugin em  seus projetos e desfrutar de seus beneficios é necessário que você tenha a CLI da StackSpot instalada em sua maquina. [Caso você não tenha siga este tutorial para fazer a instalação](https://docs.stackspot.com/docs/stk-cli/installation/).

### 1. Importe a Stack em sua maquina

```sh
stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
```

### 2. Agora verifique se a Stack foi importada com sucesso

```sh
stk list stack | grep java-springboot
```

### 3. Aplique o Plugin, no diretorio do seu projeto, execute

```sh
stk apply plugin java-springboot-restapi-stack/java-spring-aws-dynamodb-plugin
```   

### 4. Escolha um RDBMS suportado

### 5. Verifque as modificações em seu projeto

```sh
git status
```   



## Suporte

Caso precise de ajuda, por favor abra uma [issue no repositorio do Github da Stack](https://github.com/zup-academy/java-spring-aws-dynamodb-plugin/issues).