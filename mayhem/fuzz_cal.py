#!/usr/bin/env python3
import atheris
import sys
import io
from contextlib import contextmanager
import logging
# Disable all logging messages
logging.disable(logging.CRITICAL)

from fitz import EmptyFileError, FileDataError

import fuzz_helpers

with atheris.instrument_imports(include=['pdf2docx']):
    from pdf2docx import Converter

from pdf2docx.converter import ConversionException

@contextmanager
def nostdout():
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = io.BytesIO()
    sys.stderr = io.BytesIO()
    yield
    sys.stdout = save_stdout
    sys.stderr = save_stderr
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeTemporaryFile(suffix='.pdf', as_bytes=True) as f, nostdout():
            cv = Converter(f)
            cv.convert('/dev/null')
            cv.close()
    except (FileDataError, EmptyFileError, ConversionException):
        return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
