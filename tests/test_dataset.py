from PIL import Image
from torchvision import transforms

from src.dataset import CatDogDataset


def test_catdogdataset_loads_images_and_labels(tmp_path):
    cats_dir = tmp_path / "cats"
    dogs_dir = tmp_path / "dogs"
    cats_dir.mkdir()
    dogs_dir.mkdir()

    cat_image_path = cats_dir / "cat_1.jpg"
    dog_image_path = dogs_dir / "dog_1.jpg"

    Image.new("RGB", (10, 10), color="blue").save(cat_image_path)
    Image.new("RGB", (10, 10), color="red").save(dog_image_path)

    dataset = CatDogDataset(tmp_path)

    assert len(dataset) == 2

    image_0, label_0 = dataset[0]
    image_1, label_1 = dataset[1]

    assert label_0 in {0, 1}
    assert label_1 in {0, 1}
    assert {label_0, label_1} == {0, 1}
    assert image_0.mode == "RGB"
    assert image_1.mode == "RGB"


def test_catdogdataset_applies_transform(tmp_path):
    cats_dir = tmp_path / "cats"
    cats_dir.mkdir()
    image_path = cats_dir / "cat_1.jpg"
    Image.new("RGB", (10, 10), color="green").save(image_path)

    transform = transforms.Resize((5, 5))
    dataset = CatDogDataset(tmp_path, transform=transform)

    image, label = dataset[0]

    assert image.size == (5, 5)
    assert label == 0
