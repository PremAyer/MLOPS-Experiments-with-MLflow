import mlflow
print("Tracking URI:")
print(mlflow.get_tracking_uri())
print("\n")

mlflow.set_tracking_uri("https://127.0.0.1:5000")
print("New Trackign URI:")
print(mlflow.get_tracking_uri())
