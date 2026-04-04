from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image, UnidentifiedImageError
import io
from model import ImageClassificationModel

app = FastAPI(
    title="Computer Vision API",
    description="Hệ thống phân loại hình ảnh sử dụng mô hình Vision Transformer (ViT) từ Hugging Face."
)

try:
    classifier = ImageClassificationModel("config.yaml")
except Exception as e:
    classifier = None
    print(f"Lỗi khởi tạo mô hình: {e}")

# Yêu cầu 1: GET / [cite: 38]
@app.get("/")
async def root():
    return {
        "system": "Computer Vision API - Image Classification",
        "description": "API phân loại hình ảnh sử dụng google/vit-base-patch16-224",
        "endpoints": ["/", "/health", "/predict"]
    }

# Yêu cầu 2: GET /health [cite: 39]
@app.get("/health")
async def health_check():
    if classifier is None:
        raise HTTPException(status_code=503, detail="Mô hình chưa sẵn sàng hoạt động.")
    return {"status": "ok", "model_loaded": True}

# Yêu cầu 3: POST /predict [cite: 40, 42, 43]
@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    # Bắt lỗi định dạng cơ bản [cite: 44, 45]
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Vui lòng tải lên tệp định dạng hình ảnh (JPEG/PNG).")
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Tệp bị hỏng hoặc không phải là hình ảnh hợp lệ.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi I/O nội bộ: {str(e)}")

    try:
        result = classifier.predict(image)
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi quá trình suy luận: {str(e)}")