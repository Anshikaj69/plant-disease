
from supabase import create_client, Client


supabase_url = "https://voegxfwsqodrciwtmzja.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZvZWd4ZndzcW9kcmNpd3RtemphIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg2MTg5NDQsImV4cCI6MjAyNDE5NDk0NH0.ehmK8XoKtps8XSThBpzg74DvIrnQS6P8CaGCFMSlnLg"

# Initialize Supabase client
supabase : Client = create_client(supabase_url, supabase_key)

def user_signup(uemail, upassword):
    res = supabase.auth.sign_up({
    "email" : uemail,
    "password" :upassword})
    return res
    
def user_signin(email, password):
    res= supabase.auth.sign_in_with_password({"email": email, "password": password})
    return res