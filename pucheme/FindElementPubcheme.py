def find_all_acc_ids(data):
    """递归查找所有 'Name': 'Accession ID' 对应的值"""
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "Accession ID":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_acc_ids(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_acc_ids(item))

    return results


def find_all_mona_ids(data):
    """递归查找所有 'Name': 'MoNA ID' 对应的值"""
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "MoNA ID":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_mona_ids(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_mona_ids(item))

    return results


def find_all_cenergy(data):
    """递归查找所有 'Name': 'Collision Energy' 对应的值"""
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "Collision Energy":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_cenergy(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_cenergy(item))

    return results


def find_all_rt(data):
    """递归查找所有 'Name': 'Retention Time' 对应的值"""
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "Retention Time":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_rt(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_rt(item))

    return results


def find_all_pm(data):
    """递归查找所有 'Name': 'Precursor m/z' 对应的值"""
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "Precursor m/z":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_pm(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_pm(item))

    return results


def find_all_instrument_type(data):
    """递归查找所有 'Name': 'Instrument Type """
    results = []

    if isinstance(data, dict):
        if data.get("Name") == "Instrument Type":
            value = data.get("Value", {}).get("StringWithMarkup", [{}])[0].get("String")
            if value:
                results.append(value)
        for v in data.values():
            results.extend(find_all_instrument_type(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(find_all_instrument_type(item))

    return results
