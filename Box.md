# Box #
this is one of the most important class in Pyata.
though you cannot create a object of this class, it is super class of all others boxes classes: [Object](http://code.google.com/p/pyata/wiki/Object), [Number](http://code.google.com/p/pyata/wiki/Number), [Message](http://code.google.com/p/pyata/wiki/Message), [Symbol](http://code.google.com/p/pyata/wiki/Symbol) and [Comment](http://code.google.com/p/pyata/wiki/Comment).
so, as you may expect, all methods described in this document can be used in any of the classes above.

## Methods ##
### Move ###
moves the object in the patch to a new x, y.
```
move(new_x, new_y)
```
where:
> _new\_x_ = new x position of the box;

> _new\_y_ = new y position of the box;

### Verify Inlets ###
verify how many inlets owns the box.
```
verify_inlets()
```

### Verify Outlets ###
verify how many outlets owns the box.
```
verify_outlets()
```

### Select ###
selects the box
```
select()
```

### Unselect ###
unselects the box
```
unselect()
```

### Shift Select ###
selects the box. if more than one box is selected, after calling this method, all of them will still be selected.
```
shift_select()
```

### Shift Unselect ###
unselects the box. if more than one box is selected, after calling this method, all of them (but the one you called shift\_unselect) will still be selected.
```
shift_unselect()
```

### Delete ###
deletes the Box from the patch.
```
delete()
```