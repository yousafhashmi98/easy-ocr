from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import easyocr

    
app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "server is running"}

@app.post("/process-image")
async def ocr_detection_easyocr(imgpath):
    reader = easyocr.Reader(['en'], gpu=True)  # Specify the language(s) you need
    results = reader.readtext(imgpath)
    
    if results:
        return results
    else:
        return None

if __name__ == '__main__':
    uvicorn.run(app=app,host='localhost',port=9000)
