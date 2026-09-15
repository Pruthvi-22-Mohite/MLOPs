# Assignment 1: Dataset Versioning

This assignment demonstrates dataset versioning with DVC. The working project is
in [DatasetVersioning](DatasetVersioning/README.md), and the local DVC remote is
in [dvc-storage](dvc-storage/README.md).

## Workflow

1. Enter `DatasetVersioning`.
2. Use the DVC metadata in `.dvc` to track `data/student.csv`.
3. Run `dvc pull` or `dvc checkout` when restoring the tracked dataset.
4. Use `dvc status` to inspect data changes.

The assignment brief is stored in `32_AIDS_D_MLOps_Assignment1.pdf`.