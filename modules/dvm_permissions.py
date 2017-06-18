# -*- coding: utf_8 -*-
DVM_PERMISSIONS = {
    "MANIFEST_PERMISSION": {
        # MESSAGES
        "SEND_SMS" : [ "dangerous", "发送SMS", "允许应用程序发送短信。恶意应用程序可能在没有确认发送的情况下消耗电话资费。" ],
        "SEND_SMS_NO_CONFIRMATION" : [ "signatureOrSystem", "发送SMS", "通过短信应用程序在没有用户输入或确认的情况下发送短信。" ],
        "RECEIVE_SMS" : [ "dangerous", "接收SMS", "允许应用程序接收和处理短信。恶意的应用程序可以监视或删除你的信息，而不显示给你。" ],
        "RECEIVE_MMS" : [ "dangerous", "接收MMS", "允许应用程序接收和处理彩信。恶意的应用程序可以监视你的消息或在你看到消息之前删除它们。" ],
        "RECEIVE_EMERGENCY_BROADCAST" : [ "signatureOrSystem", "", "允许应用程序接收紧急小区广播消息，以将其记录或显示给用户。 保留用于系统应用程序。" ],
        "READ_CELL_BROADCASTS" : [ "dangerous", "接收小区广播消息", "允许应用程序读取先前接收的小区广播消息，并注册内容观察器以在已接收单元广播并将其添加到数据库时获得通知。 对于紧急警报，在呈现警报对话和通知声音/振动/语音之后立即更新数据库。 然后，在用户关闭警报后，更新“读取”列。 这使得辅助紧急援助应用能够在首次接收到警报时开始加载附加的紧急信息（如果因特网接入可用），并且延迟向用户呈现信息，直到初始警报对话被解除之后。"],
        "READ_SMS" : [ "dangerous", "读取SMS或MMS", "允许应用程序读取存储在您的手机或SIM卡上的短信。恶意应用程序可以读取您的机密信息。" ],
        "WRITE_SMS" : [ "dangerous", "编辑SMS或MMS", "允许应用程序记录在您手机或SIM卡上存储的短信。恶意应用程序可以删除您的消息。" ],
        "RECEIVE_WAP_PUSH" : [ "dangerous", "接收WAP", "允许应用程序接收和处理WAP消息。 恶意应用程式可能会监控您的邮件或将其删除，而不向您显示。" ],
        "BROADCAST_SMS" : [ "signature", "发送已收到短信的广播", "允许应用程序广播通知已收到某条短信。恶意应用程序可以凭此权限伪造传入的短信。" ],
        "BROADCAST_WAP_PUSH" : [ "signature", "发送WAP-PUSH接收的广播", "允许应用程序广播通知：WAP-PUSH消息已收到。恶意的应用程序可以使用这个伪造MMS消息的接收凭证或悄悄利用恶意变种替换任何网页的内容。" ],

        # SOCIAL_INFO
        "READ_CONTACTS" : [ "dangerous", "读取联系人数据", "允许应用程序读取存储在您手机上的所有联系人（地址）数据。恶意应用程序可凭此权限将数据发送给其他人。" ],
        "WRITE_CONTACTS" : [ "dangerous", "写入联系人资料", "允许应用程序修改存储在您手机上的联系人（地址）数据。恶意应用程序可以用此来删除或修改您的联系人数据。" ],
        "BIND_DIRECTORY_SEARCH" : [ "signatureOrSystem", "执行联系人目录搜素", "允许应用程序执行联系人目录搜索。仅由联系人程序使用。" ],
        "READ_CALL_LOG": [ "dangerous", "读取用户通话记录", "允许应用程序读取用户通话记录。" ],
        "WRITE_CALL_LOG": [ "dangerous", "写入（但不读取）用户联系人数据", "允许应用程序写入（但不读取）用户的联系人数据。" ],
        "READ_SOCIAL_STREAM" : [ "dangerous", "从用户的社交流读取", "允许应用程序从用户的社交流读取。" ],
        "WRITE_SOCIAL_STREAM" : [ "dangerous", "写入用户的社交流", "允许应用程序写入（但不读取）用户的社交流数据。" ],

        # PERSONAL_INFO
        "READ_PROFILE" : [ "dangerous", "读取用户的个人资料数据", "允许应用程序读取用户的个人资料数据。" ],
        "WRITE_PROFILE" : [ "dangerous", "写入用户的个人资料数据", "允许应用程序写入（但不读取）用户的个人资料数据。" ],
        "RETRIEVE_WINDOW_CONTENT": [ "signatureOrSystem", "", "允许应用程序检索活动窗口的内容活动窗口是已触发辅助功能事件的窗口。" ],
        "BIND_APPWIDGET" : [ "signatureOrSystem" , "选择窗口小部件" , "允许应用程序告诉系统哪些窗口小部件可以由哪个应用程序使用，使用此权限，应用程序可以授权其他应用程序访问个人数据。不适用于正常应用。" ],
        "BIND_KEYGUARD_APPWIDGET" : [ "signatureOrSystem", "", "私人权限，限制谁可以打开一个对话框来添加一个新的键盘小部件。" ],

        # CALENDAR
        "READ_CALENDAR" : [ "dangerous" , "读取日历活动" , "允许应用程序读取手机上存储的所有日历活动。恶意应用可以使用此功能将您的日历活动发送给其他人。" ],
        "WRITE_CALENDAR": [ "dangerous" , "添加或修改日历活动并向邀请对象发送电子邮件" , "允许应用程序添加或更改日历中可能向访客发送电子邮件的活动，否则恶意应用可能使用此功能删除或修改您的日历活动或向客人发送电子邮件。" ],

        # USER_DICTIONARY
        "READ_USER_DICTIONARY" : [ "dangerous" , "读取用户定义的字典" , "允许应用程序读取用户可能已经存储在用户字典中的任何私人单词，名称和短语。" ],
        "WRITE_USER_DICTIONARY" : [ "normal" , "写入用户定义的字典" , "允许应用程序写入新词到用户字典。" ],

        # BOOKMARKS
        "READ_HISTORY_BOOKMARKS" : [ "dangerous" , "读取浏览器的历史记录和书签" , "允许应用程序读取浏览器访问过的所有URL和所有浏览器的书签。" ],
        "WRITE_HISTORY_BOOKMARKS" : [ "dangerous" , "写入浏览器的历史记录和书签" , "允许应用程序修改存储在手机上的浏览器历史记录或书签。恶意应用可以使用此功能擦除或修改浏览器的数据。" ],

        # DEVICE_ALARMS
        "SET_ALARM" : [ "normal" , "在闹钟应用中设置闹钟" , "允许应用程序在已安装的闹钟应用程序中设置闹钟。" ],

        # VOICEMAIL
        "ADD_VOICEMAIL" : [ "dangerous", "将语音邮件添加到系统", "允许应用程序将语音邮箱添加到系统中。" ],

        # LOCATION
        "ACCESS_FINE_LOCATION" : [ "dangerous" , "精确（GPS）位置" , "访问手机上的全球定位系统等精确位置来源（如果可用）。恶意应用可以使用此功能确定您的位置。" ],
        "ACCESS_COARSE_LOCATION" : [ "dangerous" , "粗略（基于网络）的位置" , "访问粗略的位置来源（如移动网络数据库），以确定可用的大致电话位置。恶意应用可以使用此功能确定您的位置。" ],
        "ACCESS_MOCK_LOCATION" : [ "dangerous" , "模拟测试位置源" , "创建用于测试的模拟位置来源。恶意应用可以使用此功能覆盖实际位置来源（如GPS或网络提供商）返回的位置。" ],
        "ACCESS_LOCATION_EXTRA_COMMANDS" : [ "normal" , "访问额外的位置提供者命令" , "访问额外的位置提供者命令。恶意应用可以使用此功能来干扰GPS或其他位置源的操作。" ],
        "INSTALL_LOCATION_PROVIDER" : [ "signatureOrSystem" , "安装位置提供程序的权限" , "创建模拟位置源进行测试。恶意应用可以使用此功能来覆盖由实时位置源（如GPS或网络）返回的位置，或者监视和报告您的位置到外部来源。" ],

        # NETWORK
        "INTERNET" : [ "dangerous" , "访问互联网" , "允许应用程序创建网络套接字。" ],
        "ACCESS_NETWORK_STATE" : [ "normal" , "查看网络状态" , "允许应用程序查看所有网络的状态。" ],
        "ACCESS_WIFI_STATE" : [ "normal" , "查看Wi-Fi状态" , "允许应用程序查看有关Wi-Fi状态的信息。" ],
        "CHANGE_WIFI_STATE" : [ "dangerous" , "更改Wi-Fi状态" , "允许应用程序连接到Wi-Fi接入点和断开连接并更改已配置的Wi-Fi网络。" ],
        "CHANGE_NETWORK_STATE" : [ "normal" , "更改网络连接" , "允许应用程序更改网络连接的状态。" ],
        "ACCESS_WIMAX_STATE": [ "normal", "", "" ],
        "CHANGE_WIMAX_STATE": [ "dangerous", "", "" ],
        "NFC" : [ "dangerous" , "控制近场通信" , "允许应用于近场通信（NFC）标签，卡和读卡器通信。" ],
        "CONNECTIVITY_INTERNAL": [ "signatureOrSystem", "使用有特权的连接管理API", "允许内部用户使用有特权的连接管理API。" ],
        "RECEIVE_DATA_ACTIVITY_CHANGE": [ "signatureOrSystem", "", "" ],

        # BLUETOOTH_NETWORK
        "BLUETOOTH" : [ "dangerous" , "创建蓝牙连接" , "允许应用程序查看本地蓝牙手机的配置，并和接受配对的设备连接。" ],
        "BLUETOOTH_ADMIN" : [ "dangerous" , "蓝牙管理" , "允许应用程序配置本地蓝牙手机，并发现和配对远程设备。" ],

        # SYSTEM TOOLS
        "BLUETOOTH_STACK": [ "signature", "", "" ],
        "NET_ADMIN": [ "signature", "配置网络接口，配置和使用IPSec等", "允许访问配置网络接口，配置和使用IPSec等。" ],
        "REMOTE_AUDIO_PLAYBACK": [ "signature", "远程音频播放", "允许远程音频播放" ],
        "READ_EXTERNAL_STORAGE" : [ "normal", "外部存储器读取", "允许应用程序读取外部存储器。" ],
        "INTERACT_ACROSS_USERS": [ "signatureOrSystemOrDevelopment", "", "允许应用程序调用API，以允许其通过设备上的用户进行交互，使用单一服务和用户定向广播。此权限不适用于第三方应用程序。" ],
        "INTERACT_ACROSS_USERS_FULL": [ "signature", "", "完全形式的INTERACT_ACROSS_USERS，删除了对发送广播的位置的限制，并允许其他类型的交互。" ],
        "MANAGE_USERS": [ "signatureOrSystem", "", "允许应用程序调用允许其查询和管理设备上的用户的API。此权限不适用于第三方应用。" ],
        "GET_DETAILED_TASKS": [ "signature", "", "允许应用程序获取有关最近运行的任务的全部细节信息。" ],
        "START_ANY_ACTIVITY": [ "signature", "", "允许应用程序启动任何活动，无论权限保护或导出状态如何。" ],
        "SET_SCREEN_COMPATIBILITY": [ "signature", "", "更改应用程序的屏幕兼容性模式。" ],
        "CHANGE_CONFIGURATION" : [ "signatureOrSystemOrDevelopment" , "更改UI设置" , "允许应用程序更改当前配置，如区域设置或整体字体大小。" ],
        "FORCE_STOP_PACKAGES" : [ "signature" , "强制停止其他应用程序" , "允许应用程序强行停止其他应用程序。" ],
        "SET_ANIMATION_SCALE" : [ "signatureOrSystemOrDevelopment" , "修改全局动画速度" , "允许应用程序随时更改全局动画速度。" ],
        "GET_PACKAGE_SIZE" : [ "normal" , "测量应用程序存储空间" , "允许应用程序检索其代码，数据和告诉缓存大小。" ],
        "SET_PREFERRED_APPLICATIONS" : [ "signature" , "设置首选应用程序" , "允许应用程序修改您的首选应用程序。恶意应用可以以静默方式更改允许的应用程序，欺骗您的现有应用程序从而收集您的私人数据。" ],
        "BROADCAST_STICKY" : [ "normal" , "发送粘性广播" , "允许应用程序发送在广播结束后依然保留的粘性广播。恶意应用可以使用此功能消耗太多内存使手机变慢或不稳定。" ],
        "MOUNT_UNMOUNT_FILESYSTEMS" : [ "signatureOrSystem" , "装载和卸载文件系统" , "允许应用程序装载和卸载可移动存储的文件系统。" ],
        "MOUNT_FORMAT_FILESYSTEMS" : [ "signatureOrSystem" , "格式化外部存储" , "允许应用程序格式化可移动存储。" ],
        "ASEC_ACCESS" : [ "signature" , "获取内部存储信息" , "允许应用程序获取内部存储信息。" ],
        "ASEC_CREATE" : [ "signature" , "创建内部存储" , "允许应用程序创建内部存储。" ],
        "ASEC_DESTROY" : [ "signature" , "销毁内部存储" , "允许应用程序销毁内部存储。" ],
        "ASEC_MOUNT_UNMOUNT" : [ "signature" , "装载和卸载内部存储" , "允许应用程序装载和卸载内部存储。" ],
        "ASEC_RENAME" : [ "signature" , "重命名内部存储" , "允许应用程序重命名内部存储。" ],
        "WRITE_APN_SETTINGS" : [ "signatureOrSystem" , "写访问点名称设置" , "允许应用程序修改APN设置，如任何APN的代理和端口。" ],
        "SUBSCRIBED_FEEDS_READ" : [ "normal" , "阅读订阅的Feed" , "允许应用程序接收有关当前已同步的Feed的详细信息。" ],
        "SUBSCRIBED_FEEDS_WRITE" : [ "dangerous" , "写入订阅的Feed" , "允许应用程序修改您当前已同步的Feed。恶意应用可以使用此功能更改已同步的Feed。" ],
        "CLEAR_APP_CACHE" : [ "dangerous" , "删除所有应用程序缓存数据" , "允许应用程序通过删除应用程序缓存目录中的文件来释放手机存储空间。访问通常严格局限于系统进程。" ],
        "DIAGNOSTIC" : [ "signature" , "读写diag拥有的资源" , "允许应用程序读取和写入diag组拥有的任何资源，这可能会影响系统稳定性和安全性。" ],
        "BROADCAST_PACKAGE_REMOVED" : [ "signature" , "发送包删除广播" , "允许应用程序广播一个应用程序包已删除的通知。恶意应用可以使用此功能杀死任何正在运行的应用程序。" ],
        "BATTERY_STATS" : [ "dangerous" , "修改电池统计信息" , "允许修改收集的电池统计信息。不适用于正常的应用程序。" ],
        "MODIFY_APPWIDGET_BIND_PERMISSIONS" : [ "signatureOrSystem", "查询和设置那些应用程序可以绑定AppWidgets", "允许应用程序查询和设置那些应用程序可以绑定AppWidgets的内部权限。" ],
        "CHANGE_BACKGROUND_DATA_SETTING" : [ "signature" , "更改后台数据使用设置" , "允许应用程序更改后台数据使用设置。" ],
        "GLOBAL_SEARCH" : [ "signatureOrSystem" , "" , "此权限可用于内容提供者，允许全局搜索系统来访问数据。此权限不适用于常规应用程序；它由应用程序使用以保护自己不受全局搜索以外的影响。" ],
        "GLOBAL_SEARCH_CONTROL" : [ "signature" , "" , "保护对全局搜索系统的访问的内部权限，确保只有系统可以访问提供者以执行查询并编写搜索统计信息。" ],
        "SET_WALLPAPER_COMPONENT" : [ "signatureOrSystem" , "设置动态壁纸" , "允许应用程序设置动态壁纸。" ],
        "READ_DREAM_STATE" : [ "signature", "", "允许应用程序读取梦想设置和梦想状态。" ],
        "WRITE_DREAM_STATE" : [ "signature", "", "允许应用程序写入梦想设置，并开始或停止梦想" ],
        "WRITE_SETTINGS" : [ "normal" , "修改全局系统设置" , "允许应用程序修改系统的设置数据。恶意应用可以使用此功能损坏系统的配置。" ],

        # ACCOUNTS
        "GET_ACCOUNTS" : [ "normal" , "发现已知账户" , "允许应用程序访问手机已知的账户列表。" ],
        "AUTHENTICATE_ACCOUNTS" : [ "dangerous" , "充当账户认证者" , "允许应用程序使用账户管理器的账户认证功能，包括创建账户以及获取和设置其密码。" ],
        "USE_CREDENTIALS" : [ "dangerous" , "使用账户的身份验证凭据" , "允许应用程序请求身份验证令牌。" ],
        "MANAGE_ACCOUNTS" : [ "dangerous" , "管理账户列表" , "允许应用程序执行添加和删除账户和删除其密码等操作。" ],
        "ACCOUNT_MANAGER" : [ "signature" , "充当账户管理器服务" , "允许应用程序拨打电话到账户验证器。" ],

        # AFFECTS_BATTERY
        "CHANGE_WIFI_MULTICAST_STATE" : [ "dangerous" , "允许Wi-Fi多播接收" , "允许应用程序接收不直接寻址到您的设备的数据包。这在发现附近提供的服务时很有用。它使用比非多播模式更多的功率。" ],
        "VIBRATE" : [ "normal" , "控制振动器" , "允许应用程序控制振动器。" ],
        "FLASHLIGHT" : [ "normal" , "控制手电筒" , "允许应用程序控制手电筒。" ],
        "WAKE_LOCK" : [ "normal" , "防止手机睡眠" , "允许应用程序阻止手机进入睡眠状态。" ],

        # AUDIO_SETTINGS
        "MODIFY_AUDIO_SETTINGS" : [ "normal" , "更改音频设置" , "允许应用程序修改全局音频设置。" ],

        # HARDWARE_CONTROLS
        "MANAGE_USB": [ "signatureOrSystem", "管理USB设备的首选项和权限", "允许应用程序管理USB设备的首选项和权限。" ],
        "ACCESS_MTP": [ "signatureOrSystem", "访问MTP USB内核驱动程序", "允许应用程序访问MTP USB内核驱动程序，仅供设备端MTP实现使用。" ],
        "HARDWARE_TEST" : [ "signature" , "测试硬件" , "允许应用程序控制各种外设以进行硬件测试。" ],

        # MICROPHONE
        "RECORD_AUDIO" : [ "dangerous" , "录制音频" , "允许应用程序访问音频录制路径。" ],

        # CAMERA
        "CAMERA" : [ "dangerous" , "拍照和视频" , "允许应用程序使用相机拍照和录像，这允许应用程序收集相机在任何时候拍到的图像。" ],

        # PHONE_CALLS
        "PROCESS_OUTGOING_CALLS" : [ "dangerous" , "拦截去电" , "允许应用程序处理去电呼叫和更改要拨打的号码。恶意应用可以使用此功能监视，重定向或阻止来电。" ],
        "MODIFY_PHONE_STATE" : [ "signatureOrSystem" , "修改电话状态" , "允许应用程序修改电话状态。不包括拨打电话。" ],
        "READ_PHONE_STATE" : [ "dangerous" , "读取手机和身份" , "允许应用程序访问设备的电话功能。具有此权限的应用程序可以确定手机的电话号码和序列号，活动状态，呼叫连接的号码等" ],
        "READ_PRIVILEGED_PHONE_STATE": [ "signatureOrSystem", "读取访问特权电话状态", "允许读取特权电话状态的权限" ],
        "CALL_PHONE" : [ "dangerous" , "直接呼叫电话号码" , "允许应用程序发起电话呼叫，而无需通过拨号器界面让用户确认正在呼叫。" ],
        "USE_SIP" : [ "dangerous" , "拨打接听互联网电话" , "允许应用程序使用SIP服务拨打和接听互联网电话。" ],

        # STORAGE
        "WRITE_EXTERNAL_STORAGE" : [ "dangerous" , "修改和删除SD卡内容" , "允许应用程序写入SD卡。" ],
        "WRITE_MEDIA_STORAGE": [ "signatureOrSystem", "写入内部媒体存储", "允许应用程序写入内部媒体存储。" ],

        # SCREENLOCK
        "DISABLE_KEYGUARD" : [ "dangerous" , "禁用键锁定" , "允许应用程序禁用键锁定和任何关联的密码安全。" ],

        # APP_INFO
        "GET_TASKS" : [ "dangerous" , "检索正在运行的应用程序" , "允许应用程序检索有关当前和最近运行的任务的信息。可能允许恶意应用程序发现其他应用程序的私人信息。" ],
        "REORDER_TASKS" : [ "normal" , "重新排序应用程序运行" , "允许应用程序将任务移动到前台和后台。恶意应用可以强制自己在前面，而无需您的控制。" ],
        "REMOVE_TASKS": [ "signature", "", "允许应用程序删除和杀死任务" ],
        "RESTART_PACKAGES" : [ "normal" , "杀死后台进程" , "允许应用程序杀死其他应用程序的后台进程，即使内存不低。" ],
        "KILL_BACKGROUND_PROCESSES" : [ "normal" , "杀死后台进程" , "允许应用程序杀死其他应用程序的后台进程，即使内存不低。" ],
        "PERSISTENT_ACTIVITY" : [ "normal" , "使应用程序总是运行" , "允许应用程序使其部分自身持久化，以便系统不能将其用于其他应用程序。" ],
        "RECEIVE_BOOT_COMPLETED" : [ "normal" , "在启动时自动启动" , "允许应用程序在系统完成启动后立即自行启动，这可能需要较长时间启动手机，并允许应用程序减慢整体手机总是运行。" ],

        # DISPLAY
        "SYSTEM_ALERT_WINDOW" : [ "dangerous" , "显示系统级警报" , "允许应用程序显示系统警报窗口。恶意应用程序可以接管电话的整个屏幕。" ],

        # WALLPAPER
        "SET_WALLPAPER" : [ "normal" , "设置壁纸" , "允许应用程序设置系统壁纸。" ],
        "SET_WALLPAPER_HINTS" : [ "normal" , "设置壁纸大小提示" , "允许应用程序设置系统壁纸大小提示。" ],

        # SYSTEM_CLOCK
        "SET_TIME_ZONE" : [ "normal" , "设置时区" , "允许应用程序更改手机时区。" ],

        # STATUS_BAR
        "EXPAND_STATUS_BAR" : [ "normal" , "展开/折叠状态栏" , "允许应用程序展开或折叠状态栏。" ],

        # SYNC_SETTINGS
        "READ_SYNC_SETTINGS" : [ "normal" , "读取同步设置" , "允许应用程序读取同步设置。" ],
        "WRITE_SYNC_SETTINGS" : [ "normal" , "写入同步设置" , "允许应用程序修改同步设置。" ],
        "READ_SYNC_STATS" : [ "normal" , "读取同步统计" , "允许应用程序读取同步统计信息。" ],

        # DEVELOPMENT_TOOLS
        "WRITE_SECURE_SETTINGS" : [ "signatureOrSystemOrDevelopment" , "修改安全系统设置" , "允许应用程序修改系统的安全设置数据。不适用于正常应用程序。" ],
        "DUMP" : [ "signatureOrSystemOrDevelopment" , "检索系统内部状态" , "允许应用程序检索系统的内部状态。恶意应用可以检索他们通常不需要的各种私人和安全信息。" ],
        "READ_LOGS" : [ "signatureOrSystemOrDevelopment" , "读取敏感日志数据" , "允许应用程序从系统中读取各种日志文件，这允许它发现有关您正在使用手机做什么的一般信息，可能包括个人或私人信息。" ],
        "SET_DEBUG_APP" : [ "signatureOrSystemOrDevelopment" , "启用应用程序调试" , "允许应用程序打开其他应用程序的调试，恶意应用可以使用此来杀死其他应用程序。" ],
        "SET_PROCESS_LIMIT" : [ "signatureOrSystemOrDevelopment" , "限制运行进程数" , "允许应用程序控制将运行的进程的最大数量。正常应用程序不需要。" ],
        "SET_ALWAYS_FINISH" : [ "signatureOrSystemOrDevelopment" , "关闭所有后台应用程序" , "允许应用程序控制活动是否总是在转到背景时完成。正常应用程序不需要。" ],
        "SIGNAL_PERSISTENT_PROCESSES" : [ "signatureOrSystemOrDevelopment" , "向应用程序发送Linux信号" , "允许应用程序请求将所提供的信号发送到所有持久进程。" ],
        "ACCESS_ALL_EXTERNAL_STORAGE"   : [ "signature", "", "允许应用程序访问所有多用户外部存储设备。" ],

        # No groups ...
        "SET_TIME": [ "signatureOrSystem" , "set time" , "允许应用程序更改手机的时钟时间。" ],
        "ALLOW_ANY_CODEC_FOR_PLAYBACK": [ "signatureOrSystem", "", "允许应用程序在解码时使用任何媒体解码器进行播放。" ],
        "STATUS_BAR" : [ "signatureOrSystem" , "禁用或修改状态栏" , "允许应用程序禁用状态栏或添加和删除系统图标。" ],
        "STATUS_BAR_SERVICE" : [ "signature" , "状态栏" , "允许应用程序成为状态栏。" ],
        "FORCE_BACK" : [ "signature" , "强制应用程序关闭" , "允许应用程序强制任何处于前台的活动关闭和回归。正常应用程序不需要。" ],
        "UPDATE_DEVICE_STATS" : [ "signatureOrSystem" , "修改电池统计" , "允许应用程序修改收集的电池统计信息，不适用于正常应用。" ],
        "INTERNAL_SYSTEM_WINDOW" : [ "signature" , "显示未授权的窗口" , "允许应用程序创建旨在由内部系统用户界面使用的窗口。不适用于正常应用程序。" ],
        "MANAGE_APP_TOKENS" : [ "signature" , "管理应用程序令牌" , "允许应用程序创建和管理自己的令牌，绕过其正常的Z顺序。正常应用程序不应该需要。" ],
        "FREEZE_SCREEN": [ "signature", "", "允许应用程序临时冻结屏幕以进行全屏转换。" ],
        "INJECT_EVENTS" : [ "signature" , "注入用户事件" , "允许应用程序将用户时间注入事件流并将它们提交到任何窗口。没有此权限，您只能传递到自己进程中的窗口。很少由应用程序需要此权限。" ],
        "FILTER_EVENTS": [ "signature", "", "允许应用程序注册输入过滤器，它们在分派到任何窗口之前过滤用户事件流。" ],
        "RETRIEVE_WINDOW_INFO" : [ "signature", "", "允许应用程序从窗口管理器检索窗口的信息。" ],
        "TEMPORARY_ENABLE_ACCESSIBILITY": [ "signature", "", "允许应用程序临时启用设备上的辅助功能。" ],
        "MAGNIFY_DISPLAY": [ "signature", "", "允许应用程序放大显示内容。" ],
        "SET_ACTIVITY_WATCHER" : [ "signature" , "监视和控制所有应用程序启动" , "允许应用程序监视和控制系统如何启动活动。恶意应用完全可能危害系统。此权限只限开发，永远不需要正常的手机使用。" ],
        "SHUTDOWN" : [ "signatureOrSystem" , "部分关闭" , "使活动管理器进入关闭状态，不执行完全关闭。" ],
        "STOP_APP_SWITCHES" : [ "signatureOrSystem" , "防止应用程序开关" , "阻止用户切换到另一个应用程序。" ],
        "READ_INPUT_STATE" : [ "signature" , "记录您输入的内容和操作" , "允许应用程序观看您按下的键，即使在其他应用程序交互（如输入密码）。一般应用不需要。" ],
        "BIND_INPUT_METHOD" : [ "signature" , "绑定到输入法" , "允许持有者绑定到输入法的顶级接口。一般应用不需要。" ],
        "BIND_ACCESSIBILITY_SERVICE" : [ "signature", "", "必须由android.accessibilityservice.AccessibilityService要求，以确保只有系统才能绑定到它。" ],
        "BIND_TEXT_SERVICE" : [ "signature", "", "必须由TextService要求，以确保只有系统才能绑定到它。" ],
        "BIND_VPN_SERVICE" : [ "signature", "", "必须是{@link android.net.VpnService}要求的，以确保只有系统才能绑定到它。" ],
        "BIND_WALLPAPER" : [ "signatureOrSystem" , "绑定到壁纸" , "允许持有者绑定到壁纸的顶级界面。一般应用不需要。" ],
        "BIND_DEVICE_ADMIN" : [ "signature" , "与设备管理员交互" , "允许持有者向设备管理员发送意向。一般应用不需要。" ],
        "SET_ORIENTATION" : [ "signature" , "改变屏幕方向" , "允许应用程序随时改变屏幕旋转。一般应用不需要。" ],
        "SET_POINTER_SPEED" : [ "signature", "", "允许低级别访问设置指针速度。一般应用不需要。" ],
        "SET_KEYBOARD_LAYOUT" : [ "signature", "", "允许低级别访问设置键盘布局。一般应用不需要。" ],
        "INSTALL_PACKAGES" : [ "signatureOrSystem" , "直接安装应用程序" , "允许应用程序安装新的或更新应用包。恶意应用可以使用它来添加具有任意强大的权限的新应用程序。" ],
        "CLEAR_APP_USER_DATA" : [ "signature" , "删除其他应用程序的数据" , "允许应用程序清楚用户数据。" ],
        "DELETE_CACHE_FILES" : [ "signatureOrSystem" , "删除其他应用程序的缓存" , "允许应用程序删除缓存文件。" ],
        "DELETE_PACKAGES" : [ "signatureOrSystem" , "删除应用程序" , "允许应用程序删除程序包。恶意应用可以使用它删除重要的应用程序。" ],
        "MOVE_PACKAGE" : [ "signatureOrSystem" , "移动应用程序资源" , "允许应用程序将应用程序资源从内部媒体移动到外部媒体，反之亦可。" ],
        "CHANGE_COMPONENT_ENABLED_STATE" : [ "signatureOrSystem" , "启用或禁用应用程序组件" , "允许应用程序更改是否启用其他应用程序的组件。恶意应用可借此停用重要的电话功能。" ],
        "GRANT_REVOKE_PERMISSIONS" : [ "signature", "", "允许应用程序缓存或撤销特定权限。" ],
        "ACCESS_SURFACE_FLINGER" : [ "signature" , "访问SurfaceFlinger" , "允许应用程序使用SurfaceFlinger低级功能。" ],
        "READ_FRAME_BUFFER" : [ "signatureOrSystem" , "读取帧缓冲区" , "允许应用程序读取帧缓冲区的内容。" ],
        "CONFIGURE_WIFI_DISPLAY" : [ "signature", "", "允许应用程序配置和连接到Wi-Fi显示器。" ],
        "CONTROL_WIFI_DISPLAY" : [ "signature", "", "允许应用程序控制Wi-Fi显示器的低级功能。仅限显示管理器使用。" ],
        "BRICK" : [ "signature" , "永久禁用手机" , "允许应用程序永久禁用手机。这是非常危险的。" ],
        "REBOOT" : [ "signatureOrSystem" , "强制手机重启" , "允许应用程序强制重启手机。" ],
        "DEVICE_POWER" : [ "signature" , "打开或关闭手机" , "允许应用程序打开或关闭手机。" ],
        "NET_TUNNELING" : [ "signature", "", "允许低级访问tun tap驱动程序。" ],
        "FACTORY_TEST" : [ "signature" , "在出厂测试模式下运行" , "作为低级制造商测试运行，允许完全访问手机硬件。仅当手机在制造商测试模式下运行。" ],
        "MASTER_CLEAR" : [ "signatureOrSystem" , "重置为出厂默认设置" , "允许应用程序将系统完全重置为出厂设置，擦除所有数据，配置和安装的应用程序。" ],
        "CALL_PRIVILEGED" : [ "signatureOrSystem" , "直接呼叫任何电话号码" , "允许应用程序呼叫任何电话号码，包括紧急号码。恶意应用可能会对紧急服务进行不必要和非法的呼叫。" ],
        "PERFORM_CDMA_PROVISIONING" : [ "signatureOrSystem" , "直接启动CDMA" , "允许应用程序启动CDMA配置。恶意应用可以不必要地启动CDMA配置。" ],
        "CONTROL_LOCATION_UPDATES" : [ "signatureOrSystem" , "控制位置更新通知" , "允许从无线电启动/禁用位置更新通知。一般应用不需要。" ],
        "ACCESS_CHECKIN_PROPERTIES" : [ "signatureOrSystem" , "访问签入属性" , "允许读取/写入由登记服务上传的属性。一般应用不需要。" ],
        "PACKAGE_USAGE_STATS" : [ "signatureOrSystem" , "更新组件使用情况统计信息" , "允许读取/写入由登记服务上传的属性。不适用于一般应用。" ],
        "BACKUP" : [ "signatureOrSystem" , "控制系统备份和恢复" , "允许应用程序控制系统的备份和恢复。一般应用不需要。" ],
        "CONFIRM_FULL_BACKUP" : [ "signature", "", "允许包启动安全完整备份确认UI。只有系统进程可以保存此权限。" ],
        "BIND_REMOTEVIEWS" : [ "signatureOrSystem", "", "必须是{@link android.widget.RemoteViewsService}，以确保只有系统能绑定到它。" ],
        "ACCESS_CACHE_FILESYSTEM" : [ "signatureOrSystem" , "访问缓存文件系统" , "允许应用程序读取和写入缓存文件系统。" ],
        "COPY_PROTECTED_DATA" : [ "signature" , "允许调用默认容器服务来复制内容。 不适用于正常应用。" , "允许调用默认容器服务来复制内容。 不适用于正常应用。" ],
        "CRYPT_KEEPER" : [ "signatureOrSystem", "访问加密方法", "保护访问加密方法的内部权限。" ],
        "READ_NETWORK_USAGE_HISTORY" : [ "signatureOrSystem", "读取特定网络和应用的历史网络使用", "允许应用程序读取特定网络和应用的历史网络使用。"],
        "MANAGE_NETWORK_POLICY": [ "signature", "管理网络策略并定义应用程序特定的规则", "允许应用程序管理网络策略并定义应用程序特定的规则。"],
        "MODIFY_NETWORK_ACCOUNTING" : [ "signatureOrSystem", "管理其他UID账户的网络流量", "允许应用程序对其他UID账户的网络流量进行管理"],
        "C2D_MESSAGE" : [ "signature" , "C2DM权限" , "C2DM权限。" ],
        "PACKAGE_VERIFICATION_AGENT" : [ "signatureOrSystem", "包验证者需要此权限以获得包管理器的信任从而进行包验证", "包验证者需要此权限以获得包管理器的信任从而进行包验证。"],
        "BIND_PACKAGE_VERIFIER" : [ "signature", "", "必须由包验证接受者所要求，以确保只有系统可以与它交互。"],
        "SERIAL_PORT" : [ "signature", "", "允许应用程序通过SeriaManager访问串行端口。" ],
        "ACCESS_CONTENT_PROVIDERS_EXTERNALLY": [ "signature", "", "允许应用程序从Application Thread外部存取内容提供者。此权限由相应API上的ActivityManagerService强制执行。"],
        "UPDATE_LOCK" : [ "signatureOrSystem", "", "允许应用程序持有UpdateLock，建议在锁被持有时无头OTA不要重启。"],
        "WRITE_GSERVICES" : [ "signatureOrSystem" , "修改Google服务地图" , "允许应用程序修改Google服务地图。不适用于普通应用。" ],
        "ACCESS_USB" : [ "signatureOrSystem" , "访问USB设备" , "允许应用程序访问USB设备。" ],
    },

    "MANIFEST_PERMISSION_GROUP": {
        "ACCOUNTS": "直接访问由账户管理器管理的帐户的权限。",
        "AFFECTS_BATTERY": "用于提供对设备上对电池寿命有影响的硬件的直接访问的权限。包括振动器，手电筒等。",
        "APP_INFO": "与安装在系统上的其他应用程序相关的权限组。",
        "AUDIO_SETTINGS": "用于提供对扬声器设置直接访问设备的权限。",
        "BLUETOOTH_NETWORK": "用于通过蓝牙访问其他设备的权限。",
        "BOOKMARKS": "用于提供访问用户书签和浏览器历史记录的权限。",
        "CALENDAR": "用于提供访问设备日历以创建/查看活动的权限。",
        "CAMERA": "用于与访问摄像机或从设备捕获图像/视频相关联的权限。",
        "COST_MONEY": "用于可用于使用户在没有他们直接参与的情况下花钱的权限。",
        "DEVICE_ALARMS": "用于提供对用户语音信箱的访问权限",
        "DEVELOPMENT_TOOLS": "与开发功能相关的权限组。",
        "DISPLAY": "允许操作另一个应用程序如何向用户显示UI的权限组。",
        "HARDWARE_CONTROLS": "用于提供对设备上的硬件的直接访问的权限。",
        "LOCATION": "用于允许访问用户当前位置的权限。",
        "MESSAGES": "用于允许应用程序代表用户发送消息或截取用户接收的消息的权限。",
        "MICROPHONE": "用于与从设备访问麦克风音频相关联的权限。请注意，电话呼叫也捕获音频，但在一个单独的（更可见的）权限组。",
        "NETWORK": "用于提供访问网络服务的权限。",
        "PERSONAL_INFO": "用于提供访问用户的私人数据（例如联系人，日历活动，电子邮件等）的权限。",
        "PHONE_CALLS": "用于与访问和修改电话状态相关联的权限：拦截呼出，读取和修改电话状态。",
        "STORAGE": "与SD卡访问相关的权限组。",
        "SOCIAL_INFO": "用于提供访问用户的社交连接（例如联系人，通话记录，社交流等）的权限。这包括读取和写入此数据（通常应表示为两个不同的权限）。",
        "SCREENLOCK": "与屏幕锁相关的权限组。",
        "STATUS_BAR": "用于更改状态栏的权限。",
        "SYSTEM_CLOCK": "与系统时钟相关的权限组。.",
        "SYSTEM_TOOLS": "与系统API相关的权限组。",
        "SYNC_SETTINGS": "用于访问同步设置或同步相关信息的权限。",
        "USER_DICTIONARY": "用于提供对用户日历的访问权限以创建/查看活动。",
        "VOICEMAIL": "用于提供访问用户语音信箱的权限。",
        "WALLPAPER": "允许操作其他应用程序如何向用户显示UI的权限组。",
        "WRITE_USER_DICTIONARY": "用于提供对用户日历的访问以创建/查看事件的权限。",
    },
}
