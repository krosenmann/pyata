# Others #

In this section are listed some global functions that can be acessed any time during the execution of the program.


## Functions ##
### Connect ###
Connects two boxes.
```
connect(box_orig, outlet, box_dest, intlet)
```
where:

> _box\_orig_ = the box where the connections starts;

> _outlet_ = number of the outlet from _box\_orig_ where the connection starts;

> _box\_dest_ = the box where the connections ends;

> _inlet_ = number of the inlet from _box\_orig_ where the connection ends;

### Disconnect ###
Disconnects two boxes.
```
disconnect(box_orig, outlet, box_dest, intlet)
```
where:

> _box\_orig_ = the box where the connections starts;

> _outlet_ = number of the outlet from _box\_orig_ where the connection starts;

> _box\_dest_ = the box where the connections ends;

> _inlet_ = number of the inlet from _box\_orig_ where the connection ends;


### Search Box ###
Searchs the indice (ID) of a specific box in memory. If there's no box with the given specification, the function returns -1.
```
search_box(box)
```
where:

> _box_ = box to be searched

### Search Connection ###
Searchs the indice (ID) of a specific connection in memory. If there's no connection with the given specification, the function returns -1.
```
search_connection(box_orig, outlet, box_dest, intlet)
```
where:

> _box\_orig_ = the box where the connections starts;

> _outlet_ = number of the outlet from _box\_orig_ where the connection starts;

> _box\_dest_ = the box where the connections ends;

> _inlet_ = number of the inlet from _box\_orig_ where the connection ends;




