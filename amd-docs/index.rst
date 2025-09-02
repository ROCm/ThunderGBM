.. meta::
   :description: Use ThunderGBM with ROCm support on AMD GPUs
   :keywords: amd, rocm, finance, financial, fintech, algorithm, gpu

************************
ThunderGBM documentation
************************

With ThunderGBM on ROCm, you can run GPU‑accelerated gradient boosting on AMD
Instinct GPUs, enabling fast, scalable machine learning for high-velocity financial
applications such as real-time fraud detection on sparse transaction data.

ThunderGBM uses atomic operations and approximate algorithms to optimize for
billion-scale datasets. It excels on sparse, high‑dimensional inputs (such as
400+ features and many zeros), achieving 10x to 20x performance gains through GPU
acceleration with low‑latency predictions. Note that accuracy might dip slightly
(approximately 1%), but this trade‑off is negligible for speed‑critical scoring
workloads.

ROCm enablement fully accelerates ThunderGBM on AMD Instinct GPUs through
optimized kernels, efficient memory management, and seamless multi‑GPU scaling,
delivering substantial performance gains over CPU‑only baselines on massive,
sparse datasets common in financial systems.

ThunderGBM is part of the `ROCm-Finance toolkit
<https://rocm.docs.amd.com/projects/rocm-finance/en/latest/>`__.

The ROCm-Finance ThunderGBM source code is hosted on GitHub at
`<https://github.com/ROCm/ThunderGBM/>`__.

ROCm-Finance ThunderGBM documentation is organized into the following categories:

.. grid:: 2
   :gutter: 3

   .. grid-item-card:: Install

      * :doc:`/install/install`
      * :doc:`/install/build-from-source`

   .. grid-item-card:: Reference

      * `Documentation (upstream) <https://github.com/Xtra-Computing/thundergbm/blob/master/docs/index.md>`__

   .. grid-item-card:: Tutorial

      * `Examples (GitHub) <https://github.com/ROCm/rocm-finance/tree/main/examples/thundergbm>`__
