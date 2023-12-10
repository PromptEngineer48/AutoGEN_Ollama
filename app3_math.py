
from autogen.agentchat.contrib.math_user_proxy_agent import MathUserProxyAgent
from autogen import AssistantAgent


config_list_mistral = [
{
'base_url': "http://0.0.0.0:8000",
}
]

llm_config={
"config_list": config_list_mistral,
}

# 1. create an AssistantAgent instance named "assistant"
assistant = AssistantAgent(
    name="assistant", 
    system_message="You are a helpful assistant.",
    llm_config=llm_config,
)

# 2. create the MathUserProxyAgent instance named "mathproxyagent"
# By default, the human_input_mode is "NEVER", which means the agent will not ask for human input.
mathproxyagent = MathUserProxyAgent(
    name="mathproxyagent", 
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False},
)


# given a math problem, we use the mathproxyagent to generate a prompt to be sent to the assistant as the initial message.
# the assistant receives the message and generates a response. The response will be sent back to the mathproxyagent for processing.
# The conversation continues until the termination condition is met, in MathChat, the termination condition is the detect of "\boxed{}" in the response.
math_problem = "Find all $x$ that satisfy the inequality $(2x+10)(x+3)<(3x+9)(x+8)$. Express your answer in interval notation."
mathproxyagent.initiate_chat(assistant, problem=math_problem)