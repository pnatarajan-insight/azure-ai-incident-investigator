from app.monitor_client import get_vm_cpu_metrics


resource_id = (
    "/subscriptions/df05ac71-5d40-4c99-9789-aa269970a25f"
    "/resourceGroups/peru-main-rg"
    "/providers/Microsoft.Compute/virtualMachines/ubuntu-testvm01"
)

region = "eastus"


cpu_metrics = get_vm_cpu_metrics(
    resource_id,
    region
)


print("Azure VM CPU Metrics")
print("====================")

if not cpu_metrics:
    print("No CPU metric data returned.")

else:
    for metric in cpu_metrics:
            print(
        f"{metric['timestamp']} "
        f"CPU: {metric['average_cpu']:.2f}%"
    )
