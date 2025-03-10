SELECT ARRAY_ALL_MATCH([])          as empty,
    ARRAY_ALL_MATCH([true])         as single_true,
    ARRAY_ALL_MATCH([false])        as single_false,
    ARRAY_ALL_MATCH([NULL])         as single_null ,
    ARRAY_ALL_MATCH([false, NULL])  as false_and_null;