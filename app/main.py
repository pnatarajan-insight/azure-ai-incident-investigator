import json

with open("scenarios/incident_001.json", "r") as file:
    incident = json.load(file)

print("Azure AI Incident Investigator")
print("================================")

print(f"Incident       : {incident['number']}")
print(f"Description    : {incident['short_description']}")
print(f"Priority       : {incident['priority']}")
print(f"Status         : {incident['state']}")
print(f"Assignment     : {incident['assignment_group']}")
print(f"CI             : {incident['configuration_item']}")
print(f"Environment    : {incident['environment']}")
print(f"Azure Resource : {incident['azure_resource_type']}")
print(f"CPU            : {incident['cpu_percent']}%")
print(f"Memory         : {incident['memory_percent']}%")
print(f"Pod Restarts   : {incident['pod_restarts']}")
print(f"HTTP 500 Count : {incident['http_500_count']}")
