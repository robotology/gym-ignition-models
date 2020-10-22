# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

import os
from typing import List
from pathlib import Path


def get_models_path() -> str:
    """
    Return the path where the models have been installed.

    Returns:
        A string containing the path of the models.
    """
    models_dir = os.path.join(os.path.dirname(__file__))
    return models_dir + '/'


def get_robot_names() -> List[str]:
    """
    Return the names of the available robots.

    The name of the robot matches with the folder containing its model file.

    Returns:
        A list of strings containing the available models.
    """
    root_dir = get_models_path()
    dirs = [d for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d))]
    return [d for d in dirs if not d.startswith("__")]


def get_model_file(robot_name: str) -> str:
    """
    Return the path to the model file of the selected robot.

    Args:
        robot_name: The name of the selected robot.

    Returns:
        The path to the model of the selected robot.
    """
    if robot_name not in get_robot_names():
        raise RuntimeError(f"Failed to find robot '{robot_name}'")

    model_dir = os.path.join(get_models_path(), robot_name)

    if not os.path.isdir(model_dir):
        raise FileNotFoundError(model_dir)  # TODO

    models_found = []

    for root, dirs, files in os.walk(model_dir):
        for file in files:
            if file.endswith((".urdf", ".sdf")):
                models_found.append(file)

    if len(models_found) != 1:
        raise RuntimeError(f"Found multiple models in the same folder: {models_found}")

    model_abs_path = os.path.join(model_dir, models_found[0])
    return model_abs_path


def get_model_string(robot_name: str) -> str:
    """
    Return the string containing the selected robot model.

    Args:
        robot_name: The name of the selected robot.

    Returns:
        A string containing the selected robot model.
    """

    model_file = get_model_file(robot_name=robot_name)

    with open(model_file, "r") as f:
        string = f.read()

    return string


def setup_environment() -> None:
    """
    Configure the environment variables.
    """

    models_path = Path(get_models_path())

    if not models_path.exists():
        raise NotADirectoryError(f"Failed to find path '{models_path}'")

    # Setup the environment to find the models
    if "IGN_GAZEBO_RESOURCE_PATH" in os.environ:
        os.environ["IGN_GAZEBO_RESOURCE_PATH"] += f":{models_path}"
    else:
        os.environ["IGN_GAZEBO_RESOURCE_PATH"] = f"{models_path}"

    # Models with mesh files
    # Workaround for https://github.com/osrf/sdformat/issues/227
    models_with_mesh = ["panda", "iCubGazeboV2_5", "iCubGazeboSimpleCollisionsV2_5"]

    # Setup the environment to find the mesh files
    for model in models_with_mesh:

        model_path = Path(get_models_path()) / model

        if not model_path.exists():
            raise NotADirectoryError(f"Failed to find path '{model_path}'")

        if "IGN_GAZEBO_RESOURCE_PATH" in os.environ:
            os.environ["IGN_GAZEBO_RESOURCE_PATH"] += f':{model_path}'
        else:
            os.environ["IGN_GAZEBO_RESOURCE_PATH"] = f'{model_path}'


# Setup the environment when the package is imported
setup_environment()
