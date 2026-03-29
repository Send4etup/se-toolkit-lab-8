import json
import os
import tempfile

config_path = "/app/nanobot/config.json"
workspace_path = "/app/nanobot/workspace"

with open(config_path) as f:
    config = json.load(f)

# LLM provider
config["providers"]["custom"]["apiKey"] = os.environ.get("LLM_API_KEY", "")
config["providers"]["custom"]["apiBase"] = os.environ.get("LLM_API_BASE_URL", "")

# Gateway host/port
config["gateway"]["host"] = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS", "0.0.0.0")
config["gateway"]["port"] = int(os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT", "18790"))

# Webchat channel
webchat_host = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS", "0.0.0.0")
webchat_port = int(os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT", "18791"))
access_key = os.environ.get("NANOBOT_ACCESS_KEY", "")

config["channels"]["webchat"] = {
    "enabled": True,
    "host": webchat_host,
    "port": webchat_port,
    "accessKey": access_key,
    "allow_from": ["*"]
}

# MCP server env vars
config["tools"]["mcpServers"]["lms"]["env"] = {
    "LMS_API_BASE_URL": os.environ.get("NANOBOT_LMS_BACKEND_URL", ""),
    "LMS_API_KEY": os.environ.get("NANOBOT_LMS_API_KEY", "")
}

# Write resolved config
resolved_path = "/app/nanobot/config.resolved.json"
with open(resolved_path, "w") as f:
    json.dump(config, f, indent=2)

os.execvp("nanobot", ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace_path])
