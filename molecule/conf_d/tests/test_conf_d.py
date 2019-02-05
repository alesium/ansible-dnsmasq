import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_conf_d_dir(host):
    f = host.file('/etc/dnsmasq.d')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_conf_d_file(host):
    f = host.file('/etc/dnsmasq.d/lala.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
