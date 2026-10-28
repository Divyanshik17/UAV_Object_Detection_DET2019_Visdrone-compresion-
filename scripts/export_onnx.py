import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser(description="Export a trained YOLO model to ONNX.")
    parser.add_argument("--weights", required=True)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--dynamic", action="store_true")
    args = parser.parse_args()

    model = YOLO(args.weights)
    output = model.export(format="onnx", imgsz=args.imgsz, dynamic=args.dynamic)
    print(f"Exported model: {output}")

if __name__ == "__main__":
    main()
