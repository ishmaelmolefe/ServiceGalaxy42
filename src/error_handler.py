def handle_api_error(error):
    return {"error": str(error), "message": "Failed to fetch data from API"}
