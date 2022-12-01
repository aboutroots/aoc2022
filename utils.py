def file_to_lines(day, separate_with_empty=False):
    if day is None:
        raise AttributeError('you forgot about the day... again!')
    lines = []
    filename = f'inputs/{day}.txt'

    if not separate_with_empty:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines

    with open(filename, 'r') as file:
        # row may consist of data from multiple lines
        current_row = []
        for line in file:
            line_stripped = line.strip()
            if len(line_stripped):
                current_row.append(line_stripped)
            else:
                # we found an empty line
                row_joined = ' '.join(current_row)
                lines.append(row_joined)
                current_row = []

        # add the last missing row that had no chance of being added
        if len(current_row):
            row_joined = ' '.join(current_row)
            lines.append(row_joined)

        return lines
