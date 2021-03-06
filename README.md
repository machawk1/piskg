[![image](https://github.com/machawk1/piskg/blob/master/meta/piskgLogo.png?raw=true)](https://pypi.python.org/pypi/piskg)
# piskg: Python IPFS Swarm Key Generator

This program generates swarm.key file for IPFS Private Network feature.

## Installing

``` {.sourceCode .bash}
$ pip install piskg
```

## Usage

```
$ piskg > ~/.ipfs/swarm.key
```

Change `~/.ipfs/` to different directory if you use custom `IPFS_PATH`. To
join a private network, save the key value to your `~/.ipfs/swarm.key`.

When using this feature, you will not be able to connect to the default
bootstrap nodes since they are not part of your private network, so you
will need to set up your own bootstrap nodes.

To prevent your node from even trying to connect to the default
bootstrap nodes, run:

``` {.sourceCode .bash}
$ ipfs bootstrap rm --all
```

To be extra cautious, you can also set the LIBP2P\_FORCE\_PNET
environment variable to 1 to force the usage of private networks. If no
private network is configured, the daemon will fail to start.

Credits
=======

Direct port of <https://github.com/Kubuxu/go-ipfs-swarm-key-gen/>. Setup
information derived from
<https://github.com/ipfs/go-ipfs/issues/3397#issuecomment-284341649>.

Logo derived from work by [Eagle Eye](https://thenounproject.com/eagleeye/) ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and [Sergey Demushkin](https://thenounproject.com/mockturtle/) ([CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)) and itself licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

License
=======

MIT
