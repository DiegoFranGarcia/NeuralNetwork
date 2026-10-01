from pathlib import Path

from PIL import Image
from torch.utils.data import Dataset


class CatDogDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = Path(root_dir)
        self.transform = transform
        self.samples = []

        for class_name, label in ("cats", 0), ("dogs", 1):
            class_dir = self.root_dir / class_name
            if not class_dir.exists():
                continue

            for image_path in sorted(class_dir.iterdir()):
                if image_path.is_file() and image_path.suffix.lower() in {".jpg", ".jpeg", ".png"}:
                    self.samples.append((image_path, label))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        image_path, label = self.samples[idx]
        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
