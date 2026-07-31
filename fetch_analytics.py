import os
import json
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

def fetch_analytics_data():
    property_id = os.environ.get("547983690")
    if not property_id:
        print("Error: GA_PROPERTY_ID environment variable not set.")
        return

    try:
        # Client uses credentials from GOOGLE_APPLICATION_CREDENTIALS env var
        client = BetaAnalyticsDataClient()

        # Query Profile Views (page_view) and Downloads (file_download)
        # Adjust metrics and dimensions based on your actual GA4 setup.
        # This is a generic example fetching total users, event counts for specific events.
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name="eventName")],
            metrics=[Metric(name="eventCount")],
            date_ranges=[DateRange(start_date="30daysAgo", end_date="today")],
        )
        response = client.run_report(request)

        stats = {
            "profile_views": 0,
            "events": 0,
            "downloads": 0
        }

        for row in response.rows:
            event_name = row.dimension_values[0].value
            count = int(row.metric_values[0].value)
            
            if event_name == "page_view":
                stats["profile_views"] += count
            elif event_name == "file_download":
                stats["downloads"] += count
            
            stats["events"] += count

        # Write to stats.json
        with open("stats.json", "w") as f:
            json.dump(stats, f, indent=2)
            
        print("Successfully updated stats.json")

    except Exception as e:
        print(f"Failed to fetch analytics: {e}")

if __name__ == "__main__":
    fetch_analytics_data()
