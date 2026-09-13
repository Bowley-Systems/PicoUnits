# pylint: skip-file
""" Filename: loader.py """

# pylint: skip-file
""" Filename: loader.py """

import io
import unittest
from contextlib import redirect_stdout

from picounits import LENGTH

from picounits.extensions.loader import Loader, DynamicLoader, LoaderContext
from picounits.utilities.errors import AttributeNotFound, InjectionError


def _out(func, *args, **kwargs):
    """ Runs func with the given args and returns captured string. """
    buf = io.StringIO()
    with redirect_stdout(buf):
        func(*args, **kwargs)

    return buf.getvalue()


class TestLoaderContext(unittest.TestCase):
    """ Unit tests for LoaderContext """
    def test_next_level(self):
        """ next_level builds indent based on in_last """
        self.assertEqual(LoaderContext(in_last=True).next_level().indent, "    ")
        self.assertEqual(LoaderContext(in_last=False).next_level().indent, "│   ")

    def test_connector(self):
        """ connector picks the right tree character """
        self.assertEqual(LoaderContext(in_last=True).connector(), "└── ")
        self.assertEqual(LoaderContext(in_last=False).connector(), "├── ")

    def test_with_last(self):
        """ with_last updates only the last flag """
        ctx = LoaderContext(indent="  ", in_last=True).with_last(False)
        self.assertEqual(ctx.indent, "  ")
        self.assertFalse(ctx.in_last)


class TestLoader(unittest.TestCase):
    """ Unit tests for Loader """
    def test_flat_attributes(self):
        """ Flat keys become direct attributes """
        loader = Loader({"a": 1, "b": 2})
        self.assertEqual((loader.a, loader.b), (1, 2))

    def test_nested_attributes(self):
        """ Dotted keys create nested Loaders """
        loader = Loader({"a.b.c": 7})
        self.assertEqual(loader.a.b.c, 7)

    def test_dict_value_becomes_loader(self):
        """ Dict values are converted into Loaders """
        loader = Loader({"cfg": {"x": 1}})
        self.assertIsInstance(loader.cfg, Loader)
        self.assertEqual(loader.cfg.x, 1)

    def test_missing_attribute(self):
        """ Missing attributes raise AttributeNotFound """
        with self.assertRaises(AttributeNotFound):
            _ = Loader({"a": 1}).nope

    def test_repr_unnamed(self):
        """ Unnamed repr uses Paths(...) form """
        self.assertEqual(repr(Loader({"a": 1})), "Paths(a)")

    def test_repr_named(self):
        """ Named repr uses name(...) form """
        self.assertEqual(repr(Loader({"a": 1}, name="root")), "root(a)")

    def test_info_scalar_and_nested(self):
        """ info prints scalars and recurses into nested loaders """
        output = _out(Loader({"a": 1, "n.m": 2}, name="root").info)
        self.assertIn("root:.", output)
        self.assertIn("a: 1", output)
        self.assertIn("m: 2", output)

    def test_info_small_list_inline(self):
        """ Small lists print inline """
        output = _out(Loader({"items": [1, 2]}).info)
        self.assertIn("items: [1, 2]", output)

    def test_info_large_list_multiline(self):
        """ Large lists print as multi-line collections """
        output = _out(Loader({"items": [1, 2, 3, 4, 5, 6]}).info)
        self.assertIn("items: [", output)

    def test_info_large_vector_multiline(self):
        """ Large lists print as multi-line collections """
        output = _out(Loader({"items": [1, 2, 3, 4, 5, 6, 7, 8] * LENGTH}).info)
        self.assertIn("items: [", output)

    def test_info_tuple(self):
        """ Tuples are printed as collections """
        output = _out(Loader({"items": (1, 2, 3)}).info)
        self.assertIn("items:", output)


class TestDynamicLoader(unittest.TestCase):
    """ Unit tests for DynamicLoader """
    def test_find_single(self):
        """ find returns a direct attribute """
        self.assertEqual(DynamicLoader({"a": 1}).find("a"), 1)

    def test_find_nested(self):
        """ find traverses a dotted path """
        self.assertEqual(DynamicLoader({"a.b.c": 7}).find("a.b.c"), 7)

    def test_find_missing(self):
        """ find returns None for missing paths """
        self.assertIsNone(DynamicLoader({"a": 1}).find("nope"))

    def test_inject_new(self):
        """ inject adds a nested attribute """
        loader = DynamicLoader({})
        loader.inject("a.b.c", 42)
        self.assertEqual(loader.a.b.c, 42)

    def test_inject_error(self):
        """ inject wraps failures as InjectionError """
        with self.assertRaises(InjectionError):
            DynamicLoader({}).inject(123, "value")


if __name__ == '__main__':
    unittest.main()