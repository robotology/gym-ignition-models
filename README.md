<p align="center">
  <h1 align="center">gym-ignition-models</h1>
</p>

<p align="center">
  <a href="https://pypi.org/project/gym-ignition-models/">
  <img src="https://img.shields.io/pypi/v/gym-ignition-models.svg" />
  </a>
  <a href="https://pypi.org/project/gym-ignition-models/">
  <img src="https://img.shields.io/pypi/pyversions/gym-ignition-models.svg" />
  </a>
  <a href="https://pypi.org/project/gym-ignition-models/">
  <img src="https://img.shields.io/pypi/status/gym-ignition-models.svg" />
  </a>
  <a href="https://pypi.org/project/gym-ignition-models/">
  <img src="https://img.shields.io/pypi/format/gym-ignition-models.svg" />
  </a>
  <a href="https://pypi.org/project/gym-ignition-models/">
  <img src="https://img.shields.io/pypi/l/gym-ignition-models.svg" />
  </a>
</p>

<p align="center">
  <h4 align="center">Robot models for <a href="https://github.com/robotology/gym-ignition">gym-ignition</a></h4>
</p>

These models have been mainly tuned and tested to work in [Ignition Gazebo](https://ignitionrobotics.org/).

### Setup

This repository can be installed with the `pip` package manager as follows:

```bash
# From PyPI
pip3 install gym-ignition-models

# From the repository (always containing the most recent changes)
pip3 install git+https://github.com/dic-iit/gym-ignition-models.git
```

Only GNU/Linux distributions are currently supported.

### Configuration

If you use Ignition Gazebo, you need to execute the following commands (from outside the directory where you cloned this repository):

```sh
PKG_DIR=$(python -c "import gym_ignition_models, inspect, os; print(os.path.dirname(inspect.getfile(gym_ignition_models)))")
export SDF_PATH=$PKG_DIR:SDF_PATH
```

If you want to make this change persistent, add the lines above to your `~/.bashrc`.

**Note:** waiting an [upstream fix](https://bitbucket.org/osrf/sdformat/issues/227/error-loading-meshes-from-a-relative), you also need to add to the `IGN_FILE_PATH` environment variable all the directories that contain model's meshes.

### Usage

You can use these models either with the standalone simulators, or find and import them in your Python code. Here below an Python example of the utility functions provided by the package:

```python
import gym_ignition_models as m

print(f"Models have been installed in {m.get_models_path()}")
print(f"Available robots: {m.get_robot_names()}")
print("\nModel files:")

for robot_name in m.get_robot_names():
    print(f"{robot_name}: {m.get_model_file(robot_name)}")
```

### Supported models

| Robot Name | Screenshot |
| ---------- | ---------- |
| `ground_plane` | <img src="https://user-images.githubusercontent.com/469199/73735685-f3fa4b80-473f-11ea-897d-28fcac85f8a6.png" height="300"> |
| `cartpole` | <img src="https://user-images.githubusercontent.com/469199/73771326-7570ce80-477e-11ea-82bc-d160d4bb88b8.png" height="300"> |
| `pendulum` | <img src="https://user-images.githubusercontent.com/469199/73772768-1b253d00-4781-11ea-88e7-b21340351549.png" height="300"> |
| `iCubGazeboV2_5` </br> `iCubGazeboSimpleCollisionsV2_5` | <img src="https://user-images.githubusercontent.com/469199/73731308-90205480-4738-11ea-876c-e9be502829ef.png" height="300"> |
| `panda` | <img src="https://user-images.githubusercontent.com/469199/73738280-7f75db80-4744-11ea-805c-318e3b064847.png" height="300"> |
| `character` | <img src="https://user-images.githubusercontent.com/469199/75965269-d8ae6780-5ec8-11ea-9712-605b600bf3b2.png" height="300"> |
