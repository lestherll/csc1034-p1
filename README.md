# CSC1034: Practical 1

## Intro
This package is built as a part of the CSC1034: Portfolio-1.

## Usage
```shell
python walking_panda.py [--optional_parameter_1] [optional_value_1] [--optional_parameter_n] [optional_value_n]
```
Adding optional parameters or arguments when running the program in CLI is in the form that is shown above. Note that arguments will not always have values that must be provided. An example is shown below.

#### Examples
```shell
python walking_panda.py --no-rotate
```
The example above allows the program to disable rotation at the start of the program. As you can see, no value was provided.

```shell
python walking_panda.py scale 2
```
The example above scales the size of the actor Panda by a factor of 2 or twice. Notice that here, a value was and must be provided.

```shell
python walking_panda.py scale 2
```
It is also possible to have multiple arguments at once. You must, however, be careful since some arguments don't work together. For example, calling `--anti-clockwise` will not have any effect if `--no-rotate` was also called.

### List of Optional Parameters
#### Camera related
- `--no-rotate` 
This disables the camera rotation and sets the camera to default view that I have set when starting the program
- `--anti-clockwise` 
This rotates the camera in the other direction. The program will not do anything if `--no-rotate` was called.
- `--top-view` 
This shows the top-view of the panda.

#### Size related
- `--scale x` 
This scales the size of the panda by **x** factor.
