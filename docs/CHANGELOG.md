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
- New colour palettes

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
- Updated the formatting for the `.info()` tree structure for dynamic loaders

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
- Non-prefixed integration for real packets with matplotlib
- Non-prefixed integration for array packets with matplotlib
- `[version]` section to `.picounits` with `format` (0.1.0)
- `[numerical]` section to `.picounits` with `significant_figures`
- Implemented significant figures from `.picounits` at runtime
- Implemented unit frame injection for large applications
- Implemented first semantic loading of ordering and symbols
- Implemented column-wise array quantities for multi-unit, single-row quantities
- Implemented `resolve_derived` to pull derived units from the working directory more easily

#### Removed
- Deprecated `MAX_EXPONENT` constant from `/configurations`
- Ordering and symbols are no longer loaded from root `__init__.py`

#### Changed
- Improved the `.picounits` file
- Moved unit boundary functions and the `validator` function into one module
- Moved all custom error messages into one module

#### Fixed
- Reordered the dimensional ordering for the `.picounits` file to reflect SI/metric ordering
- Single-unit arrays without prefixes in `.uiv` files
- Improved the static type hinting of quantities via improving the `.pyi` implementation

#### Documentation
- Added prefix set to `/docs` and also reformatted the `/docs` section
- Improved the README and reformatted it

---

### [1.1.1] - 2026-09-14

#### Added
- `.info()` for quantity construction trace / construction representation at endpoint
- `.info()` for `.uiv` files now can represent vector arrays across multiple lines
- Introduction for quantity trace debugging within `introduction.py` tutorial
- `PURE` = PicoUnits runtime error for consistent error outputs
- `PUPE` = PicoUnits parser error, and `PUPW` = PicoUnits parser warning for consistent errors
- `80%` unit test support and `100%` unit test support for the parser
- Support for modulus between two real number packets

#### Changed
- Renamed the `example` folder to `tutorial`, as it was never really an example anyway

#### Fixed
- Fixed dynamic loader indexation of arrays within the tree for `.info()` of `.uiv` files

#### Documentation
*(TBD) — Work in progress*

---