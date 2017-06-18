# -*- coding: utf_8 -*-
"""
四大组件攻击面分析
"""
# TODO
from xml.dom import minidom

def attack_surface(manifest):
    manifest_text = open(manifest).read()
    manifest_xml = minidom.parseString(manifest_text)

    applications = manifest_xml.getElementsByTagName("application")
    activities = manifest_xml.getElementsByTagName("activity")
    services = manifest_xml.getElementsByTagName("service")
    receivers = manifest_xml.getElementsByTagName("receiver")
    providers = manifest_xml.getElementsByTagName("provider")

    for activity in activities:
        if activity.getAttribute("android:exported"):
            if activity.getAttribute("android:exported").lower() == "true":
                if activity.getAttribute("android:permission"):
                    print(activity.getAttribute("android:permission"))
                intents = activity.getAttribute("intent-filter")
                schemes = []
                mimes = []
                hosts = []
                paths = []
                if intents:
                    for intent in intents:
                        data = intent.getElementsByTagName("data")
                        if data:
                            for d in data:
                                if d.getAttribute("android:scheme"):
                                    schemes.append(d.getAttribute("android:scheme"))
                                if d.getAttribute("android:mimeType"):
                                    mimes.append(d.getAttribute("android:mimeType"))
                                if d.getAttribute("android:host"):
                                    hosts.append(d.getAttribute("android:host"))
                                if d.getAttribute("android:path"):
                                    paths.append(d.getAttribute("android:path"))
                    schemes = list(set(schemes))
                    mimes = list(set(mimes))
                    hosts = list(set(hosts))
                    paths = list(set(paths))
                    print(schemes, mimes, hosts, paths)
            elif activity.getAttribute("android:exported") == "false":
                continue
        else:
            continue

    for service in services:
        if service.getAttribute("android:exported"):
            if service.getAttribute("android:exported").lower() == "true":
                if service.getAttribute("android:permission"):
                    print(service.getAttribute("android:permission"))
                intents = service.getAttribute("intent-filter")
                schemes = []
                mimes = []
                hosts = []
                paths = []
                if intents:
                    for intent in intents:
                        data = intent.getElementsByTagName("data")
                        if data:
                            for d in data:
                                if d.getAttribute("android:scheme"):
                                    schemes.append(d.getAttribute("android:scheme"))
                                if d.getAttribute("android:mimeType"):
                                    mimes.append(d.getAttribute("android:mimeType"))
                                if d.getAttribute("android:host"):
                                    hosts.append(d.getAttribute("android:host"))
                                if d.getAttribute("android:path"):
                                    paths.append(d.getAttribute("android:path"))
                    schemes = list(set(schemes))
                    mimes = list(set(mimes))
                    hosts = list(set(hosts))
                    paths = list(set(paths))
                    print(schemes, mimes, hosts, paths)
            elif service.getAttribute("android:exported") == "false":
                continue
        else:
            continue

    for receiver in receivers:
        if receiver.getAttribute("android:exported"):
            if receiver.getAttribute("android:exported").lower() == "true":
                if receiver.getAttribute("android:permission"):
                    print(receiver.getAttribute("android:permission"))
                intents = receiver.getAttribute("intent-filter")
                schemes = []
                mimes = []
                hosts = []
                paths = []
                if intents:
                    for intent in intents:
                        data = intent.getElementsByTagName("data")
                        if data:
                            for d in data:
                                if d.getAttribute("android:scheme"):
                                    schemes.append(d.getAttribute("android:scheme"))
                                if d.getAttribute("android:mimeType"):
                                    mimes.append(d.getAttribute("android:mimeType"))
                                if d.getAttribute("android:host"):
                                    hosts.append(d.getAttribute("android:host"))
                                if d.getAttribute("android:path"):
                                    paths.append(d.getAttribute("android:path"))
                    schemes = list(set(schemes))
                    mimes = list(set(mimes))
                    hosts = list(set(hosts))
                    paths = list(set(paths))
                    print(schemes, mimes, hosts, paths)
            elif receiver.getAttribute("android:exported") == "false":
                continue
        else:
            continue

    for provider in providers:
        if provider.getAttribute("android:exported"):
            if provider.getAttribute("android:exported").lower() == "true":
                if provider.getAttribute("android:permission"):
                    print(provider.getAttribute("android:permission"))
                intents = provider.getAttribute("intent-filter")
                schemes = []
                mimes = []
                hosts = []
                paths = []
                if intents:
                    for intent in intents:
                        data = intent.getElementsByTagName("data")
                        if data:
                            for d in data:
                                if d.getAttribute("android:scheme"):
                                    schemes.append(d.getAttribute("android:scheme"))
                                if d.getAttribute("android:mimeType"):
                                    mimes.append(d.getAttribute("android:mimeType"))
                                if d.getAttribute("android:host"):
                                    hosts.append(d.getAttribute("android:host"))
                                if d.getAttribute("android:path"):
                                    paths.append(d.getAttribute("android:path"))
                    schemes = list(set(schemes))
                    mimes = list(set(mimes))
                    hosts = list(set(hosts))
                    paths = list(set(paths))
                    print(schemes, mimes, hosts, paths)
            elif provider.getAttribute("android:exported") == "false":
                continue
        else:
            continue

    debuggable = ''
    allowBackup = ''
    testOnly = ''
    for application in applications:
        debuggable = application.getAttribute("android:debuggable")
        allowBackup = application.getAttribute("android:allowBackup")
        testOnly = application.getAttribute("android:testOnly")

    check_dic = {
        'debuggable' : debuggable,
        'allowBackup' : allowBackup,
        'testOnly' : testOnly
    }

    return check_dic
