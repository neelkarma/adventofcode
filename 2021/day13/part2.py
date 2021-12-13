from common import Axis, axis_map, fold_regex


if __name__ == "__main__":
    with open("./input.txt", "r") as input_file:
        # Interpret data
        points_raw, folds_raw = input_file.read().split("\n\n")
        points = set(
            tuple(int(coord) for coord in coords.split(","))
            for coords in points_raw.split("\n")
        )
        folds = []
        for line in folds_raw.split("\n"):
            match = fold_regex.match(line)
            if not match:
                raise ValueError(f"Invalid fold instruction: {line}")
            folds.append((axis_map[match.group(1)], int(match.group(2))))

        # Compute the folds
        for fold_axis, fold_at in folds:
            for x, y in points.copy():
                match fold_axis:
                    case Axis.X:
                        if x > fold_at:
                            new_point = (fold_at - abs(fold_at - x), y)
                            points.remove((x, y))
                            points.add(new_point)
                    case Axis.Y:
                        if y > fold_at:
                            new_point = (x, fold_at - abs(fold_at - y))
                            points.remove((x, y))
                            points.add(new_point)

        # Print the message
        row_str = ""
        max_x = 0
        max_y = 0
        for x, y in points:
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        for y in range(max_y + 1):
            for x in range(max_x + 1):
                if (x, y) in points:
                    row_str += "#"
                    continue
                row_str += " "
            print(row_str)
            row_str = ""
