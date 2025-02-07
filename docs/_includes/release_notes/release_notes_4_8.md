## Firebolt Release Notes - Version 4.8

### New Features

<!-- Auto Generated Markdown for FIR-36620 - Owned by Pascal Schulze -->
**Introduced new bitwise shift functions `BIT_SHIFT_RIGHT` and `BIT_SHIFT_LEFT`**

The following bitwise shift functions are now supported:
* `BIT_SHIFT_RIGHT` shifts the bits of a number to the right by a specified number of positions, which effectively divides the number by `2` for each position shifted.
* `BIT_SHIFT_LEFT` shifts the bits of a number to the left by a specified number of positions, which effectively multiples the number by `2` for each position shifted.


<!-- Auto Generated Markdown for FIR-35769 and FIR-35770 - Owned by Demian Hespe -->
**Introduced new trigonometric functions `ACOS`, `ATAN`, `ASIN`, `COS`, `COT`, `TAN`, `DEGREES`, and `PI`**

The following trigonometric functions are now supported:
* `ACOS` calculates the arccosine of a value in radians.
* `ATAN` calculates the arctangent of a value in radians.
* `ASIN` calculates the arcsine of a value in radians. 
* `COS` calculates the cosine of a value in radians. 
* `COT` calculates the cotangent of a value in radians. 
* `TAN` calculates the tangent of a value in radians. 
* `DEGREES` converts a value in radians to degrees.
* `PI` returns π as a value of type `DOUBLE PRECISION`.

<!-- Auto Generated Markdown for FIR-37293 - Owned by Mosha Pasumansky -->
**Introduced the `timezone` query-level setting with `time_zone` as an alias**

Added the `timezone` query-level setting. The previous `time_zone` query setting still works, and is now an alias for `timezone`.

<!-- Auto Generated Markdown for FIR-35668 - Owned by Kfir Yehuda -->
**Introduced new `PERCENTILE_CONT` and `MEDIAN` aggregate functions**

Added the following aggregate functions:
* `PERCENTILE_CONT` calculates a specified percentile of values in an ordered dataset.
* `MEDIAN` returns the median of a given column. It is equivalent to `PERCENTILE_CONT(0.5)`: half the values in the column are smaller, and half are bigger than the returned value. If the number of values in the column is even, `MEDIAN` returns the arithmetic mean of the two middle values.


**Added support to meet HIPAA regulations for health information**

Added [support to meet federal HIPAA regulations]({% link Overview/Security/security.md %}#hipaa-compliance) to ensure the confidentiality, integrity, and availability of electronic protected health information within the Firebolt platform.

### Performance Improvements

<!-- Auto Generated Markdown for FIR-36922 - Owned by Ori Brostovski -->
**Improved expression comparison logic within queries**

Improved expression comparison logic to better recognize identical expressions within queries. This enhancement supports a broader range of queries and boosts the overall quality of query plans.

<!-- Auto Generated Markdown for FIR-37388 - Owned by Arsenii Krasikov -->
**Improving cold reads by reducing the amount of Amazon S3 requests needed to load data**

Improved the performance of cold reads by minimizing the number of Amazon S3 requests required to load data. In the case of tiny tablets, this improvement lead to a 50% improvement in performance.

### Bug Fixes

<!-- Auto Generated Markdown for FIR-37268 - Owned by Zhen Li -->
**Fixed a bug preventing view creation with type conversions to array types**

Fixed an issue that prevented users from creating database views that involve type conversion to array types.
