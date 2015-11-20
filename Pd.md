# Pd #
an important class in Pyata. if you want to use this library, is this class you must import at first. you also must have a instance of this class inside your program. it will be responsible to communicate with the Pd process and has all the methods related to basic Pd functionalities (copy, paste, save, and others).

## Methods ##
### Init ###
initializes the library stuff and the Pd itself. must be called before doing any kind of thing with Pyata.
```
init()
```

### Quit ###
finishes the library stuff and the Pd itself. must be called when your program is about to end.
```
quit()
```

### Save ###
saves the modifications in the patch.
```
save()
```

### Clear ###
clears the patch.
```
clear()
```

### Get Box List ###
returns the boxes available in Pd.
```
get_box_list()
```

### Get Connection List ###
returns the connections available in Pd.
```
get_connection_list()
```

### Copy ###
copies the selected boxes (if you want to select/unselect a box, just check select()/unselect() method, from Box class).
```
copy()
```

### Paste ###
pastes boxes available in transfer board.
```
paste(new_x, new_y)
```
where:
> _new\_x_ = the x position where you want to paste the objects;

> _new\_y_ = the y position where you want to paste the objects;


### Duplicate ###
duplicates the selected boxes (if you want to select/unselect a box, just check select()/unselect() method, from Box class).
```
duplicate(new_x, new_y)
```
where:
> _new\_x_ = the x position where you want to duplicate the objects;

> _new\_y_ = the y position where you want to duplicate the objects;

### Selectall ###
selects all the objects available in Pd.
```
selectall()
```