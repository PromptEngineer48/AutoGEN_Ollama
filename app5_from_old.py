#install these two libraries
# pip install pyautogen
# pip install xgboost

from autogen import AssistantAgent, UserProxyAgent


config_list_mistral = [
{
'base_url': "http://0.0.0.0:8000",
'api_key': "NULL",
}
]

config_list_codellama = [
{
'base_url': "http://0.0.0.0:36792",
'api_key': "NULL",
}
]

llm_config_mistral={
"config_list": config_list_mistral,
}

llm_config_codellama={
"config_list": config_list_codellama,
}

#create an instance of AssistanAgent
assistant = AssistantAgent(
    name = "assistant",
    llm_config=llm_config_codellama,
)

#create an instance of UserProxyAgent
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    llm_config=llm_config_mistral,
)

user_proxy.initiate_chat(
    assistant,
    message = """Write me a python function to check for prime number and the check for the number 79"""
)