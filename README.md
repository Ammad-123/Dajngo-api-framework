# Dajngo-api-framework
How to use Dajngo-api-framework see the steps
# Easy CRUD API Framework
Django-Ninja features:
Plus Extra:

## Install
`pip install django-api-framework`

Then add "easy" to your django INSTALLED_APPS:

```
[
    ...,
    "easy",
    ...,
]
```

## Usage
### Get all your Django app CRUD APIs up and running in < 1 min
In your Django project next to urls.py create new apis.py file:
```
from easy.main import EasyAPI

api_admin_v1 = EasyAPI(
    urls_namespace="admin_api",
    version="v1.0.0",
)

# Automatic Admin API generation
api_admin_v1.auto_create_admin_controllers()
```
Go to urls.py and add the following:
```
from django.urls import path
from .apis import api_admin_v1

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_admin/v1/", api_admin_v1.urls),  # <---------- !
]
```
Now go to http://127.0.0.1:8000/api_admin/v1/docs

You will see the automatic interactive API documentation (provided by Swagger UI).
![Auto generated APIs List](https://github.com/freemindcore/django-api-framework/blob/fae8209a8d08c55daf75ac3a4619fe62b8ef3af6/docs/images/admin_apis_list.png)


### Boilerplate Django project
A boilerplate Django project for quickly getting started, and get production ready easy-apis with 100% test coverage UP and running:
https://github.com/freemindcore/django-easy-api

![Auto generated APIs - Users](https://github.com/freemindcore/django-api-framework/blob/9aa26e92b6fd79f4d9db422ec450fe62d4cd97b9/docs/images/user_admin_api.png)


## Thanks to your help
**_If you find this project useful, please give your stars to support this open-source project. :) Thank you !_**





## Advanced Usage
If `CRUD_API_ENABLED_ALL_APPS` is set to True (default), all app models CRUD apis will be generated.
Apps in the `CRUD_API_EXCLUDE_APPS` list, will always be excluded.

If `CRUD_API_ENABLED_ALL_APPS` is set to False, only apps in the `CRUD_API_INCLUDE_APPS` list will have CRUD apis generated.

Also, configuration is possible for each model, via APIMeta class:
- `generate_crud`:      whether to create crud api, default to True
- `model_exclude`:      fields to be excluded in Schema
- `model_fields`:       fields to be included in Schema, default to `"__all__"`
- `model_join`:         prefetch and retrieve all m2m fields, default to False
- `model_recursive`:    recursively retrieve FK/OneToOne fields, default to False
- `sensitive_fields`:   fields to be ignored

Example:
```
class Category(TestBaseModel):
    title = models.CharField(max_length=100)
    status = models.PositiveSmallIntegerField(default=1, null=True)

    class APIMeta:
        generate_crud = True
        model_fields = ["field_1", "field_2",] # if not configured default to "__all__"
        model_join = True
        model_recursive = True
        sensitive_fields = ["password", "sensitive_info"]
```

### Adding CRUD APIs to a specific API Controller
By inheriting `CrudAPIController` class, CRUD APIs can be added to any API controller.
Configuration is available via `APIMeta` inner class in your Controller, same as the above `APIMeta` inner class defined in your Django models.

Example:

```
@api_controller("event_api", permissions=[AdminSitePermission])
class EventAPIController(CrudAPIController):
    def __init__(self, service: EventService):
        super().__init__(service)

    class APIMeta:
        model = Event # django model
        generate_crud = True # whether to create crud api, default to True
        model_fields = ["field_1", "field_2",] # if not configured default to "__all__"
        model_join = True
        model_recursive = True
        sensitive_fields = ["password", "sensitive_info"]

```
Please check tests/demo_app for more examples.
