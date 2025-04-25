Here's a professional `README.md` for your FastAPI-based Image Services project:

---

```markdown
# 🖼️ Image Services API

A FastAPI-based microservice for intelligent image processing. This service provides endpoints for:

- ✅ Background removal
- ✂️ Automatic face detection and cropping
- 📸 Biometric passport photo generation (custom size)

---

## 🚀 Features

- 🔄 Remove background using [rembg](https://github.com/danielgatis/rembg)
- 🤖 Auto-crop face from image using [autocrop](https://github.com/leblancfg/autocrop)
- 📏 Generate passport photo with specified dimensions using [photoidmagick](https://github.com/majormode/photoidmagick)
- 🧪 Built with [FastAPI](https://fastapi.tiangolo.com/) for high-performance APIs

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/image-services-api.git
cd image-service

# (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🛠️ API Endpoints

### 1. `/remove-bg/`
**POST** – Removes background from an uploaded image.

- **Form Data**:
  - `file`: Image file (JPG, PNG, etc.)

**Example using `curl`:**
```bash
curl -X POST "http://localhost:8000/remove-bg/" -F "file=@your_image.jpg" --output no_bg.png
```

---

### 2. `/auto-crop-passport-size/`
**POST** – Automatically crops image to face using face detection.

- **Form Data**:
  - `file`: Image file (supported extensions listed in code)

**Returns**: Cropped image with face centered.

---

### 3. `/crop-passport-photo/`
**POST** – Creates biometric passport photo with custom dimensions.

- **Form Data**:
  - `file`: Image file (JPG, JPEG, PNG)
- **Query Parameters**:
  - `width`: Width in pixels
  - `height`: Height in pixels

**Example using `curl`:**
```bash
curl -X POST "http://localhost:8000/crop-passport-photo/?width=600&height=600" \
  -F "file=@your_photo.jpg" --output passport_photo.jpg
```

---

## 📁 Project Structure

```
/app
│
├── main.py
├── requirements.txt
├── routes
│   ├── background_removal.py
│   ├── auto_crop.py
│   └── passport_photo_crop.py
├── services
│   ├── background_removal_service.py
│   ├── auto_crop_service.py
│   └── passport_photo_crop_service.py
└── utils
    └── file_validation.py
```

---

## 🧪 Run the App

```bash
uvicorn main:app --reload
```

Access docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 👨‍💻 Author

Built with ❤️ by [Rajnish-Kumar](https://github.com/shramarajnishkumar/)

```