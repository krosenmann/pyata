<a href='http://www.youtube.com/watch?feature=player_embedded&v=Xpwb48qjxds' target='_blank'><img src='http://img.youtube.com/vi/Xpwb48qjxds/0.jpg' width='480' height=320 /></a>

_[watch in HD](http://www.youtube.com/v/Xpwb48qjxds&hl=pt_BR&fs=1&rel=0&hd=1)_

## Description ##
**Pyata** (Pyatã, from Tupi or yet, **Py**.thon + Pure D.**ata**) is a simple cross-plataform open-source Python module that allows people to use [Pure Data](http://puredata.info/) (aka, Pd) just like an API. In other words, it is an abstraction to Pd, that can be used for doing a lot of things that Pd can do, but without manipulate the Pd interface in a direct way.

It was developed using a technique known as "[dynamic patching](http://jeraman.wordpress.com/2009/03/22/how-to-use-pure-data-as-a-api/)", which is based on dynamic creation of Pd objects realized through sockets, achieved through [FUDI protocol](http://wiki.puredata.info/en/FUDI). This means, for example, that we can create a [osc~ 440] object sending to Pd a specific message through sockets.

So what basically the library does is to receive the commands given by users, transforming them into the equivalent message. These messages are sent to Pd, that processes them like they were a patch running inside Pd (a virtual patch), generating results. After that, these results are reloaded again into the Python program, that allows it to be always updated according the “virtual patch”.

Before starting, please, read the tutorial!

> http://code.google.com/p/pyata/wiki/Getting_Started


## Functionalities ##
This version includes:
  * Boxes creation, edition and remotion (object, number, comments, symbols and messages);
  * Get from Pd the state of any box (number of inlet/outlets, the ID of each box on Patch, values of numbers and symbols);
  * Connection management (connect and disconnect boxes);
  * Basic operations (copy, paste, duplicate, cut, save);