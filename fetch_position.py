import requests
import json
from google.transit import gtfs_realtime_pb2


VEHICLE_POSITION_URL = "https://testraildata.njtransit.com/api/GTFSRT/getVehiclePositions"

def fetch_vehicle_positions(token):
    response = requests.post(
        VEHICLE_POSITION_URL,
        files={"token": (None, token)},
        headers = {"accept": "*/*"}
    )

    return response.content

def parse_vehicle_positions(proto_data):
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(proto_data)
    
    vehicles = []
    for entity in feed.entity:
        if entity.HasField("vehicle"):
            v =  entity.vehicle
            vehicles.append({
                "vehicle_id": v.vehicle.id,
                "route_id": v.trip.route_id,
                "latitude": v.position.latitude,
                "longitude": v.position.longitude,
                "timestamp": v.timestamp,
                "occupancy_status": v.occupancy_status,
            })
    return vehicles

def main():
    with open("token.txt", "r") as f:
        token = f.read().strip()


    proto_data = fetch_vehicle_positions(token)
    vehicles = parse_vehicle_positions(proto_data)

    with open("train_positions.json", "w") as f:
        json.dump(vehicles, f, indent = 2)

    print ("Train positions saved.")


if __name__ == "__main__":
    main()