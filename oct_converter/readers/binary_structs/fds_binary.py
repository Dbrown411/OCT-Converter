from construct import Int32un, PaddedString, Struct

fds_header = Struct(
            "FOCT" / PaddedString(4, "ascii"),
            "FDA" / PaddedString(3, "ascii"),
            "version_info_1" / Int32un,
            "version_info_2" / Int32un,
        )
fds_oct_header = Struct(
            "unknown" / PaddedString(1, "ascii"),
            "width" / Int32un,
            "height" / Int32un,
            "bits_per_pixel" / Int32un,
            "number_slices" / Int32un,
            "unknown" / PaddedString(1, "ascii"),
            "size" / Int32un,
        )
fds_fundus_header = Struct(
            "width" / Int32un,
            "height" / Int32un,
            "bits_per_pixel" / Int32un,
            "number_slices" / Int32un,
            "unknown" / PaddedString(1, "ascii"),
            "size" / Int32un,
        )