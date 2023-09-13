import multiprocessing

bind = "0.0.0.0:8000"  # Bind the application to this address and port

# Number of worker processes to spawn
workers = multiprocessing.cpu_count() * 2 + 1

# Module name of the Flask application
# Make sure this matches the name used in your `application.py` file
module_name = "app"

# Name of the callable within the Flask application
callable_name = "app"