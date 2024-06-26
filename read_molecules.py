from typing import TextIO, Dict, Tuple, Optional
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
    {'TEST': [('N', ('0.1', '0.2', '0.3')), ('N', ('0.2', '0.1', '0.0'))]}
    """

    # If there isn't a line, we're at the end of the file
    line = reader.readline()
    if not line:
        return None
    molecule = {}

    # Name of the molecule: "COMPND [name]"
    parts = line.split()
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
            atom_name = parts[2]
            others = tuple(parts[3:])
            atoms.append((atom_name, others))

    molecule[name] = atoms
    return molecule

def read_all_molecules(reader: TextIO) -> CompoundDict:
    """Read zero or more molecules from reader, returning a list of the molecule information.

    >>> compnd1 = 'COMPND T1\\nATOM N 0.1 0.2 0.3 \\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> compnd2 = 'COMPND T2\\nATOM N 0.1 0.2 0.3 \\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(compnd1 +compnd2)
    >>> result = read_all_molecules(infile)
    >>> result['T1']
if __name__ == "__main__":
    import doctest
    doctest.testmod()
