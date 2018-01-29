# rebrickable.LegoApi

All URIs are relative to *https://rebrickable.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lego_colors_list**](LegoApi.md#lego_colors_list) | **GET** /api/v3/lego/colors/ | Get a list of all Colors.
[**lego_colors_read**](LegoApi.md#lego_colors_read) | **GET** /api/v3/lego/colors/{id}/ | Get details about a specific Color.
[**lego_elements_read**](LegoApi.md#lego_elements_read) | **GET** /api/v3/lego/elements/{element_id}/ | Get details about a specific Element ID.
[**lego_mocs_parts_list**](LegoApi.md#lego_mocs_parts_list) | **GET** /api/v3/lego/mocs/{set_num}/parts/ | Get a list of all Inventory Parts in this MOC.
[**lego_mocs_read**](LegoApi.md#lego_mocs_read) | **GET** /api/v3/lego/mocs/{set_num}/ | Get details for a specific MOC.
[**lego_part_categories_list**](LegoApi.md#lego_part_categories_list) | **GET** /api/v3/lego/part_categories/ | Get a list of all Part Categories.
[**lego_part_categories_read**](LegoApi.md#lego_part_categories_read) | **GET** /api/v3/lego/part_categories/{id}/ | Get details about a specific Part Category.
[**lego_parts_colors_list**](LegoApi.md#lego_parts_colors_list) | **GET** /api/v3/lego/parts/{part_num}/colors/ | Get a list of all Colors a Part has appeared in.
[**lego_parts_colors_read**](LegoApi.md#lego_parts_colors_read) | **GET** /api/v3/lego/parts/{part_num}/colors/{color_id}/ | Get details about a specific Part/Color combination.
[**lego_parts_colors_sets_list**](LegoApi.md#lego_parts_colors_sets_list) | **GET** /api/v3/lego/parts/{part_num}/colors/{color_id}/sets/ | Get a list of all Sets the Part/Color combination has appeard in.
[**lego_parts_list**](LegoApi.md#lego_parts_list) | **GET** /api/v3/lego/parts/ | Get a list of Parts.
[**lego_parts_read**](LegoApi.md#lego_parts_read) | **GET** /api/v3/lego/parts/{part_num}/ | Get details about a specific Part.
[**lego_sets_alternates_list**](LegoApi.md#lego_sets_alternates_list) | **GET** /api/v3/lego/sets/{set_num}/alternates/ | Get a list of MOCs which are Alternate Builds of a specific Set - i.e. all parts in the MOC can
[**lego_sets_list**](LegoApi.md#lego_sets_list) | **GET** /api/v3/lego/sets/ | Get a list of Sets, optionally filtered by any of the below parameters.
[**lego_sets_parts_list**](LegoApi.md#lego_sets_parts_list) | **GET** /api/v3/lego/sets/{set_num}/parts/ | Get a list of all Inventory Parts in this Set.
[**lego_sets_read**](LegoApi.md#lego_sets_read) | **GET** /api/v3/lego/sets/{set_num}/ | Get details for a specific Set.
[**lego_sets_sets_list**](LegoApi.md#lego_sets_sets_list) | **GET** /api/v3/lego/sets/{set_num}/sets/ | Get a list of all Inventory Sets in this Set.
[**lego_themes_list**](LegoApi.md#lego_themes_list) | **GET** /api/v3/lego/themes/ | Return all Themes
[**lego_themes_read**](LegoApi.md#lego_themes_read) | **GET** /api/v3/lego/themes/{id}/ | Return details for a specific Theme


# **lego_colors_list**
> ArrayOfColors lego_colors_list(page=page, page_size=page_size, ordering=ordering)

Get a list of all Colors.

Get a list of all Colors.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all Colors.
    api_response = api_instance.lego_colors_list(page=page, page_size=page_size, ordering=ordering)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegoApi->lego_colors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **ordering** | **str**| null | [optional] 

### Return type

[**ArrayOfColors**](ArrayOfColors.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_colors_read**
> Color lego_colors_read(id)

Get details about a specific Color.

Get details about a specific Color.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
id = 'id_example' # str | null

try:
    # Get details about a specific Color.
    api_response = api_instance.lego_colors_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegoApi->lego_colors_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| null | 

### Return type

[**Color**](Color.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_elements_read**
> lego_elements_read(element_id)

Get details about a specific Element ID.

Get details about a specific Element ID.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
element_id = 'element_id_example' # str | null

try:
    # Get details about a specific Element ID.
    api_instance.lego_elements_read(element_id)
except ApiException as e:
    print("Exception when calling LegoApi->lego_elements_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element_id** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_mocs_parts_list**
> lego_mocs_parts_list(set_num, page=page, page_size=page_size)

Get a list of all Inventory Parts in this MOC.

Get a list of all Inventory Parts in this MOC.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get a list of all Inventory Parts in this MOC.
    api_instance.lego_mocs_parts_list(set_num, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling LegoApi->lego_mocs_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 
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

# **lego_mocs_read**
> lego_mocs_read(set_num)

Get details for a specific MOC.

Get details for a specific MOC.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null

try:
    # Get details for a specific MOC.
    api_instance.lego_mocs_read(set_num)
except ApiException as e:
    print("Exception when calling LegoApi->lego_mocs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_part_categories_list**
> lego_part_categories_list(page=page, page_size=page_size, ordering=ordering)

Get a list of all Part Categories.

Get a list of all Part Categories.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all Part Categories.
    api_instance.lego_part_categories_list(page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_part_categories_list: %s\n" % e)
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

# **lego_part_categories_read**
> lego_part_categories_read(id)

Get details about a specific Part Category.

Get details about a specific Part Category.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
id = 'id_example' # str | null

try:
    # Get details about a specific Part Category.
    api_instance.lego_part_categories_read(id)
except ApiException as e:
    print("Exception when calling LegoApi->lego_part_categories_read: %s\n" % e)
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

# **lego_parts_colors_list**
> lego_parts_colors_list(part_num, page=page, page_size=page_size, ordering=ordering)

Get a list of all Colors a Part has appeared in.

Get a list of all Colors a Part has appeared in.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
part_num = 'part_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all Colors a Part has appeared in.
    api_instance.lego_parts_colors_list(part_num, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_parts_colors_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_num** | **str**| null | 
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

# **lego_parts_colors_read**
> lego_parts_colors_read(color_id, part_num)

Get details about a specific Part/Color combination.

Get details about a specific Part/Color combination.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
color_id = 'color_id_example' # str | null
part_num = 'part_num_example' # str | null

try:
    # Get details about a specific Part/Color combination.
    api_instance.lego_parts_colors_read(color_id, part_num)
except ApiException as e:
    print("Exception when calling LegoApi->lego_parts_colors_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **lego_parts_colors_sets_list**
> lego_parts_colors_sets_list(color_id, part_num, page=page, page_size=page_size, ordering=ordering)

Get a list of all Sets the Part/Color combination has appeard in.

Get a list of all Sets the Part/Color combination has appeard in.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
color_id = 'color_id_example' # str | null
part_num = 'part_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of all Sets the Part/Color combination has appeard in.
    api_instance.lego_parts_colors_sets_list(color_id, part_num, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_parts_colors_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **color_id** | **str**| null | 
 **part_num** | **str**| null | 
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

# **lego_parts_list**
> lego_parts_list(page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id, bricklink_id=bricklink_id, brickowl_id=brickowl_id, lego_id=lego_id, ldraw_id=ldraw_id, ordering=ordering, search=search)

Get a list of Parts.

Get a list of Parts.  Optionally filter by one or more of the below query parameters.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
part_num = 'part_num_example' # str | null (optional)
part_cat_id = 'part_cat_id_example' # str | null (optional)
color_id = 'color_id_example' # str | null (optional)
bricklink_id = 'bricklink_id_example' # str | null (optional)
brickowl_id = 'brickowl_id_example' # str | null (optional)
lego_id = 'lego_id_example' # str | null (optional)
ldraw_id = 'ldraw_id_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)
search = 'search_example' # str | null (optional)

try:
    # Get a list of Parts.
    api_instance.lego_parts_list(page=page, page_size=page_size, part_num=part_num, part_cat_id=part_cat_id, color_id=color_id, bricklink_id=bricklink_id, brickowl_id=brickowl_id, lego_id=lego_id, ldraw_id=ldraw_id, ordering=ordering, search=search)
except ApiException as e:
    print("Exception when calling LegoApi->lego_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
 **part_num** | **str**| null | [optional] 
 **part_cat_id** | **str**| null | [optional] 
 **color_id** | **str**| null | [optional] 
 **bricklink_id** | **str**| null | [optional] 
 **brickowl_id** | **str**| null | [optional] 
 **lego_id** | **str**| null | [optional] 
 **ldraw_id** | **str**| null | [optional] 
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

# **lego_parts_read**
> lego_parts_read(part_num)

Get details about a specific Part.

Get details about a specific Part.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
part_num = 'part_num_example' # str | null

try:
    # Get details about a specific Part.
    api_instance.lego_parts_read(part_num)
except ApiException as e:
    print("Exception when calling LegoApi->lego_parts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **part_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_sets_alternates_list**
> lego_sets_alternates_list(set_num, page=page, page_size=page_size, ordering=ordering)

Get a list of MOCs which are Alternate Builds of a specific Set - i.e. all parts in the MOC can

Get a list of MOCs which are Alternate Builds of a specific Set - i.e. all parts in the MOC can be found in the Set.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Get a list of MOCs which are Alternate Builds of a specific Set - i.e. all parts in the MOC can
    api_instance.lego_sets_alternates_list(set_num, page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_sets_alternates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 
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

# **lego_sets_list**
> lego_sets_list(page=page, page_size=page_size, theme_id=theme_id, min_year=min_year, max_year=max_year, min_parts=min_parts, max_parts=max_parts, ordering=ordering, search=search)

Get a list of Sets, optionally filtered by any of the below parameters.

Get a list of Sets, optionally filtered by any of the below parameters.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
theme_id = 'theme_id_example' # str | null (optional)
min_year = 'min_year_example' # str | null (optional)
max_year = 'max_year_example' # str | null (optional)
min_parts = 'min_parts_example' # str | null (optional)
max_parts = 'max_parts_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)
search = 'search_example' # str | null (optional)

try:
    # Get a list of Sets, optionally filtered by any of the below parameters.
    api_instance.lego_sets_list(page=page, page_size=page_size, theme_id=theme_id, min_year=min_year, max_year=max_year, min_parts=min_parts, max_parts=max_parts, ordering=ordering, search=search)
except ApiException as e:
    print("Exception when calling LegoApi->lego_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **str**| null | [optional] 
 **page_size** | **str**| null | [optional] 
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

# **lego_sets_parts_list**
> lego_sets_parts_list(set_num, page=page, page_size=page_size)

Get a list of all Inventory Parts in this Set.

Get a list of all Inventory Parts in this Set.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get a list of all Inventory Parts in this Set.
    api_instance.lego_sets_parts_list(set_num, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling LegoApi->lego_sets_parts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 
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

# **lego_sets_read**
> lego_sets_read(set_num)

Get details for a specific Set.

Get details for a specific Set.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null

try:
    # Get details for a specific Set.
    api_instance.lego_sets_read(set_num)
except ApiException as e:
    print("Exception when calling LegoApi->lego_sets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lego_sets_sets_list**
> lego_sets_sets_list(set_num, page=page, page_size=page_size)

Get a list of all Inventory Sets in this Set.

Get a list of all Inventory Sets in this Set.

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
set_num = 'set_num_example' # str | null
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)

try:
    # Get a list of all Inventory Sets in this Set.
    api_instance.lego_sets_sets_list(set_num, page=page, page_size=page_size)
except ApiException as e:
    print("Exception when calling LegoApi->lego_sets_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_num** | **str**| null | 
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

# **lego_themes_list**
> lego_themes_list(page=page, page_size=page_size, ordering=ordering)

Return all Themes

Return all Themes

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
page = 'page_example' # str | null (optional)
page_size = 'page_size_example' # str | null (optional)
ordering = 'ordering_example' # str | null (optional)

try:
    # Return all Themes
    api_instance.lego_themes_list(page=page, page_size=page_size, ordering=ordering)
except ApiException as e:
    print("Exception when calling LegoApi->lego_themes_list: %s\n" % e)
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

# **lego_themes_read**
> lego_themes_read(id)

Return details for a specific Theme

Return details for a specific Theme

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
api_instance = rebrickable.LegoApi(rebrickable.ApiClient(configuration))
id = 'id_example' # str | null

try:
    # Return details for a specific Theme
    api_instance.lego_themes_read(id)
except ApiException as e:
    print("Exception when calling LegoApi->lego_themes_read: %s\n" % e)
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

