# Copyright (C) 2020 Istituto Italiano di Tecnologia (IIT). All rights reserved.
# This software may be modified and distributed under the terms of the
# GNU Lesser General Public License v2.1 or any later version.

import os
import shutil

import setuptools
from setuptools.command.build_ext import build_ext


class CopyMeshes(setuptools.Extension):
    extension_name = "CopyMeshes"

    def __init__(self):
        setuptools.Extension.__init__(self, name=self.extension_name, sources=[])


class BuildExtension(build_ext):
    """
    Setuptools build extension handler.
    It processes all the extensions listed in the "ext_modules" entry.
    """

    # Name of the python package (the name used to import the module)
    PACKAGE_NAME = "gym_ignition_models"

    # Shared mesh directory
    SHARED_MESH_DIR = "meshes"

    # Dict that defines the folders to copy during the build process
    FROM_DEST_TO_ORIG = {
        "iCubGazeboV2_5/meshes": f"{SHARED_MESH_DIR}/iCubGazeboV2_5",
        "iCubGazeboSimpleCollisionsV2_5/meshes": f"{SHARED_MESH_DIR}/iCubGazeboV2_5",
    }

    def run(self) -> None:
        if len(self.extensions) != 1 or not isinstance(self.extensions[0], CopyMeshes):
            raise RuntimeError("This class can only build one CopyMeshes object")

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
            raise RuntimeError(
                f"The build package directory '{pkg_dir}' does not exist"
            )

        # Copy the folders
        for dest, orig in self.FROM_DEST_TO_ORIG.items():
            orig_folder = os.path.join(pkg_dir, orig)
            dest_folder = os.path.join(pkg_dir, dest)

            if not os.path.isdir(orig_folder):
                raise RuntimeError(f"Folder '{orig_folder}' does not exist")

            if os.path.isdir(dest_folder):
                shutil.rmtree(dest_folder)

            shutil.copytree(orig_folder, dest_folder)

        # Remove the shared mesh folder
        shutil.rmtree(os.path.join(pkg_dir, self.SHARED_MESH_DIR))


# Read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    ext_modules=[CopyMeshes()],
    cmdclass=dict(build_ext=BuildExtension),
)
