"""MCP server for SDK Version Compatibility Resolver."""
import sys
import json
from client import SDKVersionDeprecationResolver

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "resolve_sdk_deprecations",
                "description": "Upgrades deprecated SDK calls to modern library syntax",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "code_snippet": {"type": "string"}
                    },
                    "required": ["code_snippet"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "resolve_sdk_deprecations":
            code = params.get("arguments", {}).get("code_snippet", "")
            res = SDKVersionDeprecationResolver.inspect_code(code)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
