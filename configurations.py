import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2

all_configs = {
    "common": {
        "DEVICE": "cuda" if torch.cuda.is_available() else "cpu",
        # "NUM_WORKERS" : 2,
        "CHANNELS_IMG": 3,
        "L1_LAMBDA": 100,
        "LOAD_MODEL": True,
        "SAVE_MODEL": True,
        "SAVE_FOLDER": "saved_models",
        "EVALUATE_FOLDER": "evaluate",
        "CHECKPOINT_DISC": "latest_n_disc.pth.tar",
        "CHECKPOINT_GEN": "latest_n_gen.pth.tar",
        "TRAIN_FLIP": False
    },
    "maps": {
        "TRAIN_DIR": "data/maps/train",
        "VAL_DIR": "data/maps/val",
        "SAMPLES": "samples/maps",
        "LEARNING_RATE": 2e-4,
        "BATCH_SIZE": 16,
        "IMAGE_SIZE": 256,
        "IMAGE_LENGTH": 1200,
        "IMAGE_SPLIT_POS": 600,
        "NUM_EPOCHS": 200,
        "both_transform": A.Compose([A.Resize(width=256, height=256), ], additional_targets={"image0": "image"}),
        "transform_only_input": A.Compose(
            [
                A.HorizontalFlip(p=0.5),
                # A.ColorJitter(p=0.2),
                A.Normalize(mean=[0.5, 0.5, 0.5], std=[
                            0.5, 0.5, 0.5], max_pixel_value=255.0,),
                ToTensorV2(),
            ]
        ),
        "transform_only_mask": A.Compose(
            [
                A.Normalize(mean=[0.5, 0.5, 0.5], std=[
                            0.5, 0.5, 0.5], max_pixel_value=255.0,),
                ToTensorV2(),
            ]
        )
    },
    "facades": {
        "TRAIN_DIR": "data/facades/train",
        "VAL_DIR": "data/facades/test",
        "SAMPLES": "samples/maps",
        "LEARNING_RATE": 2e-4,
        "BATCH_SIZE": 16,
        "IMAGE_SIZE": 256,
        "IMAGE_LENGTH": 512,
        "IMAGE_SPLIT_POS": 256,
        "NUM_EPOCHS": 200,
        "TRAIN_FLIP": True,
        "both_transform": A.Compose([A.Resize(width=256, height=256), ], additional_targets={"image0": "image"}),
        "transform_only_input": A.Compose(
            [
                A.HorizontalFlip(p=0.5),
                # A.ColorJitter(p=0.2),
                A.Normalize(mean=[0.5, 0.5, 0.5], std=[
                            0.5, 0.5, 0.5], max_pixel_value=255.0,),
                ToTensorV2(),
            ]
        ),
        "transform_only_mask": A.Compose(
            [
                A.Normalize(mean=[0.5, 0.5, 0.5], std=[
                            0.5, 0.5, 0.5], max_pixel_value=255.0,),
                ToTensorV2(),
            ]
        )
    }
}