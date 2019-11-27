# _MongoDB_ Open Microservice

> Access a MongoDB server

[![Open Microservice Specification Version](https://img.shields.io/badge/Open%20Microservice-1.0-477bf3.svg)](https://openmicroservices.org) [![Open Microservices Spectrum Chat](https://withspectrum.github.io/badge/badge.svg)](https://spectrum.chat/open-microservices) [![Open Microservices Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v1.4%20adopted-ff69b4.svg)](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md) [![Open Microservices Commitzen](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## Introduction

This project is an example implementation of the [Open Microservice Specification](https://openmicroservices.org), a standard originally created at [Storyscript](https://storyscript.io) for building highly-portable "microservices" that expose the events, actions, and APIs inside containerized software.

## Getting Started

The `oms` command-line interface allows you to interact with Open Microservices. If you're interested in creating an Open Microservice the CLI also helps validate, test, and debug your `oms.yml` implementation!

See the [oms-cli](https://github.com/microservices/oms) project to learn more!

### Installation

```
npm install -g @microservices/oms
```

## Usage

### Open Microservices CLI Usage

Once you have the [oms-cli](https://github.com/microservices/oms) installed, you can run any of the following commands from within this project's root directory:

#### Actions

##### insertOne

> Insert one entry into a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| value | `any` | `true` | None | The value to insert into MongoDB |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run insertOne \ 
    -a collection='*****' \ 
    -a value='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### insertMany

> Insert many entries into a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| values | `list` | `true` | None | The values to insert into MongoDB. |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run insertMany \ 
    -a collection='*****' \ 
    -a values='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### findOne

> Finds one entry in a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run findOne \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### findMany

> Finds many entry in a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run findMany \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### count

> Count number of matching entries in a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run count \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### updateOne

> Updates one entry in a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| value | `any` | `true` | None | The value to insert into MongoDB |
| upsert | `boolean` | `false` | None | If set to 'true', creates a new document when no document matches the query criteria.  |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run updateOne \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -a value='*****' \ 
    -a upsert='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### updateMany

> Update many entry in a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| value | `any` | `true` | None | The value to insert into MongoDB |
| upsert | `boolean` | `false` | None | If set to 'true', creates a new document when no document matches the query criteria.  |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run updateMany \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -a value='*****' \ 
    -a upsert='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### deleteOne

> Delete one entry from a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run deleteOne \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### deleteMany

> Delete many entries from a collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| query | `map` | `true` | None | The MongoDB search query |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run deleteMany \ 
    -a collection='*****' \ 
    -a query='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### drop

> Drop an entire collection.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run drop \ 
    -a collection='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

##### listCollection

> List all collections.
##### Action Arguments

| Argument Name | Type | Required | Default | Description |
|:------------- |:---- |:-------- |:--------|:----------- |
| collection | `string` | `true` | None | The MongoDB collection to use |
| MONGODB_URI | `string` | `false` | None | The MongoDB URI to connect to.  |

``` shell
oms run listCollection \ 
    -a collection='*****' \ 
    -e MONGODB_URI=$MONGODB_URI
```

## Contributing

All suggestions in how to improve the specification and this guide are very welcome. Feel free share your thoughts in the Issue tracker, or even better, fork the repository to implement your own ideas and submit a pull request.

[![Edit mongodb on CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/oms-services/mongodb)

This project is guided by [Contributor Covenant](https://github.com/oms-services/.github/blob/master/CODE_OF_CONDUCT.md). Please read out full [Contribution Guidelines](https://github.com/oms-services/.github/blob/master/CONTRIBUTING.md).

## Additional Resources

* [Install the CLI](https://github.com/microservices/oms) - The OMS CLI helps developers create, test, validate, and build microservices.
* [Example OMS Services](https://github.com/oms-services) - Examples of OMS-compliant services written in a variety of languages.
* [Example Language Implementations](https://github.com/microservices) - Find tooling & language implementations in Node, Python, Scala, Java, Clojure.
* [Storyscript Hub](https://hub.storyscript.io) - A public registry of OMS services.
* [Community Chat](https://spectrum.chat/open-microservices) - Have ideas? Questions? Join us on Spectrum.
