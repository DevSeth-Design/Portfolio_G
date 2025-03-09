from fastapi import APIRouter, HTTPException, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from pydantic import BaseModel, EmailStr, Field
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

limiter = Limiter(key_func=get_remote_address, default_limits=["5 per minute", "1 per second"])
app = FastAPI()
router = APIRouter()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your Vite dev server
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],  
    allow_headers=["Content-Type", "Authorization"],  
    max_age=600, # 10 minutes
)

class ContactForm(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: str = Field(..., pattern=r"^\+?\d{10,15}$")  
    title: str = Field(..., min_length=3, max_length=100)
    message: str = Field(..., min_length=10, max_length=1000)

@app.get("/")
async def root():
    return {"message": "Server is running!"}

def send_email(contact_form: ContactForm):
    sender_email = os.getenv("SMTP_EMAIL")  # Your new sender email
    sender_password = os.getenv("SMTP_PASSWORD")  # App password for email
    recipient_email = os.getenv("RECIPIENT_EMAIL")  # Where the form should be sent

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = f"New Contact Form Submission: {contact_form.title}"

        body = f"""
        Name: {contact_form.name}
        Email: {contact_form.email}
        Phone: {contact_form.phone}

        Message:
        {contact_form.message}
        """

        msg.attach(MIMEText(body, "plain"))

        # ✅ Connect to SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Change this if not using Gmail
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()

        print("✅ Email sent successfully!")
        return {"message": "Email sent"}
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        raise HTTPException(status_code=500, detail="Failed to send email")

@router.post("/contact")
async def send_contact_form(contact_form: ContactForm):
    try:
        send_email(contact_form)
        print(f"Sending email to {contact_form.email}")
        return {"message": "Email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=2)