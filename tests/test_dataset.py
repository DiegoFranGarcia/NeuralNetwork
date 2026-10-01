from pathlib import Path

from PIL import Image

from src.dataset import CatDogDataset


def test_catdogdataset_loads_images_and_labels(tmp_path):
    cat_dir = tmp_path / "cats"
    dog_dir = tmp_path / "dogs"
    cat_dir.mkdir()
    dog_dir.mkdir()

    Image.new("RGB", (10, 10), color="white").save(cat_dir / "cat1.jpg")
    Image.new("RGB", (10, 10), color="black").save(dog_dir / "dog1.png")

    dataset = CatDogDataset(tmp_path)

    assert len(dataset) == 2

    first_image, first_label = dataset[0]
    second_image, second_label = dataset[1]

    assert first_image.size == (10, 10)
    assert second_image.size == (10, 10)
    assert {first_label, second_label} == {0, 1}


def test_catdogdataset_applies_transform(tmp_path):
    cat_dir = tmp_path / "cats"
    cat_dir.mkdir()

    Image.new("RGB", (8, 8), color="white").save(cat_dir / "cat1.jpg")

    def to_size(image):
        return image.resize((4, 4))

    dataset = CatDogDataset(tmp_path, transform=to_size)

    image, label = dataset[0]

    assert image.size == (4, 4)
    assert label == 0


def test_catdogdataset_ignores_non_image_files(tmp_path):
    cat_dir = tmp_path / "cats"
    dog_dir = tmp_path / "dogs"
    cat_dir.mkdir()
    dog_dir.mkdir()

    Image.new("RGB", (10, 10), color="white").save(cat_dir / "cat1.jpg")
    (dog_dir / "notes.txt").write_text("not an image")

    dataset = CatDogDataset(tmp_path)

    assert len(dataset) == 1
