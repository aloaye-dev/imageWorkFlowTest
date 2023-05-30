```json showLineNumbers
{
  "identifier": "githubWorkflow",
  "description": "This blueprint represents a GitHub workflow in our catalog",
  "title": "GitHub Workflow",
  "icon": "Github",
  "schema": {
    "properties": {
      "jobName": {
        "type": "string",
        "title": "Job Name"
      },
      "runsOn": {
        "type": "string",
        "title": "Runs On"
      },
      "numSteps": {
        "type": "number",
        "title": "Number of Steps"
      }
    },
    "required": []
  },
  "mirrorProperties": {},
  "calculationProperties": {},
  "relations": {}
}
```