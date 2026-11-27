from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient


def get_resource_details(resource_id):

    parts = resource_id.strip("/").split("/")

    subscription_id = parts[1]
    resource_group = parts[3]

    credential = DefaultAzureCredential()

    client = ResourceManagementClient(
        credential,
        subscription_id
    )

    resource = client.resources.get_by_id(
        resource_id,
        api_version="2024-07-01"
    )

    resource_details = {
        "name": resource.name,
        "resource_id": resource.id,
        "resource_type": resource.type,
        "resource_group": resource_group,
        "region": resource.location
    }

    return resource_details
