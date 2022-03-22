'''
   Gather a tool's versions / moduleNames
'''


def gatherToolVersions(results):
    # parse the output to group versions and module names of a tool
    tools_collection = {}
    for tool in results:
        if tool[1] not in tools_collection:
            tools_collection[tool[1]] = {}
            tools_collection[tool[1]]['versions'] = set()
            tools_collection[tool[1]]['modulenames'] = set()
        tools_collection[tool[1]]['category'] = tool[3]
        tools_collection[tool[1]]['keywords'] = tool[4]
        tools_collection[tool[1]]['description'] = tool[5]
        tools_collection[tool[1]]['url'] = tool[6]

    # tools_collection will have 3247 tools after grouping
    for tool in results:
        if tool[1] in tools_collection:
            tools_collection[tool[1]]['versions'].add(tool[2])
            tools_collection[tool[1]]['modulenames'].add(tool[7])

    # convert the set to list to make it json serializable
    for tool in tools_collection:
        tools_collection[tool]['versions'] = list(tools_collection[tool]['versions'])
        tools_collection[tool]['modulenames'] = list(tools_collection[tool]['modulenames'])

    return tools_collection
