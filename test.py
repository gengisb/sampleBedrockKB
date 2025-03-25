import boto3
region_name="us-west-2" #TODO CHANGE
kb_id="XXXX" #TODO CHANGE
bedrock_agent_runtime = boto3.client(
    service_name = "bedrock-agent-runtime",region_name=region_name)

def retrieveAndGenerate(input, kbId):
    return bedrock_agent_runtime.retrieve_and_generate(
        input={
            'text': input
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kbId,
                'modelArn': 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
                }
            }
        )

response = retrieveAndGenerate("liste les appareils?", kb_id)["output"]["text"]
print(response)
