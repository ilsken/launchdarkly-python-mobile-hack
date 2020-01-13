from ldclient.version import VERSION

def _headers(sdk_key, client='PythonClient', with_auth=True):
  return {'Authorization': sdk_key, 'User-Agent': '{0}/{1}'.format(client, VERSION),
            'Content-Type': "application/json"}


