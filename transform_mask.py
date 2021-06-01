def space_split(i):
    return i.split(" ")


def read_mask_string(mask_string):
    return map(
        lambda x: map(percentage_to_float, x), map(space_split, mask_string.split(","))
    )


def write_mask_string(mask):
    return ",".join(
        list(
            map(
                lambda x: f"{float_to_percentage(x[0])} {float_to_percentage(x[1])}",
                mask,
            )
        )
    )


def percentage_to_float(arg):
    return float(arg[:-1])


def float_to_percentage(arg):
    return str(arg) + "%"


def transform_point(point):
    x, y = tuple(point)
    return (x / 16 * 9 + (100-100/16*9)/2, y / 12 * 9 + (100-100/12*9)/2)


clip_mask = read_mask_string(
    "0% 9%,0% 81%,9% 81%,9% 90%,18% 90%,18% 99%,81% 99%,81% 90%,90% 90%,90% 81%,99% 81%,99% 9%,90% 9%,90% 0%,72% 0%,72% 9%,63% 9%,63% 18%,36% 18%,36% 9%,27% 9%,27% 0%,9% 0%,9% 9%,9% 9%"
)

transformed_clip_mask = map(transform_point, clip_mask)

print(write_mask_string(transformed_clip_mask))
