.. meta::
   :description: Use ThunderGBM with ROCm support on AMD GPUs
   :keywords: amd, rocm, finance, financial, fintech, algorithm, gpu

*****************************
ROCm ThunderGBM documentation
*****************************

With ThunderGBM on ROCm, you can run GPU‑accelerated gradient boosting on AMD
hardware, enabling fast, scalable machine learning for high-velocity financial
applications such as real-time fraud detection on sparse transaction data.

ThunderGBM uses atomic operations and approximate algorithms to optimize for
billion-scale datasets. It excels on sparse, high‑dimensional inputs (such as
400+ features and many zeros), achieving 10x to 20x performance gains through GPU
acceleration with low‑latency predictions. Note that accuracy might dip slightly
(approximately 1%), but this trade‑off is negligible for speed‑critical scoring
workloads.

ROCm enablement fully accelerates ThunderGBM on AMD GPUs through optimized kernels,
efficient memory management, and seamless multi‑GPU scaling, delivering
substantial performance gains over CPU‑only baselines on massive, sparse
datasets common in financial systems.

The ROCm ThunderGBM source code is hosted on GitHub at
`<https://github.com/ROCm-Finance/ThunderGBM/>`__.

.. ThunderGBM is part of the ROCm Finance Domain SDK :doc:`<rocm-finance:index>`.

ThunderGBM is part of the `ROCm Finance SDK <https://rocm.docs.amd.com/projects/rocm-finance-internal/en/latest/>`__.

ROCm LightGBM documentation is organized into the following categories:

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: Install

      * :doc:`/install/install`
      * :doc:`/install/build-from-source`

   .. grid-item-card:: Reference

      * `Documentation (upstream) <https://github.com/Xtra-Computing/thundergbm/blob/master/docs/index.md>`__

   .. grid-item-card:: Tutorial

      * `Examples (GitHub) <https://github.com/AMD-AIOSS/rocm-finance/tree/main/examples/thundergbm>`__
