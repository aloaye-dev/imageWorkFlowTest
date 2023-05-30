```json showLineNumbers
{
    "identifier": "githubWorkflowMapper",
    "title": "GitHub Workflow Mapper",
    "description": "A webhook configuration to map GitHub Workflow in Port",
    "icon": "Github",
    "mappings": [
        {
            "blueprint": "githubWorkflow",
            "itemsToParse": ".body.jobs",
            "entity": {
                "identifier": ".item.id",
                "title": ".body.workflow_name",
                "properties": {
                    "job": ".item.job_name",
                    "runsOn": ".item.runs_on",
                    "numSteps": ".item.num_steps"
                }
            }
        }
    ],
    "enabled": true,
    "security": {}
}
```