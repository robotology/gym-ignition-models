# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

from setuptools import setup, find_packages


setup(
    name="gym-ignition-extra-models",
    version="1.0",
    author="Diego Ferigo",
    author_email="diego.ferigo@iit.it",
    description="Additional robot models for RL simulations",
    license="LGPL",
    platforms='any',
    python_requires='>=3.6',
    keywords="robot model robotics humanoid simulation urdf sdf icub",
    packages=find_packages(),
    package_data={'gym_ignition_extra_models': [
      '*/meshes/*.*',
      '*/meshes/**/**/*.*',
      '*/*.urdf',
      '*/model.config',
    ]},
    url="https://github.com/dic-iit/gym-ignition-extra-models",
)
