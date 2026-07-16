.. meta::
   :description: Build ThunderGBM with ROCm support from source for AMD GPUs
   :keywords: amd, rocm, finance, financial, fintech, algorithm, gpu, install, setup, env, docker, package, contribute, develop, build, pip, make

**************************************
Build ThunderGBM on ROCm from source
**************************************

Prerequisites
=============

Before proceeding, ensure that you have installed a supported ROCm version,
operating system, and Python environment that are compatible with the ROCm
Finance libraries. Verify that your system includes a supported AMD Instinct
GPU. For guidance, see `AMD Finance installation prerequisites
<https://rocm.docs.amd.com/projects/rocm-finance/en/latest/install/prerequisites.html>`__.

For a consistent and streamlined setup experience, it's recommended to use
a ROCm development environment Docker container. See `Install AMD Finance
<https://rocm.docs.amd.com/projects/rocm-finance/en/latest/install/install.html>`__
for instructions.

Build from source
=================

1. Install required software dependencies.

   .. code-block:: shell

      apt-get update && apt-get install -y --no-install-recommends  git libomp-dev python3-venv curl ca-certificates gpg wget
      wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | sudo tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
      echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ noble main' | sudo tee /etc/apt/sources.list.d/kitware.list >/dev/null
      apt-get update && apt-get install -y --no-install-recommends cmake

2. Clone the `<https://github.com/AMD-Ecosystem/thundergbm>`__ source code from GitHub.

   .. code-block:: shell

      git clone --recurse-submodules https://github.com/AMD-Ecosystem/thundergbm.git

3. Create and activate a Python virtual environment.

   .. code-block:: shell

      python -m venv thundergbm-build
      source thundergbm-build/bin/activate

4. Build the shared object library.

   .. code-block:: shell

      # Set the GPU target
      export AMDGPU_TARGETS="gfx942"
      export CMAKE_PREFIX_PATH=/opt/rocm/lib/cmake/
      export CMAKE_MODULE_PATH=/opt/rocm/lib/cmake
      export CMAKE_POLICY_VERSION_MINIMUM=3.5
      export CMAKE_C_COMPILER=hipcc
      export CMAKE_CXX_COMPILER=hipcc
      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rocm/lib/llvm/lib/
      export LDFLAGS="-L/opt/rocm/lib -Wl,-rpath,/opt/rocm/lib"
       
      cd thundergbm
      cmake -S . -B build
      cmake --build build -- -j 8

5. Build and install the Python package.

   .. code-block:: shell

      cd python
      pip install setuptools
      python setup.py bdist_wheel
      pip install dist/amd_thundergbm.whl 

6. Verify the installation.

   .. code-block:: shell

      pip show -v amd_thundergbm 

   .. dropdown:: Example output

      .. code-block:: shell-session

         Name: amd_thundergbm
         Version: 0.3.16
         Summary: A Fast GBM Library on GPUs and CPUs with ROCm support
         Home-page: https://github.com/AMD-Ecosystem/thundergbm
         Author: Xtra Computing Group


7. Run the Python examples.

   .. code-block:: shell

      cd examples
      LD_PRELOAD="/opt/rocm/lib/llvm/lib/libomp.so" python ranking_demo.py
      LD_PRELOAD="/opt/rocm/lib/llvm/lib/libomp.so" python classification_demo.py
      LD_PRELOAD="/opt/rocm/lib/llvm/lib/libomp.so" python regression_demo.py
