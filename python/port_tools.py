def apply_port_exclusions(include_ports, exclude_ports):
    """
    Returns a new list of low-high port pairs that includes the ports
    specified in include_ports and removes the ports specified in
    exclude_ports.
    :param list include_ports: List of low-high pairs to include
    :param list exclude_ports: List of low-high pairs to exclude
    :return: The new list of ports with exclusions applied
    :rtype: list
    :raises: ValueError: if any low-high pair is invalid
    :raises: TypeError: if any low-high pair is not an integer
    """
    inc_ports = minimized(include_ports)
    exc_ports = minimized(exclude_ports)
    if not inc_ports:
        return inc_ports
    result = list()
    for port in inc_ports:
        low, high = port
        port_range = range(low, high + 1)
        for exc_port in exc_ports:
            ex_low, ex_high = exc_port
            if high < ex_low:
                # this port range is not excluded
                result.append(port)
                break
            elif ex_low <= low and ex_high >= high:
                # this port range is excluded
                break
            if ex_low in port_range:
                if ex_low == low:
                    pass
                else:
                    result.append([low, ex_low - 1])
            if ex_high in port_range:
                if ex_high == high:
                    pass
                else:
                    result.append([ex_high + 1, high])
    return result


def minimized(ports):
    """
    Returns a new list of port low-high pairs minimized so that pairs that
    are adjacent to each other are combined into a single pair
        i.e. minimize([[a, b], [b + 1, c]]) returns [[a, c]]
    and overlapping ranges are reduced to a single range.
    The new list is sorted in ascending order.
    :param list ports: List of low-high pairs to minimize
    :return: The list of minimized ports
    :raises: ValueError if any low-high pair is invalid
    :raises: TypeError if any low-high pair is not an integer
    """
    if ports:
        _validate(ports)
        mini = list()
        sorted_ports = sorted(ports)
        mini.append(sorted_ports.pop(0))
        for pair in sorted_ports:
            previous = mini.pop()
            low, high = previous
            next_low, next_high = pair
            if next_low == high + 1:
                # pairs are adjacent
                mini.append([low, next_high])
            elif next_low == low and next_high == high:
                # pairs are the same
                mini.append([low, high])
            elif next_low < high:
                # pairs overlap
                if next_high > high:
                    mini.append([low, next_high])
                else:
                    mini.append([low, high])
            else:
                mini.append(previous)
                mini.append(pair)
        return mini
    else:
        return ports


def _validate(ports):
    """
    :param list ports: List of low-high pairs to validate
    :raises: ValueError if any low-high pair is invalid
    :raises: TypeError if any low-high pair is not an integer
    """
    for port in ports:
        low, high = port
        if type(low) != int or type(high) != int:
            raise TypeError
        if low > high:
            raise ValueError
