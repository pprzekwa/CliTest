
class CliMock(object):

    @staticmethod
    def to_string(cmd):
        return ' '.join(cmd)

    def execute(self, command):
        cmd = self.to_string(command)
        return {
            'user': 'TAP CLI user',
            'user delete': 'TAP CLI user delete',
            'user invitation': 'TAP CLI user invitation',
            'user invitation resend': 'TAP CLI user invitation resend',
            'user invitation send': 'TAP CLI user invitation send',
            'user invitation delete': 'TAP CLI user invitation delete'
        }[cmd]

