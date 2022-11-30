# **Java Spring AWS DynamoDB Plugin**

Java Spring Plugin AWS DynamoDB is a set of technologies and development methodology that together support the use of Amazon DynamoDb in Java Spring Boot Applications.

This Plugin has support for projects created with Stack Java Spring Boot REST API. And given that it also supports Java Spring Boot projects that use **Maven** as a dependency manager and have their property settings in the **YAML** pattern.



In the next sections you will find detailed information on how to use Java Spring AWS DynamoDB Plugin to enable the ability to handle Amazon DynamoDb and all Spring Data support in your projects.

Below is a summary of each section of this documentation.

1. [Plugin Core Technologies](#plugin-core-technologies)
2. [Capabilities Enabled when using the Plugin](#what-are-the-capabilities-enabled)
3. [Benefits of using the Plugin](#what-are-the-benefits-of-using-java-spring-aws-dynamodb-plugin)
4. [Applying Java Spring AWS DynamoDB Plugin](#applying-java-spring-aws-dynamodb-plugin)


## **Plugin core technologies**
The purpose of this session is to inform which technologies are part of the Java Spring AWS DynamoDB Plugin.

By applying this plugin in a Java Spring Boot project, your application can benefit from the entire infrastructure of the Spring Data tool and AWS DynamoDB.


### **Technological Composition**

The definition of this Plugin was designed aiming at the greatest pains in using AWS DynamoDB together with a Java application.

We understand that quality is non-negotiable, and we look to technologies and methodologies as a means to obtain the much-desired software quality. This premise was the guide for choosing each technology detailed below.


- Production environment
    - SpringData DynamoDB
        - Amazon DynamoDB
        - Spring Data
- Development environment
    - Docker Compose
        - LocalStack
- Test environment
    - JUnit
    - TestContainers
        - LocalStack



## **What are the capabilities Enabled**

By applying the Java Spring AWS DynamoDB Plugin to your Java Spring Boot project, your project will be able to:

1. Map objects as dynamo entities and benefit from the full structure of Amazon DynamoDB
2. Create Spring Data Repositories and Benefit from Abstractions
3. Ability to build applications that use DynamoDB without using AWS
4. Create an automated integration test suite with TestContainers
5. Development environment set up next to Docker with Docker-compose and LocalStack


## **What are the benefits of using Java Spring AWS DynamoDB Plugin**

1. Easy configuration of DynamoDb and Spring Data in your project through StackSpot CLI.
2. Example Codes for Creating DynamoDb Repositories based on good practices.
3. Example Codes for Creating Converters for Java.time APIs with DynamoDb.
4. Example Code with Use Case for Spring Data DynamoDb repositories
6. Integration Testing example codes based on best practices.
7. Configuration of the test environment with JUnit and TestContainers.
8. DockerCompose for using LocalStack and DynamoDb in a development environment.


[Watch this video to see the benefits of using Java Spring AWS DynamoDB Plugin in your project](https://youtu.be/azGk4QYM_iQ)


## **Applying Java Spring AWS DynamoDB Plugin**

To apply the Java Spring AWS DynamoDB Plugin in your projects and enjoy its benefits, you must have the StackSpot CLI installed on your machine. [If not, follow this tutorial to install](https://docs.stackspot.com/docs/stk-cli/installation/).

### 1. Import the Stack on your machine

```sh
stk import stack https://github.com/zup-academy/java-springboot-restapi-stack
```

### 2. Now check if the Stack was successfully imported

```sh
stk list stack | grep java-springboot
```

### 3. Apply the Plugin, in your project directory, execute

```sh
stk apply plugin java-springboot-restapi-stack/java-spring-aws-dynamodb-plugin
```

### 4. Choose a supported RDBMS

### 5. Check the changes in your project

```sh
git status
```



## Support

If you need help, please open an [issue in Stack's Github repository](https://github.com/zup-academy/java-spring-aws-dynamodb-plugin/issues).