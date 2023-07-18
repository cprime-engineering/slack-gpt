load("@pip//:requirements.bzl", "requirement")

py_library(
    name = "domain",
    srcs = [
        "domain.py",
        "prompt_engineering/pre_prompt_templates.py",
        "prompt_engineering/prompt_generator.py",
    ],
    deps = [
        requirement("langchain"),
    ],
)