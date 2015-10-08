import os


def get_includes():
    import arduino_library_template
    r"""
    Return the directory that contains the `arduino_library_template` Cython *.hpp and
    *.pxd header files.

    Extension modules that need to compile against `arduino_library_template` should use
    this function to locate the appropriate include directory.

    Notes
    -----
    When using ``distutils``, for example in ``setup.py``.
    ::

        import arduino_library_template
        ...
        Extension('extension_name', ...
                  include_dirs=[...] + arduino_library_template.get_includes())
        ...

    """
    return [os.path.join(os.path.dirname(arduino_library_template.__file__), 'Arduino', 'ArduinoLibraryTemplate')]
