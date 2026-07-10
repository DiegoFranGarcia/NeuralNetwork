from pathlib import Path

from PIL import Image
from torch.utils.data import Dataset


class CatDogDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = Path(root_dir)
        self.transform = transform
        self.class_to_label = {"cats": 0, "dogs": 1}
        self.samples = []

        for class_name in ["cats", "dogs"]:
            class_dir = self.root_dir / class_name
            if not class_dir.exists():
                continue

            for file_path in sorted(class_dir.iterdir()):
                if file_path.is_file() and file_path.suffix.lower() in {
                    ".jpg",
                    ".jpeg",
                    ".png",
                }:
                    self.samples.append((file_path, self.class_to_label[class_name]))

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]
        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
