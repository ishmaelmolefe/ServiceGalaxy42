from api_client import get_cars
import logging

# Updated service.py
def search_car_availability(token, make, model):
    """Search for a car across all pages."""
    page = 1
    limit = 10  # Match default from api_client.get_cars
    
    try:
        while True:
            cars_data = get_cars(token, page=page, limit=limit)
            cars_list = cars_data.get("cars", [])
            
            if not cars_list:
                break  # No more results
                
            for car in cars_list:
                if (
                    car["make"].lower() == make.lower()
                    and car["model"].lower() == model.lower()
                ):
                    return car["available"]
            
            page += 1  # Check next page
            
    except Exception as e:
        logging.error("Error during search", exc_info=True)
        raise
    
    return False  # Car not found