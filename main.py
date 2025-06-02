from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
from app.utils.preprocessing import preprocess_input
from schemas import PersonalityInput

app = FastAPI()

# Setup Jinja2 templates folder
templates = Jinja2Templates(directory="app/template")

# Load saved model and label encoder once
model = joblib.load("Model/random_forest_model.pkl")
label_encoder = joblib.load("Model/personality_label_encoder.pkl")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict_personality(
    request: Request,
    Time_spent_Alone: float = Form(...),
    Stage_fear: str = Form(...),
    Social_event_attendance: float = Form(...),
    Going_outside: float = Form(...),
    Drained_after_socializing: str = Form(...),
    Friends_circle_size: int = Form(...),
    Post_frequency: float = Form(...)
):
    # Collect form data into dict
    form_data = {
        "Time_spent_Alone": Time_spent_Alone,
        "Stage_fear": Stage_fear,
        "Social_event_attendance": Social_event_attendance,
        "Going_outside": Going_outside,
        "Drained_after_socializing": Drained_after_socializing,
        "Friends_circle_size": Friends_circle_size,
        "Post_frequency": Post_frequency
    }

    try:
        # Validate using Pydantic schema (optional, but recommended)
        validated_data = PersonalityInput(**form_data)
    except Exception as e:
        return templates.TemplateResponse("form.html", {"request": request, "error": f"Input validation error: {str(e)}"})

    # Preprocess data
    input_df = preprocess_input(form_data)

    # Predict using the model
    pred_encoded = model.predict(input_df)[0]

    # Decode the prediction label
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]

    # Return form with result
    return templates.TemplateResponse("form.html", {"request": request, "result": f"Predicted Personality: {pred_label}"})
