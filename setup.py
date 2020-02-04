# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

import os
import shutil
import platform
from setuptools.command.build_ext import build_ext
from setuptools import setup, find_packages, Extension


class CopyMeshes(Extension):
    extension_name = "CopyMeshes"

    def __init__(self):
        Extension.__init__(self, name=self.extension_name, sources=[])


class BuildExtension(build_ext):
    """
    Setuptools build extension handler.
    It processes all the extensions listed in the 'ext_modules' entry.
    """

    # Name of the python package (the name used to import the module)
    PACKAGE_NAME = "gym_ignition_extra_models"

    # Shared mesh directory
    SHARED_MESH_DIR = "meshes"

    # Dict that defines the folders to copy during the build process
    FROM_ORIG_TO_DEST = {
        f"{SHARED_MESH_DIR}/iCubGazeboV2_5": "iCubGazeboV2_5/meshes",
    }

    def run(self) -> None:
        if len(self.extensions) != 1 or not isinstance(self.extensions[0], CopyMeshes):
            raise RuntimeError("This class can only build one CopyMeshes object")

        if platform.system() != "Linux":
            raise RuntimeError("Only Linux is currently supported")

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext) -> None:
        if ext.name != CopyMeshes.extension_name:
            print(f"Skipping unsupported extension '{ext.name}'")
            return

        if self.inplace:
            raise RuntimeError("Editable mode is not supported by this project")

        # Get the temporary external build directory
        ext_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))

        # Package directory
        pkg_dir = os.path.join(ext_dir, self.PACKAGE_NAME)

        # Check that the directory exists
        if not os.path.isdir(pkg_dir):
            raise RuntimeError(f"The build package directory '{pkg_dir}' does not exist")

        # Copy the folders
        for orig, dest in self.FROM_ORIG_TO_DEST.items():
            orig_folder = os.path.join(pkg_dir, orig)
            dest_folder = os.path.join(pkg_dir, dest)

            if not os.path.isdir(orig_folder):
                raise RuntimeError(f"Folder '{orig_folder}' does not exist")

            if os.path.isdir(dest_folder):
                shutil.rmtree(dest_folder)

            shutil.copytree(orig_folder, dest_folder)

        # Remove the shared mesh folder
        shutil.rmtree(os.path.join(pkg_dir, self.SHARED_MESH_DIR))


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
      'meshes/*.*',
      'meshes/**/*.*',
      'meshes/**/**/*.*',
      '*/meshes/*.*',
      '*/meshes/**/*.*',
      '*/meshes/**/**/*.*',
      '*/*.sdf',
      '*/*.urdf',
      '*/model.config',
    ]},
    ext_modules=[CopyMeshes()],
    cmdclass={
      'build_ext': BuildExtension,
    },
    url="https://github.com/dic-iit/gym-ignition-extra-models",
)
