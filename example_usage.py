"""Example usage for SDK Version Compatibility Resolver."""
from client import SDKVersionDeprecationResolver

if __name__ == "__main__":
    legacy_code = "payload = user_schema.dict()\nloop = asyncio.get_event_loop()"
    res = SDKVersionDeprecationResolver.inspect_code(legacy_code)
    print("Deprecations Found:", res["deprecations_found"])
    print("Modernized Code:\n", res["modernized_code"])
