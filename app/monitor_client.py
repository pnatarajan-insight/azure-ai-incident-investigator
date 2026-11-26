from datetime import timedelta

from azure.identity import DefaultAzureCredential
from azure.monitor.querymetrics import MetricsClient

def get_vm_cpu_metrics(resource_id, region):

    credential = DefaultAzureCredential()

    endpoint = f"https://{region}.metrics.monitor.azure.com"

    client = MetricsClient(
        endpoint,
        credential
    )

    response = client.query_resources(
        resource_ids=[resource_id],
        metric_namespace="Microsoft.Compute/virtualMachines",
        metric_names=["Percentage CPU"],
        timespan=timedelta(hours=1),
        granularity=timedelta(minutes=5),
        aggregations=["Average"]
    )

    cpu_values = []

    for result in response:
        for metric in result.metrics:
            for time_series in metric.timeseries:
                for data in time_series.data:

                    if data.average is not None:

                        cpu_values.append({
                            "timestamp": data.timestamp,
                            "average_cpu": data.average
                        })

    return cpu_values
