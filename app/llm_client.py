import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def send_to_llm(prompt):

    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not endpoint:
        raise ValueError("AZURE_OPENAI_ENDPOINT is missing")

    if not api_key:
        raise ValueError("AZURE_OPENAI_API_KEY is missing")

    if not deployment:
        raise ValueError("AZURE_OPENAI_DEPLOYMENT is missing")

    # Azure OpenAI v1 endpoint
    base_url = endpoint.rstrip("/") + "/openai/v1/"

    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    response = client.responses.create(
        model=deployment,
        input=prompt
    )

    return response.output_text
