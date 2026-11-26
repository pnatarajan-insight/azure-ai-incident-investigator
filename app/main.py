import json

from app.ai_investigator import investigate_incident
from app.analyzer import ( analyze_cpu, analyze_memory, analyze_pod_restarts, determine_overall_risk, generate_recommendations, get_ticket_priority, correlate_evidence, build_evidence)

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
print(f"Recent Deployment : {incident['recent_deployment']}")

print()


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

overall_risk = determine_overall_risk(findings)

print()

print(f"Overall Incident Risk: {overall_risk}")

recommendations = generate_recommendations(incident)

print()

print("Recommended Investigation")
print("=========================")

for index, recommendation in enumerate(recommendations, start=1):
    print(f"{index}. {recommendation}")

ticket_priority = get_ticket_priority(incident["priority"])

print()

print(f"ServiceNow priority : P{incident['priority']} ({ticket_priority})")

correlations = correlate_evidence(incident)

print()

print("Evidence Correlation")
print("====================")
for index, correlation in enumerate(correlations, start=1):
    print(f"{index}. {correlation}")

evidence = build_evidence(incident)

print()

print("Collected Evidence")
print("==================")

for item in evidence:
    print(
            f"- {item['type']}: "
            f"{item['value']}{item['unit']} "
            f"[{item['source']}]"
        )

analysis = {
        "findings": findings,
        "overall_risk": overall_risk,
        "recommendations": recommendation,
        "correlations": correlation,
        "evidence": evidence
    }



print(f"\nEvidence Items Collected: {len(evidence)}")

print()

print("AI Incident Investigation")

print("=========================")

print("Sending incident evidence to Azure OpenAI...")

print()

ai_result = investigate_incident(
        incident,
        analysis
        )

print(ai_result)

