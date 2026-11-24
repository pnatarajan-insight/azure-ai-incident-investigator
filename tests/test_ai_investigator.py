from app.ai_investigator import build_ai_prompt


sample_incident = {
    "incident_id": "INC0012345",
    "priority": "P2",
    "resource": "prod-web-vm01",
    "resource_type": "Microsoft.Compute/virtualMachines",
    "alert": "High CPU utilization",
    "metric": "Percentage CPU",
    "metric_value": 94,
    "threshold": 90,
    "duration": "15 minutes",
    "description": "CPU utilization exceeded the configured threshold."
}


prompt = build_ai_prompt(sample_incident)

print(prompt)
