load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "prompt_templates.py",
        "slack_functions.py",
        "slackbot.py",
    ],
    deps = [
        requirement("flask"),
        requirement("slack-sdk"),
        requirement("slack-bolt"),
        requirement("python-dotenv"),
        requirement("langchain"),
        requirement("openai"),
    ],
)
