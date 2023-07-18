load("@pip//:requirements.bzl", "requirement")

py_binary(
    name = "slackbot",
    srcs = [
        "slackbot.py",
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
