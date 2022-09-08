import argparse
import base64
import json
import logging
import os
import shutil
import subprocess
import tempfile
from get_chrome import guess_chrome_path
from basic_format import build_resume


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="JSON file contain resume data [resume.json]")
    parser.add_argument("-o", "--output", help="Ouptut file name")
    parser.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("-d", "--debug", action="store_true")
    args = parser.parse_args()
    if args.quiet:
        logging.basicConfig(level=logging.WARN, format="%(message)s")
    elif args.debug:
        logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(message)s")
    return args


def write_pdf(html, prefix):
    chrome = guess_chrome_path()
    html64 = base64.b64encode(html.encode("utf-8"))
    options = [
        "--no-sandbox",
        "--headless",
        "--print-to-pdf-no-header",
        "--enable-logging=stderr",
        "--log-level=2",
        "--in-process-gpu",
        "--disable-gpu",
    ]

    tmpdir = tempfile.mkdtemp(prefix="resume.md_")
    options.append(f"--crash-dumps-dir={tmpdir}")
    options.append(f"--user-data-dir={tmpdir}")

    try:
        subprocess.run(
            [
                chrome,
                *options,
                f"--print-to-pdf={prefix}.pdf",
                "data:text/html;base64," + html64.decode("utf-8"),
            ],
            check=True,
        )
        logging.info(f"Wrote {prefix}.pdf")
    except subprocess.CalledProcessError as exc:
        if exc.returncode == -6:
            logging.warning(
                "Chrome died with <Signals.SIGABRT: 6> " f"but you may find {prefix}.pdf was created successfully."
            )
        else:
            raise exc
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
        if os.path.isdir(tmpdir):
            logging.debug(f"Could not delete {tmpdir}")


def main():
    args = parse_arguments()
    prefix, _ = os.path.splitext(os.path.abspath(args.file))
    print(prefix)
    with open(args.file) as file:
        resume_json = json.load(file)
    html = build_resume(resume_json).render()
    write_pdf(html, prefix=prefix)


if __name__ == "__main__":
    main()
