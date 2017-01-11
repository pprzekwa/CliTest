commands = {
    'user': {
        'expected_message': 'TAP CLI user',
        'command': ['user'],
        'sub_commands': {
            'delete': {
                'expected_message': 'TAP CLI user delete',
                'command': ['user', 'delete'],
            },
            'invitation': {
                'expected_message': 'TAP CLI user invitation',
                'command': ['user', 'invitation'],
                'sub_commands': {
                    'send': {
                        'expected_message': 'TAP CLI user invitation send',
                        'command': ['user', 'invitation', 'send'],
                    },
                    'resend': {
                        'expected_message': 'TAP CLI user invitation resend',
                        'command': ['user', 'invitation', 'resend'],
                    },
                    'delete': {
                        'expected_message': 'TAP CLI user invitation delete',
                        'command': ['user', 'invitation', 'delete'],
                    }
                }
            }
        }
    }
}