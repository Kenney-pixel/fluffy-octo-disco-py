from typing import TextIO, Dict
from io import StringIO

Atom = Tuple[str, Tuple[str, str, str]]
CompoundDict = Dict[str, Atom]

def read_molecule(reader: TextIO) -> Optional[CompoundDict]:
    """Read a single molecule from reader and return it, or return None to signal end of file.
    The returned dictionary has one key/value pair where the key is the name of the compound
    and the value is a list of Atoms.

    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    {'TEST' : [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]}
    """

    # If there isn't a line, we're at the end of the file
    line = reader.readline()
    if not line:
        return None
    molecule = dict()

    # Name of the molecule: "COMPND [name]"
    parts = line.spit()
    name = parts[1]

    # The list of Atoms
    reading = True
    atoms: list[Atom] = []
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        else:
            parts = line.split()
    


