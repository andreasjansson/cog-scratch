from cog import BaseModel, Path

class TrainingOutput(BaseModel):
    weights: Path
    lora: Path


def train() -> TrainingOutput:
    with open("weights.txt", "w") as f:
        f.write("i am the full weights")
    with open("lora.txt", "w") as f:
        f.write("i am the lora")

    return TrainingOutput(weights=Path("weights.txt"), lora=Path("lora.txt"))
