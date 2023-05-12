from flask import Flask, render_template
from azure.signalr import ConnectionString, SignalRServiceConnection
import os

app = Flask(__name__)

# Configure Azure SignalR
connection_string = os.environ.get("AzureSignalRConnectionString")
service_connection = SignalRServiceConnection(connection_string)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/telemetry")
def telemetry():
    request.headers.add("Access-Control-Allow-Origin", "*")
    return service_connection.create_streaming_response("telemetry")

if __name__ == "__main__":
    app.run()
