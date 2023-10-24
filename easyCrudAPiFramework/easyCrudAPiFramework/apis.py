from easy.main import EasyAPI

api_admin_v1 = EasyAPI(
    urls_namespace="admin_api",
    version="v1.0.0",
)

# Automatic Admin API generation
api_admin_v1.auto_create_admin_controllers()