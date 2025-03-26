import boto3
import json
region_name="us-west-2" #TODO CHANGE
kb_id="GIH0AEZT1V" #TODO CHANGE
# try out KB using RetrieveAndGenerate API
bedrock_agent_runtime_client = boto3.client("bedrock-agent-runtime", region_name=region_name)
# Lets see how different Anthropic Claude 3 models responds to the input text we provide
claude_model_ids = [ ["Claude 3 Haiku", "us.anthropic.claude-3-5-sonnet-20241022-v2:0"]]
def ask_bedrock_llm_with_knowledge_base(query: str, model_arn: str, kb_id: str) -> str:
    response = bedrock_agent_runtime_client.retrieve_and_generate(
        input={
            'text': query
        },
    retrieveAndGenerateConfiguration={
        'type': 'KNOWLEDGE_BASE',
        'knowledgeBaseConfiguration': {
            'knowledgeBaseId': kb_id,
            'modelArn': model_arn,
            'retrievalConfiguration': {
                'vectorSearchConfiguration': {
                  #  'filter': {
                       # 'equals': {
                     #       'key': 'Marque',
                      #      'value': 'Samsung'
                 #       }
                #    }
                }
            }
        }
    }
)

    return response

#invoke bedrock agents
def invoke_bedrock_agent(query: str, agent_id: str, agent_alias_id: str) -> str:
    response = bedrock_agent_runtime_client.invoke_agent(
        agentId=agent_id,
        agentAliasId=agent_alias_id,
        sessionId='XXXXXXXX',
        inputText=query
    )
    return response
query = "liste les appareils?"

for model_id in claude_model_ids:
    model_arn = f'us.anthropic.claude-3-5-sonnet-20241022-v2:0'
    response = ask_bedrock_llm_with_knowledge_base(query, model_arn, kb_id)
    generated_text = response['output']['text']
    citations = response["citations"]
    contexts = []
    for citation in citations:
        retrievedReferences = citation["retrievedReferences"]
        for reference in retrievedReferences:
            contexts.append(reference["content"]["text"])
    #print(f"---------- Generated using {model_id[0]}:")
    #print(generated_text )
   # print(f'---------- The citations for the response generated by {model_id[0]}:')
  #  print(contexts)
    print()
    invoke_bedrock_agent(query, "DJCWVLUALB", "gengis")
    print(response)
