<!--
#006d77ff -> deep, muted teal-green 
#d92c2aff -> bold, warm crimson-red 

Thanks for downloading our PicoUnits repository `▽`ʃ♡
- William Bowley (2026/11/01)
-->

<p align="center">
  <img 
    src="https://raw.githubusercontent.com/Bowley-Systems/PicoUnits/refs/heads/main/media/logo.png" 
    alt="Logo" 
    width="700"
  >
</p>

<br>

![Version](https://img.shields.io/badge/Version-1.1.3-006D77?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-E14F4C?style=flat-square)
![Python  Version](https://img.shields.io/badge/Python-3.10%2B-006D77?style=flat-square)
![Coverage](https://img.shields.io/badge/coverage-80%25-E14F4C?style=flat-square)
[![PyPI Downloads](https://img.shields.io/pepy/dt/picounits?label=downloads\&style=flat-square\&color=006D77)](https://pepy.tech/projects/picounits)

<div align="center">
  <table>
    <tr>
      <td style="vertical-align:top; width:50%;">
        <p>
        <b>PicoUnits</b> is a dynamic runtime typing system for numerical dimensional quantities. It provides a consistent type system for expressing dimensional quantities throughout your pipeline.</p>
        <pre><code>"Propagate dimensional type information through your pipeline"</code></pre>
        <br>
        <p>
        <b>Picounits</b> also has a custom domain-specific language called `unit-values` for writing parameters
        externally of python. It is then parsed into dimensional types via an attribute tree that can be used during runtime.
        </p>
        <pre><code>[circuit]
# The current represented as a complex number
current_phasor: 10+1j (A)
current_range: [0, 3] (A)
voltage_range: [5, 12, 24] k(kg*m^2*s^-3*A^-1)
magnet_grade: [0.836, 1.10] M(A/m), (kg*s^-2*A^-1)</code></pre>
      </td>
      <td style="vertical-align:top; width:50%;">
        <img src="./media/01_examples/parser_example.gif" width="400">
      </td>
    </tr>
  </table>
</div>

### Installation 
 
To install:

```bash
pip install PicoUnits
```

#### Documentation

Full documentation is available in the [`docs/`](https://github.com/Bowley-Systems/PicoUnits/tree/main/docs) folder including API reference, changelog, and contributors.

---
