def analyze_cpu(cpu):
    if cpu > 90:
        return {
            "severity": "CRITICAL",
            "message": f"CPU utilization is very high at {cpu}%"
        }
    elif cpu > 75:
        return {
            "severity": "WARNING",
            "message": f"CPU utilization is elevated at {cpu}%"
        }
    else:
        return {
            "severity": "INFO",
            "message": f"CPU utilization is within normal range at {cpu}%"
        }


def analyze_memory(memory):
    if memory > 90:
        return {
            "severity": "CRITICAL",
            "message": f"Memory utilization is very high at {memory}%"
        }
    elif memory > 75:
        return {
            "severity": "WARNING",
            "message": f"Memory utilization is elevated at {memory}%"
        }
    else:
        return {
            "severity": "INFO",
            "message": f"Memory utilization is within normal range at {memory}%"
        }

def analyze_pod_restarts(restarts):
    if restarts == 0:
        return {
            "severity": "INFO",
            "message": "No Pod restarts detected"
        }
    elif restarts < 5:
        return {
            "severity": "WARNING",
            "message": f"Pod restarts detected: {restarts}"
        }
    else:
        return {
            "severity": "HIGH",
            "message": f"Pod restart count is high at {restarts}"
        }

SEVERITY_RANK = {
        "INFO": 1,
        "WARNING": 2,
        "HIGH": 3,
        "CRITICAL": 4
        }

def determine_overall_risk(findings):
    highest_severity = "INFO"

    for finding in findings:
        current_severity = finding["severity"]

        if SEVERITY_RANK[current_severity] > SEVERITY_RANK[highest_severity]:
            highest_severity = current_severity

    return highest_severity


def generate_recommendations(incident):
    recommendations = []

    if incident["memory_percent"] > 90:
        recommendations.append(
            "Investigate container memory consumption."
        )
        recommendations.append(
            "Review Kubernetes memory requests and limits."
        )

    if incident["pod_restarts"] > 5:
        recommendations.append(
            "Inspect Kubernetes events to determine the reason for pod restarts."
        )

    if incident["cpu_percent"] > 90:
        recommendations.append(
            "Investigate processes responsible for high CPU utilization."
        )

    if not recommendations:
        recommendations.append(
            "No critical telemetry conditions were detected by the current rules."
        )

    return recommendations

def get_ticket_priority(priority):
    priority_mapping = {
            "1": "CRITICAL",
            "2": "HIGH",
            "3": "MODERATE",
            "4": "LOW"
        }

    return priority_mapping.get(priority, "UNKNOWN")

def correlate_evidence(incident):
    correlations = []

    if (
        incident["memory_percent"] > 90
        and incident["pod_restarts"] > 5
    ):
        correlations.append(
            "High memory utilization is occurring together with repeated pod restarts."
        )

    if (
        incident["pod_restarts"] > 5
        and incident["http_500_count"] > 10
    ):
        correlations.append(
            "Repeated pod restarts correlate with elevated HTTP 500 errors."
        )

    if (
        incident["recent_deployment"]
        and incident["http_500_count"] > 10
    ):
        correlations.append(
            "Application errors are present following a recent deployment."
        )

    if (
        incident["termination_reason"] == "OOMKilled"
        and incident["memory_percent"] > 90
    ):
        correlations.append(
                "Container termination with OOMKilled is consistent with observed high memory utilization."
        )

    return correlations

def build_evidence(incident):
    evidence = []

    if incident["memory_percent"] > 90:
        evidence.append({
            "source": "Telemetry",
            "type": "Memory",
            "value": incident["memory_percent"],
            "unit": "%",
            "status": "Abnormal"
        })

    if incident["pod_restarts"] > 5:
        evidence.append({
            "source": "Kubernetes",
            "type": "Pod Restarts",
            "value": incident["pod_restarts"],
            "unit": "count",
            "status": "Abnormal"
        })

    if incident["http_500_count"] > 10:
        evidence.append({
            "source": "Application",
            "type": "HTTP 500",
            "value": incident["http_500_count"],
            "unit": "count",
            "status": "Abnormal"
        })

    if incident["recent_deployment"]:
        evidence.append({
            "source": "Deployment",
            "type": "Recent Deployment",
            "value": True,
            "unit": "",
            "status": "Context"
        })

    if incident["termination_reason"]:
        evidence.append({
            "source": "Kubernetes",
            "type": "Termination Reason",
            "value": incident["termination_reason"],
            "unit": "",
            "status": "Abnormal"
        })

    return evidence
