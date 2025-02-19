#CHIPSEC: Platform Security Assessment Framework
#Copyright (c) 2010-2022, Intel Corporation
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; Version 2.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
#Contact information:
#chipsec@intel.com
#

import struct
import os
import string

import chipsec.file

BIT0 = 0x0001
BIT1 = 0x0002
BIT2 = 0x0004
BIT3 = 0x0008
BIT4 = 0x0010
BIT5 = 0x0020
BIT6 = 0x0040
BIT7 = 0x0080
BIT8 = 0x0100
BIT9 = 0x0200
BIT10 = 0x0400
BIT11 = 0x0800
BIT12 = 0x1000
BIT13 = 0x2000
BIT14 = 0x4000
BIT15 = 0x8000
BIT16 = 0x00010000
BIT17 = 0x00020000
BIT18 = 0x00040000
BIT19 = 0x00080000
BIT20 = 0x00100000
BIT21 = 0x00200000
BIT22 = 0x00400000
BIT23 = 0x00800000
BIT24 = 0x01000000
BIT25 = 0x02000000
BIT26 = 0x04000000
BIT27 = 0x08000000
BIT28 = 0x10000000
BIT29 = 0x20000000
BIT30 = 0x40000000
BIT31 = 0x80000000
BIT32 = 0x100000000
BIT33 = 0x200000000
BIT34 = 0x400000000
BIT35 = 0x800000000
BIT36 = 0x1000000000
BIT37 = 0x2000000000
BIT38 = 0x4000000000
BIT39 = 0x8000000000
BIT40 = 0x10000000000
BIT41 = 0x20000000000
BIT42 = 0x40000000000
BIT43 = 0x80000000000
BIT44 = 0x100000000000
BIT45 = 0x200000000000
BIT46 = 0x400000000000
BIT47 = 0x800000000000
BIT48 = 0x1000000000000
BIT49 = 0x2000000000000
BIT50 = 0x4000000000000
BIT51 = 0x8000000000000
BIT52 = 0x10000000000000
BIT53 = 0x20000000000000
BIT54 = 0x40000000000000
BIT55 = 0x80000000000000
BIT56 = 0x100000000000000
BIT57 = 0x200000000000000
BIT58 = 0x400000000000000
BIT59 = 0x800000000000000
BIT60 = 0x1000000000000000
BIT61 = 0x2000000000000000
BIT62 = 0x4000000000000000
BIT63 = 0x8000000000000000

BOUNDARY_1KB   = 0x400
BOUNDARY_2KB   = 0x800
BOUNDARY_4KB   = 0x1000
BOUNDARY_1MB   = 0x100000
BOUNDARY_2MB   = 0x200000
BOUNDARY_4MB   = 0x400000
BOUNDARY_8MB   = 0x800000
BOUNDARY_16MB  = 0x1000000
BOUNDARY_32MB  = 0x2000000
BOUNDARY_64MB  = 0x4000000
BOUNDARY_128MB = 0x8000000
BOUNDARY_256MB = 0x10000000
BOUNDARY_512MB = 0x20000000
BOUNDARY_1GB   = 0x40000000
BOUNDARY_2GB   = 0x80000000
BOUNDARY_4GB   = 0x100000000

ALIGNED_4KB   = 0xFFF
ALIGNED_1MB   = 0xFFFFF
ALIGNED_8MB   = 0x7FFFFF
ALIGNED_64MB  = 0x3FFFFFF
ALIGNED_128MB = 0x7FFFFFF
ALIGNED_256MB = 0xFFFFFFF

MASK_8b  = 0xFF
MASK_16b = 0xFFFF
MASK_32b = 0xFFFFFFFF
MASK_64b = 0xFFFFFFFFFFFFFFFF


def bit(bit_num):
    return int(1 << bit_num)


def is_set(val, bit_mask):
    return bool(val & bit_mask != 0)


def scan_single_bit_mask(bit_mask):
    for bit_num in range(0, 7):
        if bit_mask >> bit_num == 1:
            return bit_num


#
# Compression Types
#
COMPRESSION_TYPE_NONE = 0
COMPRESSION_TYPE_TIANO = 1
COMPRESSION_TYPE_UEFI = 2
COMPRESSION_TYPE_LZMA  = 3
COMPRESSION_TYPE_BROTLI = 4
COMPRESSION_TYPE_EFI_STANDARD = 5
COMPRESSION_TYPE_UNKNOWN = 6
COMPRESSION_TYPES_ALGORITHMS = [COMPRESSION_TYPE_LZMA, COMPRESSION_TYPE_TIANO, COMPRESSION_TYPE_UEFI, COMPRESSION_TYPE_BROTLI, COMPRESSION_TYPE_NONE]
COMPRESSION_TYPES = [COMPRESSION_TYPE_NONE, COMPRESSION_TYPE_TIANO, COMPRESSION_TYPE_UEFI, COMPRESSION_TYPE_LZMA, COMPRESSION_TYPE_BROTLI, COMPRESSION_TYPE_EFI_STANDARD, COMPRESSION_TYPE_UNKNOWN]

def DB(val):
    return struct.pack('<B', val)
def DW(val):
    return struct.pack('<H', val)
def DD(val):
    return struct.pack('<L', val)
def DQ(val):
    return struct.pack('<Q', val)

SIZE2FORMAT = {
    1: 'B',
    2: 'H',
    4: 'I',
    8: 'Q'
}

def bytestostring(mbytes):
    if isinstance(mbytes, bytes):
        return mbytes.decode("latin_1")
    else:
        return mbytes

def stringtobytes(mstr):
    if isinstance(mstr, str):
        return mstr.encode("latin_1")
    else:
        return mstr

def pack1(value, size):
    """Shortcut to pack a single value into a string based on its size."""
    return struct.pack(SIZE2FORMAT[size], value)

def unpack1(string, size):
    """Shortcut to unpack a single value from a string based on its size."""
    return struct.unpack(SIZE2FORMAT[size], string)[0]

def get_version():
    version_strs = []
    chipsec_folder = os.path.abspath(chipsec.file.get_main_dir())
    for fname in sorted([x for x in os.listdir(os.path.join(chipsec_folder, "chipsec")) if x.startswith('VERSION')]):
        version_file = os.path.join(chipsec_folder, "chipsec", fname)
        with open(version_file, "r") as verFile:
            version_strs.append(verFile.read().strip())
    return '-'.join(version_strs)

def is_printable(seq):
    return set(seq).issubset(set(string.printable))

def is_hex(maybe_hex):
    return all(char in string.hexdigits for char in maybe_hex)

def is_all_ones(value, size, width=8):
    mask = (1<<(size * width)) - 1
    return (mask == (mask & value))

def get_message():
    msg_str = ""
    chipsec_folder = os.path.abspath(chipsec.file.get_main_dir())
    msg_file = os.path.join(chipsec_folder, "chipsec", "MESSAGE")
    if os.path.exists(msg_file):
        with open(msg_file, "r") as msgFile:
            msg_str = msgFile.read()
    return msg_str
