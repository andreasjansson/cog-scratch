# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from typing import Optional
from cog import BasePredictor, Input, Path


class Predictor(BasePredictor):
    def setup(self, weights: Optional[Path] = None) -> None:
        """Load the model into memory to make running multiple predictions efficient"""
        self.weights = weights

    def predict(
        self,
        prefix: str = Input(description="Text to prefix output with"),
        __weights: Path = Input(default=None),
    ) -> str:
        """Run a single prediction on the model"""

        print(__weights)

        output = prefix + "\n"
        if self.weights:
            with self.weights.open() as f:
                output += f.read() + "\n"
        if __weights:
            with __weights.open() as f:
                output += f.read() + "\n"

        return output
