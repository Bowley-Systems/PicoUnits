<!--
#006d77ff, 
#d92c2aff 
Hello,
PicoUnits only exists because I got annoyed by the 
uncertainty of other unit systems and I wanted a 
language that can encode parameters into it (UnitValues).

I think the final result here is quite reasonable for 
that initial problem. I hope you enjoy using PicoUnits.

William Bowley, 
20th August, 2026

P.S: Thanks for downloading our PicoUnits repository `▽`ʃ♡
-->

<!-- Make sure to update the logo with the github link before release if changed -->

<p align="center">
<img src="media/logo.png" alt="PicoUnits logo" style="width:100%; max-width:100%; display:block;"></p>
</p>
<h4 align="center">A Dynamic Runtime Type System for Dimensional Numerical Quantities.</h4>
<p align="center">
  Define the type. Define the variable. Execute. <br>
  Automate physical meaning throughout your pipeline.
</p>

## Overview

<!--
Make sure to update the coverage value 
(if unit tests are done for the update). 
It is not automatic. 
--> 

![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-006D77?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-60%25-E14F4C?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/picounits?label=downloads\&style=flat-square\&color=006D77)](https://pepy.tech/projects/picounits)

PicoUnits is a dynamic runtime dimensional typing system for numerical quantities. It provides a consistent type system for expressing dimensional quantities throughout your pipeline.

> [!important]
> ### Features:
> - Configurable `unit frames` with custom symbols and dimension ordering
> - Parses `UnitValues` language formats (`.ut`) and unit-informed values (`.uiv`)
> - Numerical support for real, complex, and vector quantities

## Unit conversion is uncertainty

PicoUnits removes uncertainty by reducing the set of units to one canonical set defined by the user.

It does not attempt to answer:

How might one convert between systems at a boundary?
```
3 feet → ? metre (1/3.280839895...?) 
↺ Each iteration
```

Because for computation, this is fundamentally flawed. It destroys certainty for implementation convenience.

```
Define unit frame → Define derived units → Work within it, not outside it.
```


## What is a Unit Frame?

A unit frame defines the dimensional system used by an application.
 
For example:
 
```text
[symbols]
time: s
length: m
mass: kg
current: A
temperature: K
amount: mol
luminosity: cd
dimensionless: ∅
```

The dimensional environment is independent of the notation used to represent it. Hence, any semantic representation can be used. However, PicoUnits operates on a fixed set of fundamental dimensions and prefixes

See the [.picounit](.picounits) file for implementation details.

## What are `.ut` and `.uiv` 

Both are dimensionally aware formats: `.ut` defines custom units, while `.uiv` encodes value:unit pairs.

`.ut` defines the custom units for your unit system:
```
[units]
ρ: kg/m^3                 # Defines the unit for density
```

`.uiv` defines the quantities within your unit system:

```
[model]
inlet_pressure: 101 k(ρ)  # 101 kPa using the defined unit ρ
```
See the [UnitValues repository](https://github.com/Bowley-Systems/UnitValues) for notation and language specification.

## Quick Start
 
```py
from picounits import expects, VOLTAGE, CURRENT, RESISTANCE
 
@expects(VOLTAGE)
def ohm_law(i, r):
    return i * r
 
# Correct Usage
ohm_law(10 * CURRENT, 5 * RESISTANCE) 
# > Output: 50.0 (kg·m²·s⁻³·A⁻¹)

# Incorrect Usage
ohm_law(10 * CURRENT, 5 * VOLTAGE)
# > DimensionError: 'ohm_law' returned kg·m²·s⁻³, expected kg·m²·s⁻³·A⁻¹
```

## Installation 
 
To install:
```bash
pip install PicoUnits
```

### Documentation
 
Documentation is available in [`docs/`](https://github.com/wgbowley/PicoUnits/tree/main/docs), with a standard introduction example available in [`example/`](https://github.com/wgbowley/PicoUnits/tree/main/example).
