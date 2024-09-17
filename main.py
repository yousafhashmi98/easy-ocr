from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import easyocr
import os

from global_functions import write_file, convert_numpy_to_python

    
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
async def ocr_detection_easyocr(image_file:UploadFile = File(...)):
    file_path = write_file(file=image_file)
    if file_path == False:
        return None
    reader = easyocr.Reader(['en'], gpu=True)
    results = reader.readtext(file_path)
    if results:
        print(type(results),end="\n")
        print(f"Raw Results: {results}", end="\n")
        final_results = convert_numpy_to_python(results=results)
        print(f"Final Results: {final_results}", end="\n")
        os.remove(file_path)
        return final_results
    else:
        os.remove(file_path)
        return None

if __name__ == '__main__':
    uvicorn.run(app=app,host='localhost',port=9000)
