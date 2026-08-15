<!-- 
Color palette: 
#006d77ff, 
#d92c2aff 
-->
 
<p align="center">
  <a href="https://raw.githubusercontent.com/wgbowley/PicoUnits/main/media/picounit_logo.png">
    <img src="https://raw.githubusercontent.com/wgbowley/PicoUnits/main/media/picounit_logo.png" alt="PicoUnits logo">
  </a>
</p>
<p align="center">A dimensional constraint system for computational engineering.</p>
<p align="center">
  Define the dimensional environment of your application.<br>
  Keep physical meaning attached to computation.
</p>

---
 
![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![Python Version](https://img.shields.io/badge/Python-3.10%2B-006D77?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/picounits?label=downloads\&style=flat-square\&color=E14F4C)](https://pepy.tech/projects/picounits)
 
> [!NOTE]
> PicoUnits is the dimensional environment underlying `PyFea`, `PicoMaterials`, and other cross-domain engineering projects.
 
### Overview

Here we go again! Version 1.1.0 lets go.

### Aims:
- 70% unit test coverage
- Get the error list from `unitValues` into the `parser` 
- Get everything in order for `PicoMaterials` (Perhaps even concurrent development at ~17th onwards)
- Write a more concise version of the implementation and reference `unitValues` instead of having a leaky readme.
- Finish up on the 2026-08-24 and release 1.1.0
- Finish most of the issues below: (Will remove over time.)

Finish a lot of these issues:
- fundamental for qualities to expose the raw dimensions instead of any derived units
- Custom dynamic loaders structures for .uiv parsing
- Readme fix, forgot ### features in the overview of the readme
- Fix arrays such that they can encoded with dimensions other than just dimensionless
- Enable constants to show up in text editors when doing from picounits import
- Conversion layer that handles multiple vector representations
- Unit test coverage for picounits: Objective 100%
- Add better static resolve for methods
- Support trigonometric functions for complex scalars