#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
import importlib
from bambou import exceptions

VSPK = None

DOCUMENTATION = '''
---
module: set_event_log
short_description: Set the sysconfig event log age
options:
  vsd_auth:
    description:
      - VSD credentials to access VSD GUI
    required: true
    default: null
  api_version:
    description:
      - VSD version
    required: true
    default: null
  event_log_age:
    description:
      - The age of the event log to be set
    required: true
    default: null
'''

EXAMPLES = '''
# Set event log age to 7
- set_event_log:
    vsd_auth:
      username: csproot
      password: csproot
      enterprise: csp
      api_url: https://10.0.0.10:8443
    api_version: 5.2.3
    event_log_age: 7
'''


def set_event_log(module, csproot, event_log_age):
    try:
        sysconfig = csproot.system_configs.get_first()
        sysconfig.event_log_entry_max_age = event_log_age
        sysconfig.save()
        module.exit_json(changed=True,
                         result="Event log age set to %s" % event_log_age)

    except exceptions.BambouHTTPError as be:
        module.fail_json(msg="Could not set event log age : %s" % be)
    except Exception as e:
        module.fail_json(msg="Could not set event log age : %s" % e)


def format_api_version(version):
    if version.startswith('5'):
        return ('v5_0')
    else:
        return ('v6')


def get_vsd_session(module, vsd_auth):
    # Format api version
    version = format_api_version(module.params['api_version'])
    global VSPK
    VSPK = importlib.import_module('vspk.{0:s}'.format(version))

    session = VSPK.NUVSDSession(**vsd_auth)
    session.start()
    csproot = session.user
    return csproot


def main():
    arg_spec = dict(
        vsd_auth=dict(required=True, type='dict'),
        api_version=dict(required=True, type='str'),
        event_log_age=dict(required=True, type='str')
    )
    module = AnsibleModule(argument_spec=arg_spec, supports_check_mode=True)

    vsd_auth = module.params['vsd_auth']
    event_log_age = module.params['event_log_age']

    try:
        csproot = get_vsd_session(module, vsd_auth)
    except ImportError:
        module.fail_json(msg='vspk is required for this module, or '
                         'API version specified does not exist.')
        return
    except Exception as e:
        module.fail_json(msg="Could not establish connection to VSD %s" % e)
        return

    set_event_log(module, csproot, event_log_age)


if __name__ == '__main__':
    main()
