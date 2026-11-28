from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequest


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

def find_vm_by_name(vm_name, subscription_ids):

    credential = DefaultAzureCredential()

    client = ResourceGraphClient(
        credential=credential
    )

    query = f"""
    Resources
    | where type =~ 'Microsoft.Compute/virtualMachines'
    | where name =~ '{vm_name}'
    | project name, id, type, resourceGroup, subscriptionId, location
    """

    request = QueryRequest(
        subscriptions=subscription_ids,
        query=query
    )

    response = client.resources(request)

    matches = []

    for resource in response.data:

        matches.append({
            "name": resource["name"],
            "resource_id": resource["id"],
            "resource_type": resource["type"],
            "resource_group": resource["resourceGroup"],
            "subscription_id": resource["subscriptionId"],
            "region": resource["location"]
        })

    return matches
