from app.resource_client import get_resource_details


resource_id = (
    "/subscriptions/df05ac71-5d40-4c99-9789-aa269970a25f"
    "/resourceGroups/peru-main-rg"
    "/providers/Microsoft.Compute/virtualMachines/ubuntu-testvm01"
)


resource = get_resource_details(resource_id)


print("Azure Resource Details")
print("======================")

print(f"Name           : {resource['name']}")
print(f"Resource Type  : {resource['resource_type']}")
print(f"Resource Group : {resource['resource_group']}")
print(f"Region         : {resource['region']}")
print(f"Resource ID    : {resource['resource_id']}")
