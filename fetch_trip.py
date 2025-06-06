import requests
import json
from google.transit import gtfs_realtime_pb2

GET_TRIP_URL = "https://testraildata.njtransit.com/api/GTFSRT/getTripUpdates"

def fetch_trip(token):
    response = requests.post(
        GET_TRIP_URL,
        files = {"token": (None, token)},
        headers = {"accept": "*/*"}
    )

    return response.content

def parse_trip(proto_data):
    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(proto_data)
    print(feed)


def main():
    with open("token.txt", "r") as f:
        token = f.read().strip()

    proto_data = fetch_trip(token)
    feed = parse_trip(proto_data)


if __name__ == "__main__":
    main()