import json

from app.llm_client import send_to_llm


def build_investigation_context(incident):

    context = {
        "incident_id": incident.get("incident_id"),
        "priority": incident.get("priority"),
        "resource": incident.get("resource"),
        "resource_type": incident.get("resource_type"),
        "alert": incident.get("alert"),
        "metric": incident.get("metric"),
        "metric_value": incident.get("metric_value"),
        "threshold": incident.get("threshold"),
        "duration": incident.get("duration"),
        "description": incident.get("description")
    }

    return json.dumps(context, indent=2)

def build_ai_prompt(incident, analysis):

    with open("prompts/incident_analysis.txt", "r") as file:
        prompt_template = file.read()

    incident_context = build_investigation_context(incident)

    analysis_context = json.dumps(analysis, indent=2)

    final_prompt = prompt_template.replace(
        "{incident_context}",
        incident_context
    )

    final_prompt = prompt_template.replace(
            "analysis_context}",
            analysis_context
    )

    return final_prompt

def investigate_incident(incident, analysis):
    prompt = build_ai_prompt(
                        incident,
                        analysis
                         )

    response = send_to_llm(prompt)

    return response
