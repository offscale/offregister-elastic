from fabric.contrib.files import append
from fabric.operations import sudo, run

from offregister_fab_utils.ubuntu.systemd import restart_systemd


def install0(**kwargs):
    installed = lambda: run("dpkg-query --showformat='${Version}' --show elasticsearch", quiet=True)

    if sudo('dpkg -s elasticsearch', quiet=True, warn_only=True).failed:
        sudo('wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -')

        append('/etc/apt/sources.list.d/elasticsearch.list',
               'deb http://packages.elasticsearch.org/elasticsearch/{}/debian stable main'.format(
                   kwargs['VERSION'][:kwargs['VERSION'].rfind('.')] if kwargs['VERSION'].count('.') == 3
                   else kwargs['VERSION']
               ),
               use_sudo=True)
        sudo('apt update')
        sudo('apt-get install -y elasticsearch={}'.format(kwargs['VERSION']))
        if kwargs.get('NO_UPGRADE'):
            sudo('apt-mark hold elasticsearch')
        restart_systemd('elasticsearch')

        return 'elasticsearch {} installed'.format(installed())

    return '[Already] elasticsearch {} installed'.format(installed())
