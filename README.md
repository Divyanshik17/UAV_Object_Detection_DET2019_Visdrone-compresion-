# UAV Object Detection on VisDrone2019-DET

Research starter repository for lightweight UAV/aerial object detection using YOLO11n and VisDrone2019-DET.

> This is a GitHub-ready starter scaffold. Add your verified custom model code and final experiment results before describing it as your completed modified model. Do not upload the dataset itself unless redistribution is permitted.

## Project overview
- Prepare VisDrone annotations in YOLO format.
- Train and evaluate a YOLO11n baseline.
- Compare a modified detector with the baseline under the same settings.
- Report precision, recall, mAP@50, mAP@50–95, model size, and inference speed.

## Dataset
Expected converted layout:

```text
data/VisDrone_YOLO/
├── images/train/
├── images/val/
├── labels/train/
├── labels/val/
└── data.yaml
```

Dataset used in the project: 6,471 training images, 548 validation images, and 10 classes. The dataset is not included in this repository. Obtain it from the official VisDrone source and follow its terms.

## Setup
Python 3.10 or 3.11 is recommended.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

## Train
Update `data/visdrone.yaml` with the correct local dataset path, then run:

```bash
python scripts/train.py --data data/visdrone.yaml --epochs 100 --imgsz 640 --batch 8
```

## Evaluate
```bash
python scripts/evaluate.py --weights runs/detect/visdrone_yolo11n/weights/best.pt --data data/visdrone.yaml --imgsz 640
```

## Predict
```bash
yolo predict model=runs/detect/visdrone_yolo11n/weights/best.pt source=path/to/image_or_folder imgsz=640
```

## Export to ONNX
```bash
python scripts/export_onnx.py --weights runs/detect/visdrone_yolo11n/weights/best.pt --imgsz 640
```

## Structure
```text
├── data/       # Dataset config and setup instructions
├── docs/       # Experiment log template
├── models/     # Custom model YAML files
├── notebooks/  # Dataset analysis and experiment notebooks
├── scripts/    # Train, evaluate, export
├── src/        # Custom modules and utilities
├── results/    # Lightweight plots and metrics
├── requirements.txt
└── .gitignore
```

## Results table
Fill this table only with results from verified runs.

| Model | Epochs | Image size | Precision | Recall | mAP@50 | mAP@50–95 | FPS |
|---|---:|---:|---:|---:|---:|---:|---:|
| YOLO11n baseline | — | — | — | — | — | — | — |
| Modified YOLO11n | — | — | — | — | — | — | — |

## Recommended experiment protocol
1. Use the same dataset split and training settings for baseline and modified models.
2. Record epochs, image size, batch size, seed, hardware, and software versions.
3. Add an ablation study for each architectural change.
4. Report per-class AP and inspect failure cases.
5. Measure FPS on the same hardware and inference settings.

## Citation
Cite the VisDrone dataset, Ultralytics/YOLO, and all papers whose ideas or code informed your work. Add a license after deciding how your code may be reused; third-party licenses remain separate.
