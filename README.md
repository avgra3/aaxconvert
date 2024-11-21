# A Simple Audio conversion tool

This is a simple conversion tool to convert __aax__ files to __mp4__ and __m4b__ file formats.

## Installation process

### From Github

For easiest installation, use the following from a specific environment:

```bash
python3 -m pip install --upgrade -e aaxconvert @ git+https://github.com/avgra3/aaxconvert.git@main
```

An alternative to this would be to do the following:

```bash
git clone https://github.com/avgra3/aaxconvert.git
cd ./aaxconvert
python -m pip install --upgrade build
python -m build
python -m pip install install ./dist/aaxconvert-0.1.0-py3-none-any.whl
```

**Note:** For Linux or Mac systems, you may need to change "pip" to "pip3".

**Note:** For Anaconda/Miniconda users, this module is not currently in any repositories, however, you can still use pip to install the _aaxconvert_ package using the same command as above - but be aware that it may cause conflicts with packages you are using.

If you're unsure or want to help contribute your code, try installing using this command from the project root directory:

```bash
pip install editable .
```

## Usage

From your terminal, you can use the following:

```bash
aaxconvert myaudiofile.aax
```

This assumes you have added your activation bytes to the system environment. If they are not provided or have not been add to the command, you will receive an error message.

## Non-Python Requirements

The below are needed to be installed on your system and callable from python in order for this command to work.

- [FFMPEG](https://www.ffmpeg.org/)

## Development & Testing

To run the current test suite from a unix machine, run the [run_scripts.sh](run_scripts.sh) file from the root directory.

If there are any issues or bugs found, please open an Issue or Pull Request with the reccomended solution.

