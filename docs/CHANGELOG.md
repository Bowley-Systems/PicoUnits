# Changelog

All notable changes to PicoUnits will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

*(ISO-DATE is used for all updates)*

---

### [1.0.6-1.0.8] - 2026-07-24

#### Added
- `.picounits` configuration file inheritance for base symbols and order
- Unit tests for extensions: construction, deserialization, syntax
- New `extensions/core` module structure with `construction.py`, `deserialization.py`, `syntax.py`
- Validation for derived unit imports (only one `.ut` file allowed)
- Lowercase names for all constant prefixes, dimensions, and quantities

#### Changed
- Major refactor of `DynamicLoader` with identity behaviour
- Refactored `Parser` class for better maintainability and traceability
- Improved module search path for users
- Renamed `unit_validator` module to `expects`
- Better error messages for parsing failures
- Improved prefix extraction from `prefix(unit)` syntax
- Enhanced parentheses handling for quantities

#### Fixed
- Reciprocal unit scaling error
- Squared scaling for length (instead of linear scaling)
- Area notation inconsistencies
- Missing format key warning handling
- Column-wise prefix extraction for lists

#### Documentation
- Improved logo with dark/light mode support
- New color palettes

---

### [1.0.9] - 2026-08-21

#### Added
- Custom loader structures for `.uiv` parsing
- Exposed the node attribute name within the API
- Parser passes the file stem to the loader to use as name
- `.fundamental` for exposing raw dimensions for debugging
- Implemented section and key attribute checking
- Implemented duplicate section detection
- Implemented errors and warning codes from UnitValues specification document

#### Changed
- Changed the `unit_test` folder to `tests` in `/src`
- Limited strings to quoted strings, aligning with UnitValues language specification

#### Fixed
- Enabled constants to show up in the API promises for PicoUnits
- Fixed array quantities in `.uiv` parsing to allow them to have dimensions

#### Documentation
- Added a contributors file rather than using `README.md` in `/docs`
- Added an API reference document implemented in LaTeX in `/docs`

---

### [1.1.0] - 2026-09-07

#### Added
- Non-prefixed integration for real-packets with matplotlib
- Non-prefixed integration for array-packets with matplotlib
- `[numerical]` section to `.picounits` with `significant_figures`
- Implemented significant figures from `.picounits` at runtime

### Removed
- Deprecated `MAX_EXPONENT` constant from `/configurations`

#### Changed
- Improved the `.picounits` file

#### Fixed
- Reordered the dimensional ordering for the `.picounits` file to reflect SI/metric ordering.
- Single unit arrays without prefixes in .uiv files.

#### Documentation
- Added prefix set to `/docs` and also reformated `/docs` section
- Improved the readme and reformatted it.

---