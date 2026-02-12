from __future__ import annotations

from io import BytesIO

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import Response
from PIL import Image
from rembg import remove

app = FastAPI(title="kyliescloset-bg")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/remove-bg")
async def remove_bg(file: UploadFile = File(...)):
    """
    Accepts an uploaded image and returns a transparent PNG (image/png).
    """
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported file type. Upload an image.")

    try:
        raw = await file.read()
        if not raw:
            raise HTTPException(status_code=400, detail="Empty upload.")

        # rembg outputs bytes; can be PNG bytes with alpha
        out_bytes = remove(raw)

        # Validate output is readable as an image; enforce PNG output
        img = Image.open(BytesIO(out_bytes)).convert("RGBA")
        buf = BytesIO()
        img.save(buf, format="PNG")
        png_bytes = buf.getvalue()

        # "Download behavior": set Content-Disposition as attachment
        filename_base = (file.filename or "image").rsplit(".", 1)[0]
        download_name = f"{filename_base}-nobg.png"

        return Response(
            content=png_bytes,
            media_type="image/png",
            headers={
                "Content-Disposition": f'attachment; filename="{download_name}"'
            },
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Background removal failed: {e}")