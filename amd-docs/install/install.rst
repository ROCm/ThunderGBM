.. meta::
   :description: Install ThunderGBM with ROCm support for AMD GPUs
   :keywords: amd, rocm, finance, financial, fintech, algorithm, gpu, install, setup, env, docker, pip, package, quick, start, lib

***************************
Install ThunderGBM with pip
***************************

.. _thundergbm-install-prerequisites:

Prerequisites
=============

Before proceeding, ensure that you have installed a supported ROCm version,
operating system, and Python version that are compatible with the ROCm
Finance libraries. Verify that your system includes an AMD GPU fully supported
by ROCm Finance. For guidance, see
`ROCm finance installation prerequisites <https://rocm.docs.amd.com/projects/rocm-finance-internal/en/latest/install/prerequisites.html>`__.

.. :ref:`ROCm Finance installation prerequisites <rocm-finance:system-requirements>`.

For a consistent and streamlined setup experience, it's recommended to use
a ROCm development environment Docker container. See
`Install ROCm Finance <https://rocm.docs.amd.com/projects/rocm-finance-internal/en/latest/install/install.html>`__ for instructions.

.. :ref:`Install ROCm Finance <rocm-finance:install-rocm-dev-docker>` for instructions.

Install ThunderGBM via pip
==========================

Install the ROCm-enabled ThunderGBM library from the AMD-hosted PyPI repository.

.. tab-set::

   .. tab-item:: ROCm 7.0
      :sync: rocm7

      .. code-block:: shell

         pip install thundergbm --index-url=https://pypi.amd.com/simple

   .. tab-item:: ROCm 6.4
      :sync: rocm6

      .. code-block:: shell

         pip install thundergbm --index-url=https://pypi.amd.com/simple

Verify your installation
------------------------

Use ``pip show`` to verify your installation:

.. code-block:: shell

   pip show -v thundergbm

.. dropdown:: Example output

   .. code-block:: shell-session

      Name: thundergbm
      Version: 0.3.16
      Summary: A Fast GBM Library on GPUs and CPUs
      ... [output truncated]

After installing ThunderGBM, import and use the library. For example:

.. code-block:: python

   from thundergbm import TGBMClassifier
   clf = TGBMClassifier()
