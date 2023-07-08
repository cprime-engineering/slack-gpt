load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "slackbot.py","prompt_templates.py",
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
