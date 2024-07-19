# orientation-filter
Filter particles by stable orientation across refinements.

Takes `.star` from Relion >= 3.1 as input. Should be at least three runs of `Refine3D` with the sample particle set and the same reference. 

1. Clone GitHub repository
2. Best to create a fresh conda/mamba environment, e.g. via `mamba create -f requirements.yml`.
3. Otherwise, check `requirements.yml` and install required packages manually.
4. Launch `jupyter lab`.
5. Follow the steps in `orientation-filter.ipynb`.