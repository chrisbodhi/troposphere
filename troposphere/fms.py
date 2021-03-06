# Copyright (c) 2012-2020, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.


from . import AWSProperty, AWSObject, Tags
from .validators import json_checker, boolean


class IEMap(AWSProperty):
    props = {
        'ACCOUNT': ([basestring], False),
        'ORGUNIT': ([basestring], False),
    }


class Policy(AWSObject):
    resource_type = "AWS::FMS::Policy"

    props = {
        'DeleteAllPolicyResources': (boolean, False),
        'ExcludeMap': (IEMap, False),
        'ExcludeResourceTags': (boolean, True),
        'IncludeMap': (IEMap, False),
        'PolicyName': (basestring, True),
        'RemediationEnabled': (boolean, True),
        'ResourceTags': (Tags, False),
        'ResourceType': (basestring, True),
        'ResourceTypeList': ([basestring], True),
        'SecurityServicePolicyData': (json_checker, True),
        'Tags': (Tags, False),
    }


class NotificationChannel(AWSObject):
    resource_type = "AWS::FMS::NotificationChannel"

    props = {
        'SnsRoleName': (basestring, True),
        'SnsTopicArn': (basestring, True),
    }
