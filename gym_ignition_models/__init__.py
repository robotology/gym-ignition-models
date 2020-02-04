# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

import os
from typing import List


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