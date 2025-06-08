# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)


# @app.route('/classify_image', methods=['GET', 'POST'])
# def classify_image():
#     image_data = request.form['image_data']

#     response = jsonify(util.classify_image(image_data))

#     response.headers.add('Access-Control-Allow-Origin', '*')

#     return response

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Sports Celebrity Image Classification")
#     util.load_saved_artifacts()
#     app.run(port=5000)






from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from util import CelebrityClassifier

app = FastAPI()
model = CelebrityClassifier()

# Allow CORS (Cross-Origin requests from browser frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify ["http://localhost:8000"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/classify_image")
async def classify_image(image_data: str = Form(...)):
    """
    Accept base64-encoded image string via form data.
    """
    result = model.classify_image(image_base64_data=image_data)
    return JSONResponse(content=result)

@app.on_event("startup")
def load_model():
    """
    Load the model and artifacts at startup.
    """
    print("Starting FastAPI Server for Sports Celebrity Image Classification...")
    model.load_saved_artifacts()