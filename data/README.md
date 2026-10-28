# Dataset setup

Do not commit the full VisDrone dataset to GitHub.

1. Download VisDrone2019-DET from its official source.
2. Convert annotations to YOLO format.
3. Arrange files under `images/train`, `images/val`, `labels/train`, and `labels/val`.
4. Update `visdrone.yaml` with the local dataset root.
5. Check the category-ID mapping carefully before training.

Original VisDrone annotations include bounding-box coordinates, score, category, truncation, and occlusion fields.
