## Import the needed libraries
import os
import yaml
import requests
from decouple import config

# Get environment variables using the config object or os.environ["KEY"]
# These are the credentials passed by the variables of your pipeline to your tasks and in to your env
WEBHOOK_URL = config("WEBHOOK_URL")

def add_entity_to_port(entity_object):
    """A function to create the passed entity in Port using the webhook URL

    Params
    --------------
    entity_object: dict
        The entity to add in your Port catalog
    
    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(WEBHOOK_URL, json=entity_object, headers=headers)
    return response.json()


def process_and_ingest_worflow_file(folder_path):
    """This function takes folder path, converts the "jobs" property into a 
    JSON array using three keys (name, runs-on, and id). It then sends this data to Port

    Params
    --------------
    folder_path: str
        The path to the Github Workflow folder relative to the project's root directory
    
    Returns
    --------------
    response: dict
        The response object after calling the webhook
    """
    index = 1
    # Process each YAML file in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".yml") or filename.endswith(".yaml"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as file:
                yaml_data = yaml.safe_load(file)

            # Extract workflow name
            workflow_name = yaml_data.get("name", "")

            # Extract job names and their runs-on values
            jobs = yaml_data.get("jobs", {})
            job_info = []
            for job_name, job_details in jobs.items():
                job_id = f"job-{index}"
                runs_on = job_details.get("runs-on", "")
                steps = job_details.get("steps", [])
                num_steps = len(steps)
                job_info.append({"id": job_id, "job_name": job_name, "runs_on": runs_on, "num_steps": num_steps})
                index+=1

            entity_object = {
                "workflow_name": workflow_name,
                "jobs": job_info
            }
            webhook_response = add_entity_to_port(entity_object)
            print(webhook_response)

# Path to the folder containing the YAML files
folder_path = ".github/workflow/"
process_and_ingest_worflow_file(folder_path)