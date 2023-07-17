load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "prompt_generator.py",
        "slack_functions.py",
        "slackbot.py",
        "pre_prompt_templates.py",
    ],
    data = ["pre_prompts/persona", "pre_prompts/footer", "pre_prompts/personalized"],
    deps = [
        requirement("slack-sdk"),
        requirement("slack-bolt"),
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
    ],
)
