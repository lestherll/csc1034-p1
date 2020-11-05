# CSC1034: Practical 1

## Intro
This package is built as a part of the CSC1034: Portfolio-1. 
This programs displays a scence with a panda in its natural habitat.

## Usage
```shell
python walking_panda.py [--optional_parameter_1] [optional_value_1] [--optional_parameter_n] [optional_value_n]
```
Adding optional parameters or arguments when running the program in CLI is in the form that is shown above. 
Note that arguments will not always have values that must be provided. An example is shown below.

#### Examples
```shell
python walking_panda.py --no-rotate
```
The example above allows the program to disable rotation at the start of the program. As you can see, no value was provided.

```shell
python walking_panda.py --scale 2
```
The example above scales the size of the actor Panda by a factor of 2 or twice. Notice that here, a value was and must be provided.

```shell
python walking_panda.py --scale 2 --no-rotate
```
It is also possible to have multiple arguments at once. You must, however, be careful since some arguments don't work together. 
For example, calling `--anti-clockwise` will not have any effect if `--no-rotate` was also passed because the camera is not rotating at all.

### List of Optional Parameters
#### Camera related
- `--no-rotate` 
This disables the camera rotation and sets the camera to default view that I have set when starting the program.
- `--anti-clockwise` 
This rotates the camera in the other direction. The program will not do anything if `--no-rotate` was passed.
- `--top-view` 
This shows the top-view of the panda. This will not work unless `--no-rotate` is passed because the rotation method, `spinCameraTask()` , is currently a **task**.
This means that it will get called every frame allowing `setTopView()` to only get called during initialisation/start of program.
In other words, `spinCameraTask()` controls the camera view every frame not allowing `setTopView()` to do anything for the rest of the runtime.

#### Size related
- `--scale x` 
This scales the size of the panda by **x** factor.
- `--size x`
This overrides the default size(0.005) of the actor panda. 
I have added this only to work with `--scale` since scale works as a multiplier for the actual size passed to pandaActor.setScale().

#### Others
- `--no-panda`
This makes the program to render without the panda.