from jsonschema import validate

question_schema = {
    "type": "object",
    "properties": {
        "body": {"type": "string", "minLength": 5, "maxLength": 100 },
        "poster": {"type": "string", "minLength": 2, "maxLength": 100 }
    },
    "required": ["body", "poster"]
}

answer_schema = {
    "type": "object",
    "properties": {
        "response": {"type": "string", "minLength": 5, "maxLength": 100 },
        "username": {"type": "string", "minLength": 2, "maxLength": 100 }
    },
    "required": ["response", "username"]
}