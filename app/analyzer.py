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
            "severity": "CRITICAL",
            "message": f"Pod restart count is high at {restarts}"
        }
