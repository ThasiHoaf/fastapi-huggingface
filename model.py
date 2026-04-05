import torch
from transformers import ViTImageProcessor, ViTForImageClassification
from omegaconf import OmegaConf
from PIL import Image

class ImageClassificationModel:
    def __init__(self, config_path: str):
        self.config = OmegaConf.load(config_path)
        self.processor = ViTImageProcessor.from_pretrained(self.config.model_path)
        self.model = ViTForImageClassification.from_pretrained(self.config.model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def predict(self, image: Image.Image) -> dict:
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        with torch.inference_mode():
            outputs = self.model(**inputs)
        
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        predicted_class_idx = logits.argmax(-1).item()
        confidence_score = probabilities[0, predicted_class_idx].item()
        predicted_label = self.model.config.id2label[predicted_class_idx]

        return {
            "predicted_class": predicted_label,
            "confidence": round(confidence_score, 4)
        }