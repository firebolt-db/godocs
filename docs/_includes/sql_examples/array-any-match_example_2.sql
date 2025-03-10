SELECT ARRAY_ANY_MATCH([])          as empty,
    ARRAY_ANY_MATCH([true])         as single_true,
    ARRAY_ANY_MATCH([false])        as single_false,
    ARRAY_ANY_MATCH([NULL])         as single_null ,
    ARRAY_ANY_MATCH([false, NULL])  as false_and_null;