"""
MVTec AD Dataset Downloader
============================
Anomalib library use කරලා MVTec AD dataset (Bottle category)
automatically download කරන script එකක්.

License: MVTec AD - CC BY-NC-SA 4.0 (Non-commercial research only)
"""

from pathlib import Path
from anomalib.data import MVTec

# Dataset save කරන folder
RAW_DATA_DIR = Path(__file__).parent.parent / "raw"
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 50)
print("DEFECTRA - MVTec AD Dataset Downloader")
print("=" * 50)
print(f"Download location: {RAW_DATA_DIR.resolve()}")
print("Category: bottle")
print("Please wait...")
print()

try:
    # Anomalib MVTec datamodule use කරලා download කරනවා
    datamodule = MVTec(
        root=str(RAW_DATA_DIR),
        category="bottle",
        image_size=(256, 256),
        train_batch_size=32,
        eval_batch_size=32,
        num_workers=0,
    )

    # Download trigger කරනවා
    datamodule.prepare_data()

    print()
    print("=" * 50)
    print("✅ Dataset downloaded successfully!")
    print(f"📁 Location: {RAW_DATA_DIR / 'bottle'}")
    print("=" * 50)

except Exception as e:
    print(f"❌ Error: {e}")
    print()
    print("Alternative: Kaggle ලේ manually download කරන්න:")
    print("https://www.kaggle.com/datasets/ipythonx/mvtec-ad")
