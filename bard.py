import google.generativeai as palm
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
palm_api_key = os.environ.get("PALM_API_KEY")

# Create a config.
palm.configure(api_key=palm_api_key)
model = palm.GenerativeModel(model_name="gemini-pro")
print(list(palm.list_models()))

# Generate some text.
def generate_itinerary(source, destination, start_date, end_date, no_of_day, budget, trip_type, transport_mode):
    """
    Generates a personalized trip itinerary based on the given parameters.

    Args:
        source (str): The starting location of the trip.
        destination (str): The destination location of the trip.
        start_date (str): The start date of the trip in YYYY-MM-DD format.
        end_date (str): The end date of the trip in YYYY-MM-DD format.
        no_of_day (int): The number of days for the trip.
        budget (str): The budget for the trip (optional).
        trip_type (str): The type of trip (e.g., solo, family, kids).
        transport_mode (str): The mode of transport (e.g., train, plane, bus, car, bike).

    Returns:
        str: The generated itinerary text with shopping suggestions.
    """
    prompt = (f"Generate a personalized trip itinerary for a {trip_type} trip from {source} to {destination} "
              f"starting on {start_date} and ending on {end_date}. The trip is {no_of_day} days long. "
              f"Consider the following details:\n"
              f"- Budget: {budget} INR\n"
              f"- Mode of Transport: {transport_mode}\n"
              f"Provide recommendations for activities, accommodations, travel tips, and places to shop. "
              f"Include suggestions on where to buy items and provide links to purchase them online (e.g., Bing Shopping).")
    
    # Generate the content based on the prompt
    response = model.generate_content(prompt)
    return response.text
