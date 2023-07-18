py_test(
    name = "pre_prompt_templates_testcase",
    srcs = ["pre_prompt_templates_testcase.py"],
    data = [
        "expected_pre_prompts/date",
        "expected_pre_prompts/footer",
        "expected_pre_prompts/persona",
        "expected_pre_prompts/personalized",
        "expected_pre_prompts/version",
    ],
    deps = ["//personas/ada:slackbot"],
)

py_test(
    name = "prompt_generator_testcase",
    srcs = ["prompt_generator_testcase.py"],
    data = ["expected_prompt_content/personalized.json"],
    deps = ["//personas/ada:slackbot"],
)

py_test(
    name = "knowledge_base_testcase",
    srcs = ["knowledge_base_testcase.py"],
    deps = ["//personas/ada:slackbot"],
)

