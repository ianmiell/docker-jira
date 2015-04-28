"""ShutIt module. See http://shutit.tk
"""

from shutit_module import ShutItModule


class docker_jira(ShutItModule):

	def build(self, shutit):
		shutit.install('apache2 postgresql wget openjdk-7-jre')
		shutit.send('mkdir -p /opt/atlassian')
		shutit.send('cd /opt/atlassian')
		f = 'atlassian-jira-6.4.1-x64.bin'
		shutit.get_url(f,['https://www.atlassian.com/software/jira/downloads/binary/'])
		shutit.multisend('sh ./' + f,{', Cancel':'o','Express Install':'1','Install':'i'})
		return True

def module():
	return docker_jira(
		'shutit.tk.docker_jira.docker_jira', 782914092.00,
		description='',
		maintainer='',
		depends=['shutit.tk.setup']
	)

