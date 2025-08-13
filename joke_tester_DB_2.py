import os
import random
from supabase import create_client, Client
from dotenv import load_dotenv
from flask import Flask, jsonify

# Load credentials from .env
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route('/joke', methods=['GET'])
def get_random_joke():
    # Fetch all jokes (for small tables), or use pg random
    response = supabase.table("jokes").select("*").execute()
    jokes = response.data
    if not jokes:
        return jsonify({"error": "No jokes found"}), 404

    joke = random.choice(jokes)
    return jsonify(joke)

if __name__ == '__main__':
    app.run(debug=True)
