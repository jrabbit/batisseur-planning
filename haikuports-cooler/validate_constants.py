ShellType = shell

class status(str):
    pass

StatusType = status

bep_defaults = {'SRC_URI': [True, None], 'WORKING': [False, True], 'INSTALL': [False, shell()], 'REPLACES': [False, None], 'DEPEND': [False, None], 'LICENSE': [False, None], 'CHECKSUM_MD5': [False, None], 'HOMEPAGE': [True, None], 'STATUS_HAIKU': [False, 'untested'], 'COPYRIGHT': [False, None], 'SUMMARY': [True, None], 'CONFLICTS': [False, None], 'SUPPLEMENTS': [False, None], 'BUILD': [False, shell()], 'DESCRIPTION': [True, None], 'FRESHENS': [False, None], 'PROVIDES': [True, None], 'TEST': [False, shell()], 'MESSAGE': [False, None], 'REVISION': [True, None], 'SOURCE_DIR': [False, None], 'BUILD_DEPEND': [False, None]}

bepTypes = {}
bepTypes['SUMMARY'] = [types.StringType]
bepTypes['DESCRIPTION'] = [types.StringType, types.ListType]
bepTypes['HOMEPAGE'] = [types.StringType]
bepTypes['SRC_URI'] = [types.StringType, types.ListType]
bepTypes['CHECKSUM_MD5'] = [types.StringType]
bepTypes['REVISION'] = [types.IntType]
bepTypes['STATUS_HAIKU'] = [StatusType]
bepTypes['PROVIDES'] = [types.StringType, types.ListType]
bepTypes['DEPEND'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['SUPPLEMENTS'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['CONFLICTS'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['FRESHENS'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['REPLACES'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['BUILD_DEPEND'] = [types.StringType, types.ListType, types.NoneType]
bepTypes['BUILD'] = [ShellType]
bepTypes['INSTALL'] = [ShellType]
bepTypes['TEST'] = [ShellType]
bepTypes['MESSAGE'] = [types.StringType]
bepTypes['LICENSE'] = [types.StringType, types.ListType]
bepTypes['COPYRIGHT'] = [types.StringType, types.ListType]
bepTypes['SOURCE_DIR'] = [types.StringType]