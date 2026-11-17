import json

from analyzer import ( analyze_cpu, analyze_memory, analyze_pod_restarts)

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


print()

###
#cpu_result = analyze_cpu(incident["cpu_percent"])
#print()
#print("Incident Analysis on CPU")
#print("========================")

#print(
#    f"[{cpu_result['severity']}] "
#    )

#memory_result = analyze_memory(incident["memory_percent"])
#print()
#print("Incidnet Analysis on Memory")
#print("===========================")

#print(
#    f"[{memory_result['severity']}]"
#      )

#pod_restart_result = analyze_pod_restarts(incident["pod_restarts"])
#print()
#print("Incident Analysis on Pod Restart")
#print("================================")

#print(
#    f"[{pod_restart_result['severity']}]"
#    )
###

findings = [
        analyze_cpu(incident["cpu_percent"]),
        analyze_memory(incident["memory_percent"]),
        analyze_pod_restarts(incident["pod_restarts"]),
]

for finding in findings:
    print(
        f"[{finding['severity']}]"
        f"[{finding['message']}]"
    )
