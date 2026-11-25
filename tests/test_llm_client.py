from app.llm_client import send_to_llm


prompt = """
You are an Azure incident investigator.

An Azure virtual machine has 95% CPU utilization
for the last 15 minutes.

Give me:
1. Available evidence
2. Possible causes
3. Investigation steps
4. Recommended action
"""


response = send_to_llm(prompt)

print(response)
