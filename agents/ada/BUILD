load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "pre_prompt_templates.py",
        "prompt_generator.py",
        "slack_functions.py",
        "slackbot.py",
    ],
    data = [
        "pre_prompts/footer",
        "pre_prompts/persona",
        "pre_prompts/personalized",
    ],
    deps = [
        requirement("slack-sdk"),
        requirement("slack-bolt"),
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
    ],
)
