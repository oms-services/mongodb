# _MongoDB_ OMS Microservice

[![Open Microservice Specification](https://img.shields.io/badge/OMS%20Enabled-👍-green.svg?)](https://openmicroservices.org)

This container should be used for connecting to a hosted MongoDB server.
Alternatively, it does come its own MongoDB server for testing.

## Direct usage in [Storyscript](https://storyscript.io/):

#### Redis Example
```coffee
# Storyscript
value = mongodb insert collection: "my.col" value: {"name": "Tom"}
```

Curious to [learn more](https://docs.storyscript.io/)?

✨🍰✨

## Usage with [OMS CLI](https://www.npmjs.com/package/microservices/oms)

##### Set
```shell
$ omg run insert -a value=<VALUE> -a collection=<collection> -e MONGODB_URI=<MONGODB_URI>
```

**Note**: The OMS CLI requires [Docker](https://docs.docker.com/install/) to be installed.

## License
[MIT License](https://github.com/omg-services/mongodb/blob/master/LICENSE).
