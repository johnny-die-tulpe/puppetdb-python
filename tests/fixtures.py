# These are fixture functions for returning PuppetDB data
def v2():
    return {
        '/nodes': [
            {
                'name': 'host1',
                'deactivated': None,
                'catalog_timestamp': '2013-02-09T21:05:15.663Z',
                'facts_timestamp': '2013-02-09T21:05:15.663Z',
                'report_timestamp': None
            },
            {
                'name': 'host2',
                'deactivated': None,
                'catalog_timestamp': '2013-02-09T21:05:15.663Z',
                'facts_timestamp': '2013-02-09T21:05:15.663Z',
                'report_timestamp': None

            }
        ],
        '/nodes/host1': {
            'name': 'host1',
            'deactivated': None,
            'catalog_timestamp': '2013-02-09T21:05:15.663Z',
            'facts_timestamp': '2013-02-09T21:05:15.663Z',
            'report_timestamp': None
        },
        '/nodes/host1/facts': [
            {
                'certname': 'host1',
                'name': 'architecture',
                'value': 'amd64',
            },
            {
                'certname': 'host1',
                'name': 'domain',
                'value': 'local',
            },
            {
                'certname': 'host1',
                'name': 'ipaddress',
                'value': '1.2.3.4',
            }
        ],
        '/nodes/host1/facts/architecture': [
            {
                'certname': 'host1',
                'name': 'architecture',
                'value': 'amd64',
            }
        ],
        '/nodes/host1/resources': [
            {
                'certname': 'host1',
                'parameters': {
                    'ensure': 'installed',
                },
                'type': 'Class',
                'sourceline': 7,
                'sourcefile': '/etc/foo/bar.pp',
                'exported': False,
                'resource': '1234567890',
            },
        ],
        '/nodes/host1/resources/Class': [
            {
                'certname': 'host1',
                'parameters': {
                    'ensure': 'installed',
                },
                'type': 'Class',
                'sourceline': 7,
                'sourcefile': '/etc/foo/bar.pp',
                'exported': False,
                'resource': '1234567890',
            },
        ],
        '/facts': [
            {
                'certname': 'host1',
                'name': 'puppetversion',
                'value': '3.2.2',
            },
            {
                'certname': 'host2',
                'name': 'puppetversion',
                'value': '2.7.10',
            }
        ],
        '/facts/ipaddress': [
            {
                'certname': 'host1',
                'name': 'ipaddress',
                'value': '10.10.10.11',
            },
            {
                'certname': 'host2',
                'name': 'ipaddress',
                'value': '10.10.10.12',
            }
        ],
        '/facts/kernelversion/3.2.34': [
            {
                'certname': 'host1',
                'name': 'kernelversion',
                'value': '3.2.34',
            }
        ],
    }
