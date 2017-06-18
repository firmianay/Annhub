#include <jansson.h>
#include <string.h>
#include <yara/re.h>
#include <yara/modules.h>

#define MODULE_NAME annhub_yara


// permission 结构
struct permissions {
    void* uses_permission;
    void* custom_permission;
};


// 移除字符串中的冒号 ':'
void remove_colon(const char* input, char* output) {
    int i, pos_out=0;

    for(i=0;i<strlen(input)+1;++i) {
        if (input[i] != ':') {
        output[pos_out++] = input[i];
        }
    }
}


// 使用字符串检测 name
define_function(name_lookup_string)
{
    YR_OBJECT* obj = get_object(module(), "name");
    char* value = obj->data;
    uint64_t result = 0;

    if (value) {
        if (strcasecmp(string_argument(1), value) == 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 name
define_function(name_lookup_regex)
{
    YR_OBJECT* obj = get_object(module(), "name");
    char* value = obj->data;
    uint64_t result = 0;

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用字符串检测 package
define_function(package_lookup_string)
{
    YR_OBJECT* package_obj = get_object(module(), "package");
    char* value = package_obj->data;
    uint64_t result = 0;

    if (value) {
        if (strcasecmp(string_argument(1), value) == 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 package
define_function(package_lookup_regex)
{
    YR_OBJECT* package_obj = get_object(module(), "package");
    char* value = package_obj->data;
    uint64_t result = 0;

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 检测 certificate.owner
define_function(certificate_owner_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "owner");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 检测 certificate.issuer
define_function(certificate_issuer_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "issuer");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 检测 certificate.serial_number
define_function(certificate_serial_number_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "serial_number");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 valid_from
define_function(certificate_valid_from_lookup_regex)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "valid_from");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用字符串检测 valid_from
define_function(certificate_valid_from_lookup_string)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;
    val = json_object_get(obj->data, "valid_from");

    if (val != NULL) {
        value = (char *)json_string_value(val);
    }

    if (value != NULL) {
        if (strcasecmp(string_argument(1), value) == 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 valid_until
define_function(certificate_valid_until_lookup_regex)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "valid_until");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用字符串检测 valid_until
define_function(certificate_valid_until_lookup_string)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;
    val = json_object_get(obj->data, "valid_until");

    if (val != NULL) {
        value = (char *)json_string_value(val);
    }
    if (value != NULL) {
        if (strcasecmp(string_argument(1), value) == 0) {
        result = 1;
        }
    }
    return_integer(result);
}


// 检测 certificate.md5
define_function(certificate_md5_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;
    val = json_object_get(obj->data, "md5");
    char *argument = string_argument(1);
    char *cert_str;
    cert_str = (char*)malloc((strlen(argument)+1)*sizeof(char));

    if (cert_str != NULL) {
        remove_colon(argument, cert_str);
    } else {
        return_integer(result);
    }

    if (val) {
        value = (char *)json_string_value(val);
        if (value) {
        if (strcasecmp(cert_str, value) == 0) {
            result = 1;
        }
        }

    }
    free(cert_str);

    return_integer(result);
}


// 检测 certificate.sha1
define_function(certificate_sha1_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;
    val = json_object_get(obj->data, "sha1");
    char *argument = string_argument(1);
    char *cert_str;
    cert_str = (char*)malloc((strlen(argument)+1)*sizeof(char));

    if (cert_str != NULL) {
        remove_colon(argument, cert_str);
    } else {
        return_integer(result);
    }

    if (val) {
        value = (char *)json_string_value(val);
        if (value) {
        if (strcasecmp(cert_str, value) == 0) {
            result = 1;
        }
        }

    }
    free(cert_str);

    return_integer(result);
}


// 检测 certificate.sha256
define_function(certificate_sha256_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;
    val = json_object_get(obj->data, "sha256");
    char *argument = string_argument(1);
    char *cert_str;
    cert_str = (char*)malloc((strlen(argument)+1)*sizeof(char));

    if (cert_str != NULL) {
        remove_colon(argument, cert_str);
    } else {
        return_integer(result);
    }

    if (val) {
        value = (char *)json_string_value(val);
        if (value) {
        if (strcasecmp(cert_str, value) == 0) {
            result = 1;
        }
        }

    }
    free(cert_str);

    return_integer(result);
}


// 检测 certificate.algorithm
define_function(certificate_algorithm_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "algorithm");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 检测 certificate.version
define_function(certificate_version_lookup)
{
    YR_OBJECT* obj = parent();
    char *value = NULL;
    uint64_t result = 0;
    json_t *val;

    val = json_object_get(obj->data, "version");
    if (val) {
        value = (char *)json_string_value(val);
    }

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}



// 检测 uses_permission, custom_permission
define_function(permission_lookup)
{
    YR_OBJECT* obj = get_object(module(), "permission");
    struct permissions *a;

    a = obj->data;
    if (a == NULL) { return_integer(0); }

    json_t* list_u_perms = (json_t*) a->uses_permission;
    json_t* list_c_perms = (json_t*) a->custom_permission;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list_u_perms, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
            result = 1;
            break;
        }
    }
    //或者遍历 custom_permission
    if (!result) {
        json_array_foreach(list_c_perms, index, value)
        {
            if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
            {
                result = 1;
                break;
            }
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 activity
define_function(activity_lookup_regex)
{
    YR_OBJECT* activity_obj = get_object(module(), "activity");
    json_t* list = (json_t*) activity_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 activity
define_function(activity_lookup_string)
{
    YR_OBJECT* activity_obj = get_object(module(), "activity");
    json_t* list = (json_t*) activity_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


//检测 main_activity
define_function(main_activity_lookup)
{
    YR_OBJECT* obj = get_object(module(), "main_activity");
    char* value = obj->data;
    uint64_t result = 0;

    if (value) {
        if (yr_re_match(regexp_argument(1), value) > 0) {
        result = 1;
        }
    }

    return_integer(result);
}


// 使用正则表达式检测 service
define_function(service_lookup_regex)
{
    YR_OBJECT* service_obj = get_object(module(), "service");
    json_t* list = (json_t*) service_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 service
define_function(service_lookup_string)
{
    YR_OBJECT* service_obj = get_object(module(), "service");
    json_t* list = (json_t*) service_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用正则表达式检测 receiver
define_function(receiver_lookup_regex)
{
    YR_OBJECT* receiver_obj = get_object(module(), "receiver");
    json_t* list = (json_t*) receiver_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 receiver
define_function(receiver_lookup_string)
{
    YR_OBJECT* receiver_obj = get_object(module(), "receiver");
    json_t* list = (json_t*) receiver_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用正则表达式检测 provider
define_function(provider_lookup_regex)
{
    YR_OBJECT* provider_obj = get_object(module(), "provider");
    json_t* list = (json_t*) provider_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 provider
define_function(provider_lookup_string)
{
    YR_OBJECT* provider_obj = get_object(module(), "provider");
    json_t* list = (json_t*) provider_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}

// 使用正则表达式检测 intent_filter
define_function(intent_filter_lookup_regex)
{
    YR_OBJECT* intent_filter_obj = get_object(module(), "intent_filter");
    json_t* list = (json_t*) intent_filter_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 intent_filter
define_function(intent_filter_lookup_string)
{
    YR_OBJECT* intent_filter_obj = get_object(module(), "intent_filter");
    json_t* list = (json_t*) intent_filter_obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用正则表达式检测 url
define_function(url_lookup_regex)
{
    YR_OBJECT* obj = get_object(module(), "url");
    json_t* list = (json_t*) obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (yr_re_match(regexp_argument(1), json_string_value(value)) > 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 使用字符串检测 url
define_function(url_lookup_string)
{
    YR_OBJECT* obj = get_object(module(), "url");
    json_t* list = (json_t*) obj->data;

    uint64_t result = 0;
    size_t index;
    json_t* value;

    json_array_foreach(list, index, value)
    {
        if (strcasecmp(string_argument(1), json_string_value(value)) == 0)
        {
        result = 1;
        break;
        }
    }
    return_integer(result);
}


// 申明
begin_declarations;
    declare_function("name", "r", "i", name_lookup_regex);
    declare_function("name", "s", "i", name_lookup_string);

    declare_function("package", "r", "i", package_lookup_regex);
    declare_function("package", "s", "i", package_lookup_string);

    declare_integer("min_sdk");
    declare_integer("max_sdk");
    declare_integer("target_sdk");

    begin_struct("certificate");
        declare_function("owner", "r", "i", certificate_owner_lookup);
        declare_function("issuer", "r", "i", certificate_issuer_lookup);
        declare_function("serial_number", "s", "i", certificate_serial_number_lookup);
        declare_function("valid_from", "r", "i", certificate_valid_from_lookup_regex);
        declare_function("valid_from", "s", "i", certificate_valid_from_lookup_string);
        declare_function("valid_until", "r", "i", certificate_valid_until_lookup_regex);
        declare_function("valid_until", "s", "i", certificate_valid_until_lookup_string);
        declare_function("md5", "s", "i", certificate_md5_lookup);
        declare_function("sha1", "s", "i", certificate_sha1_lookup);
        declare_function("sha256", "s", "i", certificate_sha256_lookup);
        declare_function("algorithm", "s", "i", certificate_algorithm_lookup);
        declare_function("version", "s", "i", certificate_version_lookup);
    end_struct("certificate");

    declare_function("permission", "r", "i", permission_lookup);

    declare_integer("permissions_number");

    declare_function("activity", "r", "i", activity_lookup_regex);
    declare_function("activity", "s", "i", activity_lookup_string);

    declare_function("main_activity", "r", "i", main_activity_lookup);

    declare_function("service", "r", "i", service_lookup_regex);
    declare_function("service", "s", "i", service_lookup_string);

    declare_function("receiver", "r", "i", receiver_lookup_regex);
    declare_function("receiver", "s", "i", receiver_lookup_string);

    declare_function("provider", "r", "i", provider_lookup_regex);
    declare_function("provider", "s", "i", provider_lookup_string)

    declare_function("intent_filter", "r", "i", intent_filter_lookup_regex);
    declare_function("intent_filter", "s", "i", intent_filter_lookup_string);

    declare_function("url", "r", "i", url_lookup_regex);
    declare_function("url", "s", "i", url_lookup_string);
end_declarations;


// 模块初始化
int module_initialize(YR_MODULE* module)
{
    return ERROR_SUCCESS;
}


// 模块结束初始化
int module_finalize(YR_MODULE* module)
{
    return ERROR_SUCCESS;
}


// 模块加载
int module_load(YR_SCAN_CONTEXT* context, YR_OBJECT* module_object, void* module_data, size_t module_data_size)
{
    // 变量定义
    YR_OBJECT* name_obj = NULL;
    YR_OBJECT* package_obj = NULL;
    YR_OBJECT* permission_obj = NULL;
    YR_OBJECT* activity_obj = NULL;
    YR_OBJECT* service_obj = NULL;
    YR_OBJECT* receiver_obj = NULL;
    YR_OBJECT* provider_obj = NULL;
    YR_OBJECT* intent_filter_obj = NULL;
    YR_OBJECT* main_activity_obj = NULL;
    YR_OBJECT* certificate_obj = NULL;
    YR_OBJECT* url_obj = NULL;
    struct permissions *permissions_struct = NULL;

    int version, perms_number;
    json_error_t json_error;
    const char* str_val = NULL;
    json_t* json = NULL;

    if (module_data == NULL)
        return ERROR_SUCCESS;

    json = json_loadb(
        (const char*) module_data,
        module_data_size,
        0,
        &json_error);

    if (json == NULL)
        return ERROR_INVALID_FILE;

    // 将对象赋给变量
    name_obj = get_object(module_object, "name");
    package_obj = get_object(module_object, "package");
    activity_obj = get_object(module_object, "activity");
    main_activity_obj = get_object(module_object, "main_activity");
    service_obj = get_object(module_object, "service");
    receiver_obj = get_object(module_object, "receiver");
    provider_obj = get_object(module_object, "provider");
    permission_obj = get_object(module_object, "permission");
    certificate_obj = get_object(module_object, "certificate");
    intent_filter_obj = get_object(module_object, "intent_filter");
    url_obj = get_object(module_object, "url");

    //设置 min_sdk
    version = 0;
    str_val = json_string_value(json_object_get(json, "min_sdk"));
    if (str_val) {
        version = atoi(str_val);
    } else {
        version = json_integer_value(json_object_get(json, "min_sdk"));
    }
    set_integer(version, module_object, "min_sdk");

    // 设置 max_sdk
    version = 0;
    str_val = json_string_value(json_object_get(json, "max_sdk"));
    if (str_val) {
        version = atoi(str_val);
    } else {
        version = json_integer_value(json_object_get(json, "max_sdk"));
    }
    set_integer(version, module_object, "max_sdk");

    // 设置 target_sdk
    version = 0;
    str_val = json_string_value(json_object_get(json, "target_sdk"));
    if (str_val) {
        version = atoi(str_val);
    } else {
        version = json_integer_value(json_object_get(json, "target_sdk"));
    }
    set_integer(version, module_object, "target_sdk");

    // 设置其他部分
    certificate_obj->data = json_object_get(json, "certificate");
    activity_obj->data = json_object_get(json, "activity");
    service_obj->data = json_object_get(json, "service");
    receiver_obj->data = json_object_get(json, "receiver");
    provider_obj->data = json_object_get(json, "provider");
    intent_filter_obj->data = json_object_get(json, "intent_filter");
    url_obj->data = json_object_get(json, "url");

    //设置 main_activity
    main_activity_obj->data = (char *)json_string_value(json_object_get(json, "main_activity"));

    // 设置 name
    name_obj->data = (char *)json_string_value(json_object_get(json, "name"));

    // 设置 package
    package_obj->data = (char *)json_string_value(json_object_get(json, "package"));

    // 设置 permission
    permissions_struct = malloc(sizeof(struct permissions));
    permissions_struct->uses_permission = (void *)json_object_get(json, "uses_permission");
    permissions_struct->custom_permission = (void *)json_object_get(json, "custom_permission");
    permission_obj->data = permissions_struct;

    // permission 总数
    perms_number = json_array_size(permissions_struct->uses_permission);
    perms_number += json_array_size(permissions_struct->custom_permission);
    set_integer(perms_number, module_object, "permissions_number");

    return ERROR_SUCCESS;
}


// 模块卸载
int module_unload(YR_OBJECT* module)
{
    YR_OBJECT* obj;
    if (module->data != NULL)
        json_decref((json_t*) module->data);

    obj = get_object(module, "permission");
    if (obj != NULL) {
        free(obj->data);
    }

    return ERROR_SUCCESS;
}
