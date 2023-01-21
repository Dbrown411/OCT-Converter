from construct import Int32un, PaddedString, Struct

fda_header = Struct(
            "FOCT" / PaddedString(4, "ascii"),
            "FDA" / PaddedString(3, "ascii"),
            "version_info_1" / Int32un,
            "version_info_2" / Int32un,
        )
fda_oct_header = Struct(
            "type" / PaddedString(1, "ascii"),
            "unknown1" / Int32un,
            "unknown2" / Int32un,
            "width" / Int32un,
            "height" / Int32un,
            "number_slices" / Int32un,
            "unknown3" / Int32un,
        )

fda_oct_header_2 = Struct(
            "unknown" / PaddedString(1, "ascii"),
            "width" / Int32un,
            "height" / Int32un,
            "bits_per_pixel" / Int32un,
            "number_slices" / Int32un,
            "unknown" / PaddedString(1, "ascii"),
            "size" / Int32un,
        )

fda_fundus_header = Struct(
            "width" / Int32un,
            "height" / Int32un,
            "bits_per_pixel" / Int32un,
            "number_slices" / Int32un,
            "unknown" / PaddedString(4, "ascii"),
            "size" / Int32un,
            # 'img' / Int8un,
        )