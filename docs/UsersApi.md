# rebrickable.UsersApi

All URIs are relative to *https://rebrickable.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_allparts_list**](UsersApi.md#users_allparts_list) | **GET** /api/v3/users/{user_token}/allparts/ | Get a list of all the Parts in all the user&#39;s Part Lists as well as the Parts inside Sets in the user&#39;s Set Lists.
[**users_badges_list**](UsersApi.md#users_badges_list) | **GET** /api/v3/users/badges/ | Get a list of all the available Badges
[**users_badges_read**](UsersApi.md#users_badges_read) | **GET** /api/v3/users/badges/{id}/ | Get details about a specific Badge
[**users_build_read**](UsersApi.md#users_build_read) | **GET** /api/v3/users/{user_token}/build/{set_num}/ | Find out how many parts the user needs to build the specified Set.
[**users_lost_parts_create**](UsersApi.md#users_lost_parts_create) | **POST** /api/v3/users/{user_token}/lost_parts/ | Add one or more Lost Parts to the user.
[**users_lost_parts_delete**](UsersApi.md#users_lost_parts_delete) | **DELETE** /api/v3/users/{user_token}/lost_parts/{id}/ | Remove the Lost Part from the user.
[**users_lost_parts_list**](UsersApi.md#users_lost_parts_list) | **GET** /api/v3/users/{user_token}/lost_parts/ | Get a list of all the Lost Parts from the user&#39;s LEGO collection.
[**users_partlists_create**](UsersApi.md#users_partlists_create) | **POST** /api/v3/users/{user_token}/partlists/ | Add a new Part List.
[**users_partlists_delete**](UsersApi.md#users_partlists_delete) | **DELETE** /api/v3/users/{user_token}/partlists/{list_id}/ | Delete a Part List and all it&#39;s Parts.
[**users_partlists_list**](UsersApi.md#users_partlists_list) | **GET** /api/v3/users/{user_token}/partlists/ | Get a list of all the user&#39;s Part Lists.
[**users_partlists_partial_update**](UsersApi.md#users_partlists_partial_update) | **PATCH** /api/v3/users/{user_token}/partlists/{list_id}/ | Update an existing Part List&#39;s details.
[**users_partlists_parts_create**](UsersApi.md#users_partlists_parts_create) | **POST** /api/v3/users/{user_token}/partlists/{list_id}/parts/ | Add one or more Parts to the Part List.
[**users_partlists_parts_delete**](UsersApi.md#users_partlists_parts_delete) | **DELETE** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Delete a Part from the Part List.
[**users_partlists_parts_list**](UsersApi.md#users_partlists_parts_list) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/parts/ | Get a list of all the Parts in a specific Part List.
[**users_partlists_parts_read**](UsersApi.md#users_partlists_parts_read) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Get details about a specific Part in the Part List.
[**users_partlists_parts_update**](UsersApi.md#users_partlists_parts_update) | **PUT** /api/v3/users/{user_token}/partlists/{list_id}/parts/{part_num}/{color_id}/ | Replace an existing Part&#39;s details in the Part List.
[**users_partlists_read**](UsersApi.md#users_partlists_read) | **GET** /api/v3/users/{user_token}/partlists/{list_id}/ | Get details about a specific Part List.
[**users_partlists_update**](UsersApi.md#users_partlists_update) | **PUT** /api/v3/users/{user_token}/partlists/{list_id}/ | Replace an existing Part List&#39;s details.
[**users_parts_list**](UsersApi.md#users_parts_list) | **GET** /api/v3/users/{user_token}/parts/ | Get a list of all the Parts in all the user&#39;s Part Lists.
[**users_profile_list**](UsersApi.md#users_profile_list) | **GET** /api/v3/users/{user_token}/profile/ | Get details about a specific user.
[**users_setlists_create**](UsersApi.md#users_setlists_create) | **POST** /api/v3/users/{user_token}/setlists/ | Add a new Set List.
[**users_setlists_delete**](UsersApi.md#users_setlists_delete) | **DELETE** /api/v3/users/{user_token}/setlists/{list_id}/ | Delete a Set List and all it&#39;s Sets.
[**users_setlists_list**](UsersApi.md#users_setlists_list) | **GET** /api/v3/users/{user_token}/setlists/ | Get a list of all the user&#39;s Set Lists.
[**users_setlists_partial_update**](UsersApi.md#users_setlists_partial_update) | **PATCH** /api/v3/users/{user_token}/setlists/{list_id}/ | Update an existing Set List&#39;s details.
[**users_setlists_read**](UsersApi.md#users_setlists_read) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/ | Get details about a specific Set List.
[**users_setlists_sets_create**](UsersApi.md#users_setlists_sets_create) | **POST** /api/v3/users/{user_token}/setlists/{list_id}/sets/ | Add one or more Sets to the Set List. Existing Sets are unaffected.
[**users_setlists_sets_delete**](UsersApi.md#users_setlists_sets_delete) | **DELETE** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Delete a Set from the Set List.
[**users_setlists_sets_list**](UsersApi.md#users_setlists_sets_list) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/sets/ | Get a list of all the Sets in a specific Set List.
[**users_setlists_sets_partial_update**](UsersApi.md#users_setlists_sets_partial_update) | **PATCH** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Update an existing Set&#39;s details in the Set List.
[**users_setlists_sets_read**](UsersApi.md#users_setlists_sets_read) | **GET** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Get details about a specific Set in the Set List.
[**users_setlists_sets_update**](UsersApi.md#users_setlists_sets_update) | **PUT** /api/v3/users/{user_token}/setlists/{list_id}/sets/{set_num}/ | Replace an existing Set&#39;s details in the Set List.
[**users_setlists_update**](UsersApi.md#users_setlists_update) | **PUT** /api/v3/users/{user_token}/setlists/{list_id}/ | Replace an existing Set List&#39;s details.
[**users_sets_create**](UsersApi.md#users_sets_create) | **POST** /api/v3/users/{user_token}/sets/ | Add one or more Sets to the user&#39;s LEGO collection. Existing Sets are unaffected.
[**users_sets_delete**](UsersApi.md#users_sets_delete) | **DELETE** /api/v3/users/{user_token}/sets/{set_num}/ | Delete the Set from all the user&#39;s Set Lists.
[**users_sets_list**](UsersApi.md#users_sets_list) | **GET** /api/v3/users/{user_token}/sets/ | Get a list of all the Sets in the user&#39;s LEGO collection.
[**users_sets_read**](UsersApi.md#users_sets_read) | **GET** /api/v3/users/{user_token}/sets/{set_num}/ | Get details about a specific Set in the user&#39;s LEGO collection.
[**users_sets_sync_create**](UsersApi.md#users_sets_sync_create) | **POST** /api/v3/users/{user_token}/sets/sync/ | Synchronise a user&#39;s Sets to the POSTed list.
[**users_sets_update**](UsersApi.md#users_sets_update) | **PUT** /api/v3/users/{user_token}/sets/{set_num}/ | Update an existing Set&#39;s quantity in all Set Lists. This PUT call is different to others in that it will create
[**users_token_create**](UsersApi.md#users_token_create) | **POST** /api/v3/users/_token/ | Generate a User Token to be used for authorising user account actions in subsequent calls. Username can be either


# **users_allparts_list**
> users_allparts_list(user_token, page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id)

Get a list of all the Parts in all the user's Part Lists as well as the Parts inside Sets in the user's Set Lists.

Get a list of all the Parts in all the user's Part Lists as well as the Parts inside Sets in the user's Set Lists.  ###WARNING this call is very resource intensive, do not overuse it!  Optionally, filter by one or more of the below query parameters.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
part_num = 'part_num_example' # str | null (optional)
part_cat_id = 'part_cat_id_example' # str | null (optional)
color_id = 'color_id_example' # str | null (optional)

try:
    # Get a list of all the Parts in all the user's Part Lists as well as the Parts inside Sets in the user's Set Lists.
    api_instance.users_allparts_list(user_token, page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_allparts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **part_num** | **str**| null | [optional] 
 **part_cat_id** | **str**| null | [optional] 
 **color_id** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_badges_list**
> users_badges_list(page=page, page_size=page_size, ordering=ordering)

Get a list of all the available Badges

Get a list of all the available Badges

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all the available Badges
    api_instance.users_badges_list(page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling UsersApi->users_badges_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_badges_read**
> users_badges_read(id)

Get details about a specific Badge

Get details about a specific Badge

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
id = 'id_example' # str | null

try:
    # Get details about a specific Badge
    api_instance.users_badges_read(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_badges_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_build_read**
> users_build_read(user_token, set_num)

Find out how many parts the user needs to build the specified Set.

Find out how many parts the user needs to build the specified Set.  The user's default Build Settings will be used to calculate a Build Match % using their LEGO Collection of Sets and Parts.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null

try:
    # Find out how many parts the user needs to build the specified Set.
    api_instance.users_build_read(user_token, set_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_build_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_lost_parts_create**
> users_lost_parts_create(user_token, inv_part_id, lost_quantity=lost_quantity)

Add one or more Lost Parts to the user.

Add one or more Lost Parts to the user.  ### Single Part When adding a single Part, returns the successfully created Part (status 201) or details for why the Part could not be added. ### Multiple Parts To add multiple Parts, POST a JSON list of them (using a Content-Type header of 'application/json'). The inv_part_id field can be retrieved from the Set's inventory. e.g: `[{\"inv_part_id\": 806698, \"lost_quantity\": 3}, {\"inv_part_id\": 256007, \"lost_quantity\": 2}]` Returns a list of successfully added Parts. If the Part already exists or is unrecognised, it will be skipped.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
inv_part_id = 'inv_part_id_example' # str | null
lost_quantity = 'lost_quantity_example' # str | null (optional)

try:
    # Add one or more Lost Parts to the user.
    api_instance.users_lost_parts_create(user_token, inv_part_id, lost_quantity=lost_quantity)
except ApiException as e:
    print("Exception when calling UsersApi->users_lost_parts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **inv_part_id** | **str**| null | 
 **lost_quantity** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_lost_parts_delete**
> users_lost_parts_delete(user_token, id)

Remove the Lost Part from the user.

Remove the Lost Part from the user.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
id = 'id_example' # str | null

try:
    # Remove the Lost Part from the user.
    api_instance.users_lost_parts_delete(user_token, id)
except ApiException as e:
    print("Exception when calling UsersApi->users_lost_parts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_lost_parts_list**
> users_lost_parts_list(user_token, page=page, page_size=page_size, ordering=ordering)

Get a list of all the Lost Parts from the user's LEGO collection.

Get a list of all the Lost Parts from the user's LEGO collection.  Optionally, filter by one or more of the below query parameters.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all the Lost Parts from the user's LEGO collection.
    api_instance.users_lost_parts_list(user_token, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling UsersApi->users_lost_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_create**
> users_partlists_create(user_token, name, is_buildable=is_buildable, num_parts=num_parts)

Add a new Part List.

Add a new Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
name = 'name_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
num_parts = 'num_parts_example' # str | null (optional)

try:
    # Add a new Part List.
    api_instance.users_partlists_create(user_token, name, is_buildable=is_buildable, num_parts=num_parts)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **name** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **num_parts** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_delete**
> users_partlists_delete(user_token, list_id)

Delete a Part List and all it's Parts.

Delete a Part List and all it's Parts.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null

try:
    # Delete a Part List and all it's Parts.
    api_instance.users_partlists_delete(user_token, list_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_list**
> users_partlists_list(user_token, page=page, page_size=page_size)

Get a list of all the user's Part Lists.

Get a list of all the user's Part Lists.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get a list of all the user's Part Lists.
    api_instance.users_partlists_list(user_token, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_partial_update**
> users_partlists_partial_update(user_token, list_id, is_buildable=is_buildable, name=name, num_parts=num_parts)

Update an existing Part List's details.

Update an existing Part List's details.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
name = 'name_example' # str | null (optional)
num_parts = 'num_parts_example' # str | null (optional)

try:
    # Update an existing Part List's details.
    api_instance.users_partlists_partial_update(user_token, list_id, is_buildable=is_buildable, name=name, num_parts=num_parts)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **name** | **str**| null | [optional] 
 **num_parts** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_parts_create**
> users_partlists_parts_create(user_token, list_id, part_num, quantity, color_id)

Add one or more Parts to the Part List.

Add one or more Parts to the Part List.  ### Single Part When adding a single Part, returns the successfully created Part (status 201) or details for why the Part could not be added. ### Multiple Parts To add multiple Parts, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"part_num\":\"3001\", \"color_id\": 1, \"quantity\": 10}, {\"part_num\":\"3001\", \"color_id\": 2, \"quantity\": 20}, {\"part_num\":\"3002\", \"color_id\": 14, \"quantity\": 30}]` Returns a list of successfully added Parts. If the Part already exists or is unrecognised, it will be skipped.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
part_num = 'part_num_example' # str | null
quantity = 'quantity_example' # str | null
color_id = 'color_id_example' # str | null

try:
    # Add one or more Parts to the Part List.
    api_instance.users_partlists_parts_create(user_token, list_id, part_num, quantity, color_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_parts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **part_num** | **str**| null | 
 **quantity** | **str**| null | 
 **color_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_parts_delete**
> users_partlists_parts_delete(user_token, list_id, color_id, part_num)

Delete a Part from the Part List.

Delete a Part from the Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
color_id = 'color_id_example' # str | null
part_num = 'part_num_example' # str | null

try:
    # Delete a Part from the Part List.
    api_instance.users_partlists_parts_delete(user_token, list_id, color_id, part_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_parts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **color_id** | **str**| null | 
 **part_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_parts_list**
> users_partlists_parts_list(user_token, list_id, page=page, page_size=page_size, ordering=ordering)

Get a list of all the Parts in a specific Part List.

Get a list of all the Parts in a specific Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all the Parts in a specific Part List.
    api_instance.users_partlists_parts_list(user_token, list_id, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_parts_read**
> users_partlists_parts_read(user_token, list_id, color_id, part_num)

Get details about a specific Part in the Part List.

Get details about a specific Part in the Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
color_id = 'color_id_example' # str | null
part_num = 'part_num_example' # str | null

try:
    # Get details about a specific Part in the Part List.
    api_instance.users_partlists_parts_read(user_token, list_id, color_id, part_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_parts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **color_id** | **str**| null | 
 **part_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_parts_update**
> users_partlists_parts_update(user_token, list_id, color_id, part_num, quantity)

Replace an existing Part's details in the Part List.

Replace an existing Part's details in the Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
color_id = 'color_id_example' # str | null
part_num = 'part_num_example' # str | null
quantity = 'quantity_example' # str | null

try:
    # Replace an existing Part's details in the Part List.
    api_instance.users_partlists_parts_update(user_token, list_id, color_id, part_num, quantity)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_parts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **color_id** | **str**| null | 
 **part_num** | **str**| null | 
 **quantity** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_read**
> users_partlists_read(user_token, list_id)

Get details about a specific Part List.

Get details about a specific Part List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null

try:
    # Get details about a specific Part List.
    api_instance.users_partlists_read(user_token, list_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_partlists_update**
> users_partlists_update(user_token, list_id, name, is_buildable=is_buildable, num_parts=num_parts)

Replace an existing Part List's details.

Replace an existing Part List's details.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
name = 'name_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
num_parts = 'num_parts_example' # str | null (optional)

try:
    # Replace an existing Part List's details.
    api_instance.users_partlists_update(user_token, list_id, name, is_buildable=is_buildable, num_parts=num_parts)
except ApiException as e:
    print("Exception when calling UsersApi->users_partlists_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **name** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **num_parts** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_parts_list**
> users_parts_list(user_token, page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id, ordering=ordering, search=search)

Get a list of all the Parts in all the user's Part Lists.

Get a list of all the Parts in all the user's Part Lists.  ###Set List logic Parts appearing in multiple Part Lists will be listed multiple times.  Optionally, filter by one or more of the below query parameters.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
part_num = 'part_num_example' # str | null (optional)
part_cat_id = 'part_cat_id_example' # str | null (optional)
color_id = 'color_id_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)
search = 'search_example' # str | null (optional)

try:
    # Get a list of all the Parts in all the user's Part Lists.
    api_instance.users_parts_list(user_token, page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id, ordering=ordering, search=search)
except ApiException as e:
    print("Exception when calling UsersApi->users_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **part_num** | **str**| null | [optional] 
 **part_cat_id** | **str**| null | [optional] 
 **color_id** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 
 **search** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_profile_list**
> users_profile_list(user_token, page=page, page_size=page_size)

Get details about a specific user.

Get details about a specific user.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get details about a specific user.
    api_instance.users_profile_list(user_token, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling UsersApi->users_profile_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_create**
> users_setlists_create(user_token, name, is_buildable=is_buildable, num_sets=num_sets)

Add a new Set List.

Add a new Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
name = 'name_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
num_sets = 'num_sets_example' # str | null (optional)

try:
    # Add a new Set List.
    api_instance.users_setlists_create(user_token, name, is_buildable=is_buildable, num_sets=num_sets)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **name** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **num_sets** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_delete**
> users_setlists_delete(user_token, list_id)

Delete a Set List and all it's Sets.

Delete a Set List and all it's Sets.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null

try:
    # Delete a Set List and all it's Sets.
    api_instance.users_setlists_delete(user_token, list_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_list**
> users_setlists_list(user_token, page=page, page_size=page_size)

Get a list of all the user's Set Lists.

Get a list of all the user's Set Lists.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get a list of all the user's Set Lists.
    api_instance.users_setlists_list(user_token, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_partial_update**
> users_setlists_partial_update(user_token, list_id, is_buildable=is_buildable, name=name, num_sets=num_sets)

Update an existing Set List's details.

Update an existing Set List's details.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
name = 'name_example' # str | null (optional)
num_sets = 'num_sets_example' # str | null (optional)

try:
    # Update an existing Set List's details.
    api_instance.users_setlists_partial_update(user_token, list_id, is_buildable=is_buildable, name=name, num_sets=num_sets)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **name** | **str**| null | [optional] 
 **num_sets** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_read**
> users_setlists_read(user_token, list_id)

Get details about a specific Set List.

Get details about a specific Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null

try:
    # Get details about a specific Set List.
    api_instance.users_setlists_read(user_token, list_id)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_create**
> users_setlists_sets_create(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)

Add one or more Sets to the Set List. Existing Sets are unaffected.

Add one or more Sets to the Set List. Existing Sets are unaffected.  ### Single Set When adding a single Set, returns the successfully created Set (status 201) or details for why the Set could not be added. ### Multiple Sets To add multiple Sets, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"set_num\":\"8043-1\", \"quantity\": 1}, {\"set_num\":\"8110-1\", \"quantity\": 2, \"include_spares\": \"False\"}]` Returns a list of successfully added Sets. If the Set already exists or is unrecognised, it will be skipped.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)
include_spares = 'include_spares_example' # str | null (optional)

try:
    # Add one or more Sets to the Set List. Existing Sets are unaffected.
    api_instance.users_setlists_sets_create(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 
 **include_spares** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_delete**
> users_setlists_sets_delete(user_token, list_id, set_num)

Delete a Set from the Set List.

Delete a Set from the Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
set_num = 'set_num_example' # str | null

try:
    # Delete a Set from the Set List.
    api_instance.users_setlists_sets_delete(user_token, list_id, set_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_list**
> users_setlists_sets_list(user_token, list_id, page=page, page_size=page_size, ordering=ordering)

Get a list of all the Sets in a specific Set List.

Get a list of all the Sets in a specific Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all the Sets in a specific Set List.
    api_instance.users_setlists_sets_list(user_token, list_id, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_partial_update**
> users_setlists_sets_partial_update(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)

Update an existing Set's details in the Set List.

Update an existing Set's details in the Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)
include_spares = 'include_spares_example' # str | null (optional)

try:
    # Update an existing Set's details in the Set List.
    api_instance.users_setlists_sets_partial_update(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 
 **include_spares** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_read**
> users_setlists_sets_read(user_token, list_id, set_num)

Get details about a specific Set in the Set List.

Get details about a specific Set in the Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
set_num = 'set_num_example' # str | null

try:
    # Get details about a specific Set in the Set List.
    api_instance.users_setlists_sets_read(user_token, list_id, set_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_sets_update**
> users_setlists_sets_update(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)

Replace an existing Set's details in the Set List.

Replace an existing Set's details in the Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)
include_spares = 'include_spares_example' # str | null (optional)

try:
    # Replace an existing Set's details in the Set List.
    api_instance.users_setlists_sets_update(user_token, list_id, set_num, quantity=quantity, include_spares=include_spares)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_sets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 
 **include_spares** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_setlists_update**
> users_setlists_update(user_token, list_id, name, is_buildable=is_buildable, num_sets=num_sets)

Replace an existing Set List's details.

Replace an existing Set List's details.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
list_id = 'list_id_example' # str | null
name = 'name_example' # str | null
is_buildable = 'is_buildable_example' # str | null (optional)
num_sets = 'num_sets_example' # str | null (optional)

try:
    # Replace an existing Set List's details.
    api_instance.users_setlists_update(user_token, list_id, name, is_buildable=is_buildable, num_sets=num_sets)
except ApiException as e:
    print("Exception when calling UsersApi->users_setlists_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **list_id** | **str**| null | 
 **name** | **str**| null | 
 **is_buildable** | **str**| null | [optional] 
 **num_sets** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_create**
> users_sets_create(user_token, set_num, quantity=quantity, include_spares=include_spares)

Add one or more Sets to the user's LEGO collection. Existing Sets are unaffected.

Add one or more Sets to the user's LEGO collection. Existing Sets are unaffected.  ### Set List logic The Set List used when adding sets is chosen in the following order: 1. If no Set Lists exist, one will be created and used 2. User's configured default Set List for Imports 3. The first Set List alphabetically  ### Single Set When adding a single Set, returns the successfully created Set (status 201) or details for why the Set could not be added. ### Multiple Sets To add multiple Sets, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"set_num\":\"8043-1\", \"quantity\": 1}, {\"set_num\":\"8110-1\", \"quantity\": 2, \"include_spares\": \"False\"}]` Returns a list of successfully added Sets. If the Set already exists or is unrecognised, it will be skipped.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)
include_spares = 'include_spares_example' # str | null (optional)

try:
    # Add one or more Sets to the user's LEGO collection. Existing Sets are unaffected.
    api_instance.users_sets_create(user_token, set_num, quantity=quantity, include_spares=include_spares)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 
 **include_spares** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_delete**
> users_sets_delete(user_token, set_num)

Delete the Set from all the user's Set Lists.

Delete the Set from all the user's Set Lists.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null

try:
    # Delete the Set from all the user's Set Lists.
    api_instance.users_sets_delete(user_token, set_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_list**
> users_sets_list(user_token, page=page, page_size=page_size, set_num=set_num, theme_id=theme_id, min_year=min_year, max_year=max_year, min_parts=min_parts, max_parts=max_parts, ordering=ordering, search=search)

Get a list of all the Sets in the user's LEGO collection.

Get a list of all the Sets in the user's LEGO collection.  ### Set List logic Sets appearing in multiple Set Lists will be listed multiple times.  Optionally, filter by one or more of the below query parameters.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
set_num = 'set_num_example' # str | null (optional)
theme_id = 'theme_id_example' # str | null (optional)
min_year = 'min_year_example' # str | null (optional)
max_year = 'max_year_example' # str | null (optional)
min_parts = 'min_parts_example' # str | null (optional)
max_parts = 'max_parts_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)
search = 'search_example' # str | null (optional)

try:
    # Get a list of all the Sets in the user's LEGO collection.
    api_instance.users_sets_list(user_token, page=page, page_size=page_size, set_num=set_num, theme_id=theme_id, min_year=min_year, max_year=max_year, min_parts=min_parts, max_parts=max_parts, ordering=ordering, search=search)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **set_num** | **str**| null | [optional] 
 **theme_id** | **str**| null | [optional] 
 **min_year** | **str**| null | [optional] 
 **max_year** | **str**| null | [optional] 
 **min_parts** | **str**| null | [optional] 
 **max_parts** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 
 **search** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_read**
> users_sets_read(user_token, set_num)

Get details about a specific Set in the user's LEGO collection.

Get details about a specific Set in the user's LEGO collection.  ### Set List logic Because this merges sets found across all Set Lists the fields list_id and include_spares may not be accurate unless the Set actually only exists in a single Set List.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null

try:
    # Get details about a specific Set in the user's LEGO collection.
    api_instance.users_sets_read(user_token, set_num)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_sync_create**
> users_sets_sync_create(user_token, set_num, quantity=quantity, include_spares=include_spares)

Synchronise a user's Sets to the POSTed list.

Synchronise a user's Sets to the POSTed list.  ### Set List logic This is used to completely replace the user's Sets with those in the supplied list. It will remove any Sets in Rebrickable that are not found in the supplied list. It will attempt to keep any current Rebrickable Sets in their existing Set Lists, and will add any new Sets found into the Default Set List for Imports in the user's settings. ### Single Set When adding a single Set, returns the successfully created Set (status 201) or details for why the Set could not be added. ### Multiple Sets To add multiple Sets, POST a JSON list of them (using a Content-Type header of 'application/json'). e.g: `[{\"set_num\":\"8043-1\", \"quantity\": 1}, {\"set_num\":\"8110-1\", \"quantity\": 2, \"include_spares\": \"False\"}]` Returns a list of successfully added Sets. If the Set is unrecognised, it will be skipped.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)
include_spares = 'include_spares_example' # str | null (optional)

try:
    # Synchronise a user's Sets to the POSTed list.
    api_instance.users_sets_sync_create(user_token, set_num, quantity=quantity, include_spares=include_spares)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_sync_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 
 **include_spares** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_sets_update**
> users_sets_update(user_token, set_num, quantity=quantity)

Update an existing Set's quantity in all Set Lists. This PUT call is different to others in that it will create

Update an existing Set's quantity in all Set Lists. This PUT call is different to others in that it will create the Set if it doesn't already exist, and it will delete the Set if you pass a quantity of 0.  ### Set List logic * Default Set List = user's configured default import list or the first alphabetically if none exist. * Increasing quantity = add to Set in default Set List if it exists, else add it there * Decreasing quantity = remove from Set in default Set List first, then from remaining lists until done

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
user_token = 'user_token_example' # str | null
set_num = 'set_num_example' # str | null
quantity = 'quantity_example' # str | null (optional)

try:
    # Update an existing Set's quantity in all Set Lists. This PUT call is different to others in that it will create
    api_instance.users_sets_update(user_token, set_num, quantity=quantity)
except ApiException as e:
    print("Exception when calling UsersApi->users_sets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_token** | **str**| null | 
 **set_num** | **str**| null | 
 **quantity** | **str**| null | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_token_create**
> UsersTokenResponse users_token_create(username, password)

Generate a User Token to be used for authorising user account actions in subsequent calls. Username can be either

Generate a User Token to be used for authorising user account actions in subsequent calls. Username can be either the actual username or the user's email address.

### Example
```python
from __future__ import print_function
import time
import rebrickable
from rebrickable.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKey
configuration = rebrickable.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = rebrickable.UsersApi(rebrickable.ApiClient(configuration))
username = 'username_example' # str | null
password = 'password_example' # str | null

try:
    # Generate a User Token to be used for authorising user account actions in subsequent calls. Username can be either
    api_response = api_instance.users_token_create(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_token_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| null | 
 **password** | **str**| null | 

### Return type

[**UsersTokenResponse**](UsersTokenResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

