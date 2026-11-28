from app.resource_client import find_vm_by_name


vm_name = "ubuntu-testvm01"

subscription_ids = [
    "df05ac71-5d40-4c99-9789-aa269970a25f"
]


matches = find_vm_by_name(
    vm_name,
    subscription_ids
)


print("Azure VM Resource Discovery")
print("===========================")


if len(matches) == 0:

    print(f"No VM found with name: {vm_name}")


elif len(matches) == 1:

    vm = matches[0]

    print(f"Name           : {vm['name']}")
    print(f"Subscription   : {vm['subscription_id']}")
    print(f"Resource Group : {vm['resource_group']}")
    print(f"Resource Type  : {vm['resource_type']}")
    print(f"Region         : {vm['region']}")
    print(f"Resource ID    : {vm['resource_id']}")


else:

    print(
        f"Multiple VMs found with name: {vm_name}"
    )

    for vm in matches:

        print()
        print(f"Subscription   : {vm['subscription_id']}")
        print(f"Resource Group : {vm['resource_group']}")
        print(f"Region         : {vm['region']}")
        print(f"Resource ID    : {vm['resource_id']}")
