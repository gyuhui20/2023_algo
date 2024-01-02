# `algo_py` directory

Contains all "modules" (.py) needed for algo classes

## Utilization

To import the module `xxx.py`

```python
from algo_py import xxx
```

- the algo_py directory must be in the same directory as the file containing the import
- or the `algo_py` directory has to be added to the "PYTHONPATH" variable

### timing.py

To use the `timing` (and `timing_ret`) function, use the following syntax:

```python
from algo_py import timing

@timing.timing
def my_function(...):
    ...
```

When calling the function `my_function`, the computing time will be displayed

### matrix.py

To use any function from the `matrix` module, use the following syntax:

```python
from algo_py import matrix

Minit = matrix.init(6, 7, 0)

Mload = matrix.load("/home/foo/my_matrix_file.txt")
```

### New: bintree.py updated

To use any function from the `bintree` module, use the following syntax:

```python
from algo_py import bintree

B = bintree.BinTree(42, None, None)
```

#### Useful functions

- save / load: binary trees are saved in text files using the linear representation (see the `files` directory in the `bst` and `avl` directories)

Example:
```Python
B = bintree.load("files/bst.bintree")
```
`save`: uses the function `to_linear_rep`

`load`: uses the function `from_linear_rep`

- print / display
```python
bintree.printBinTree(B)
 -  15
  | -  8
  |  | -  1
  |    -  12
  |     | -  10
    -  28
     | -  20
     |    -  23
       -  42
        | -  35
          -  66

bintree.printer(B)
              15                              
              / \
             /   \
            /     \
           /       \
          /         \
         /           \
        /             \
       /               \
      8              28  
      / \             / \
     /   \           /   \
    /     \         /     \
   /       \       /       \
  1      12      20      42      
          /         \     / \
         /           \   /   \
        10          23  35  66      
```

#### Graphviz to display bintrees

##### Online

- Copy the result of `print(bintree.dot(T))` here: [https://dreampuf.github.io/GraphvizOnline](https://dreampuf.github.io/GraphvizOnline)

##### Console
Install Graphviz:
- ubuntu:
	```bash
	sudo apt-get graphviz
	```
- windows: [use this installation procedure](https://forum.graphviz.org/t/new-simplified-installation-procedure-on-windows/224)

You can now create image files:
- save the result of your `dot` function in a file (`bintree.dot`in the example below)
- run `dot`:
   - for instance under Ubuntu
        ```bash
        dot bintree.dot -Tpng > bintree.png
        ```
        creates `bintree.png`

##### IPython
Using the `display` functions in `bintree.py` with IPython (spyder, jupyter..)
- install the Graphviz Python module

  With Anaconda, in a terminal:
  ```bash
  conda install python-graphviz
  ```

  Or in Python console:
	```Python
	pip install Graphviz
	```

- try `bintree.display(T)` 

### queue.py

To use any function from the `queue` module, use the following syntax:

```python
from algo_py import queue

q = queue.Queue()
```
