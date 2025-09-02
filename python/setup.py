from os import path
import setuptools
from shutil import copyfile
from sys import platform

dirname = path.dirname(path.abspath(__file__))

if platform == "linux" or platform == "linux2":
    lib_path = path.abspath(path.join(dirname, '../build/lib/libthundergbm.so'))
elif platform == "win32":
    lib_path = path.abspath(path.join(dirname, '../build/bin/Debug/thundergbm.dll'))
elif platform == "darwin":
    lib_path = path.abspath(path.join(dirname, '../build/lib/libthundergbm.dylib'))
else:
    print("OS not supported!")
    exit()
if not path.exists(path.join(dirname, "thundergbm", path.basename(lib_path))):
    copyfile(lib_path, path.join(dirname, "thundergbm", path.basename(lib_path)))
setuptools.setup(name="amd_thundergbm",
                 version="0.3.16",
                 packages=["thundergbm"],
                 package_dir={"python": "thundergbm"},
                 description="A Fast GBM Library on GPUs and CPUsi with ROCm support",
                 long_description="""The mission of ThunderGBM is to help users easily and efficiently apply GBDTs and Random Forests to solve problems. ThunderGBM exploits GPUs and multi-core CPUs to achieve high efficiency""",
                 long_description_content_type="text/plain",
                 license='Apache-2.0',
                 author='Xtra Computing Group',
                 maintainer='thundergbm contributorsi, Advanced Micro Devices, Inc.',
                 maintainer_email='wenzy@comp.nus.edu.sg',
                 url="https://github.com/rocm/thundergbm",
				 documentation="https://rocm.docs.amd.com/projects/thundergbm/en/latest/index.html",
                 package_data={"thundergbm": [path.basename(lib_path)]},
                 install_requires=['numpy', 'scipy', 'scikit-learn'],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: Apache Software License",
                 ],
                 )
