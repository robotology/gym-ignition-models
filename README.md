<p align="center">
<h1 align="center">gym-ignition-extra-models</h1>
</p>

<p align="center">
<h4 align="center">Additional robot models for <a href="https://github.com/robotology/gym-ignition">gym-ignition</a></h4>
</p>

These models have been mainly tuned and tested to work in [Ignition Gazebo](ignitionrobotics.org/) and [PyBullet](https://pybullet.org/wordpress/).

### Setup

This repository can be installed with the `pip` package manager as follows:

```bash
pip3 install git+https://github.com/dic-iit/gym-ignition-extra-models.git
```

Only GNU/Linux distributions are currently supported.

### Configuration

If you use Ignition Gazebo, you need to execute the following commands (from outside the directory where you cloned this repository):

```sh
PKG_DIR=$(python -c "import gym_ignition_extra_models, inspect, os; print(os.path.dirname(inspect.getfile(gym_ignition_extra_models)))")
export SDF_FILE=$PKG_DIR:$SDF_FILE
```

If you want to make this change persistent, add the lines above to your `~/.bashrc`.

**Note:** waiting an upstream fix, you also need to add to the `IGN_FILE_PATH` environment variable all the directories that contain model's meshes.

### Usage

You can use these models either with the standalone simulators, or find and import them in your Python code. Here below an Python example of the utility functions provided by the package:

```python
import gym_ignition_extra_models as m

print(f"Models have been installed in {m.get_models_path()}")
print(f"Available robots: {m.get_robot_names()}")
print("\nModel files:")

for robot_name in m.get_robot_names():
    print(f"{robot_name}: {m.get_model_file(robot_name)}")
```

### Supported models

| Robot Name | Screenshot |
| ---------- | ---------- |
|            |            |

