# Bug Descriptions

## bug1.py
- **Intended Behavior**: Calculate ROI safely. If investment is 0, return 0.0.
- **Current Issue**: Crashes with `ZeroDivisionError` when investment is 0.

## bug2.js
- **Intended Behavior**: Wait for all database updates to complete, then return the full log.
- **Current Issue**: Returns empty log immediately because `forEach` does not await async callbacks.

## bug3.java
- **Intended Behavior**: Compare string content and handle nulls safely.
- **Current Issue**: Uses `==` (reference comparison) and throws `NullPointerException` on null input.

## bug4.py
- **Intended Behavior**: User settings should override defaults. File must be closed safely.
- **Current Issue**: Defaults overwrite user settings. File handle is leaked (not closed).

## bug5.c
- **Intended Behavior**: Read input safely with bounds checking (max 32 chars).
- **Current Issue**: Uses `gets()`, causing potential Stack Buffer Overflow.

## bug6.php
- **Intended Behavior**: Strict string comparison for tokens.
- **Current Issue**: Uses loose `==` comparison, allowing "Magic Hash" bypass (treating scientific notation strings as floats).
