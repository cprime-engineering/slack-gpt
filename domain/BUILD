load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "domain",
    srcs = [
        "domain.py",
        "prompt_engineering/pre_prompt_templates.py",
        "prompt_engineering/prompt_generator.py",
        "slack_integration/web_client.py",
        "pinecone_integration/pinecone_client.py",
    ],
    data = [
        "source_knowledge/savings_accounts.txt",
    ],
    deps = [
        requirement("langchain"),
        requirement("slack-sdk"),
        requirement("python-dotenv"),
        requirement("openai"),
        requirement("pinecone-client"),
        requirement("tiktoken"),
    ],
)
