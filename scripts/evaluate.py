import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="Evaluate a trained YOLO detector.")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--data", required=True, help="Path to dataset YAML.")
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--device", default="", help="For example: 0 or cpu.")
    args = parser.parse_args()

    model = YOLO(args.weights)
    metrics = model.val(
        data=args.data,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device or None,
    )
    print(metrics.results_dict)

if __name__ == "__main__":
    main()
