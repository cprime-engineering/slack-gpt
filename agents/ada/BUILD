load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "pre_prompt_templates.py",
        "prompt_generator.py",
        "slack_functions.py",
        "slackbot.py",
        "knowledge_base.py",
    ],
    data = [
        "pre_prompts/date",
        "pre_prompts/footer",
        "pre_prompts/persona",
        "pre_prompts/personalized",
        "pre_prompts/version",
        "source_knowledge/legends_of_computer_science.json",
    ],
    deps = [
        requirement("slack-sdk"),
        requirement("slack-bolt"),
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
        requirement("pandas"),
        requirement("tiktoken"),
    ],
)
